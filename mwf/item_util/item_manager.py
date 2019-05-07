from .item import Item

class ItemManager:
    _item_dict = {}
    _max_item_id = 0

    def add_item(self,
                  name: str,
                  price: int,
                  item_id: int = _max_item_id + 1,
                  desc: str = "an item"
                  ):
        if item_id in self._item_dict:
            raise ValueError(f"item id {item_id} already exists")
        self._item_dict[item_id] = Item(
            item_id=item_id,
            name=name,
            price=price,
            desc=desc,
        )
        self._max_item_id = max(self._max_item_id, item_id)
        return item_id

    def get_item_by_id(self, item_id: int):
        if item_id not in self._item_dict:
            raise ValueError(f"item id {item_id} not found")
        return self._item_dict[item_id]
