from mwf.infra import getter
from typing import List, Tuple

class Bag:
    def __init__(self,
                 bag_id: int):
        self._bag_id = bag_id
        self._container = {}

    bag_id = property(fget=getter(attr="_bag_id"))
    # container = property(fget=getter(attr="_container"))

    def add_item(self, item_id: int, count: int = 1) -> None:
        if item_id not in self._container:
            self._container[item_id] = 0
        self._container[item_id] += count

    def add_multi_items(self, item_ids: List[int], counts: List[int] = None) -> None:
        if len(item_ids) == 0:
            return
        if len(item_ids) != len(counts):
            raise ValueError(f"list of item ids and counts are not the same length ({len(item_ids)} and {len(counts)})")
        if counts is None:
            d = {item_id : 1 for item_id in item_ids}
        else:
            d = {item_ids[i] : counts[i] for i in range(len(item_ids))}
        self._container.update(d)

    def peek_item_count(self, item_id: int) -> int:
        return 0 if item_id not in self._container else self._container[item_id]

    def peek_multi_item_counts(self, item_ids: List[int]) -> List[Tuple[int, int]]:
        return [(item_id, 0 if item_id not in self._container else self._container[item_id])
                for item_id in item_ids]

    def peek_all_item_counts(self, ) -> List[int]:
        return list(self._container.items())

    def remove_item(self, item_id: int, count: int = 1) -> None:
        if item_id not in self._container:
            raise ValueError(f"item id {item_id} not found")
        elif count > self._container[item_id]:
            raise ValueError(f"item id {item_id} not found")

        if self._container[item_id] == count:
            del self._container[item_id]
        else:
            self._container[item_id] -= count

    def remove_multi_items(self, item_ids: List[int], counts: List[int] = None) -> None:
        if len(item_ids) == 0:
            return
        if len(item_ids) != len(counts):
            raise ValueError(f"list of item ids and counts are not the same length ({len(item_ids)} and {len(counts)})")

        for i in range(len(item_ids)):
            item_id = item_ids[i]
            count = counts[i]
            if item_id not in self._container:
                raise ValueError(f"item id {item_id} not found")
            elif count > self._container[item_id]:
                raise ValueError(f"item id {item_id} not found")

        for i in range(len(item_ids)):
            item_id = item_ids[i]
            count = counts[i]
            if self._container[item_id] == count:
                del self._container[item_id]
            else:
                self._container[item_id] -= count

    def clear(self) -> None:
        self._container.clear()
