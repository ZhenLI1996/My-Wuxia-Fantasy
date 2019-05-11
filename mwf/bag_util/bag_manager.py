# TODO: BagManager

from .bag import Bag

class BagManager:
    _bag_dict = {}
    _max_bag_id = 0

    def add_bag(self,
                bag_id: int = _max_bag_id + 1):

        if bag_id in self._bag_dict:
            raise ValueError(f"bag id {bag_id} exists")
        self._bag_dict[bag_id] = Bag(bag_id=bag_id)
        self._max_bag_id = max(self._max_bag_id, bag_id)

    def get_bag_by_id(self, bag_id: int):
        if bag_id not in self._bag_dict:
            raise ValueError(f"npc id {bag_id} not found")
        return self._bag_dict[bag_id]


