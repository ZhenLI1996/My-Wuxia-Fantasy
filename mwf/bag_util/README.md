# Bags Design

- class `Bag`: `bag_util.bag.Bag`
- class `BagManager`: `bag_util.bag_manager.BagManager`

## `Bag` - Class of Bags

Attributes

- `_bag_id`
- `_container`: container if `{item_id : count}` 

Properties

- `bag_id`: getter
<!-- - `container`: getter -->

Methods

- `add_item(item_id: int, count: int = 1) -> None`
- `add_multi_items(item_ids: List[int], counts: List[int] = None) -> None`: raises `ValueError` if `len(item_ids) != len(counts)`
  - if `counts` is `None`:
    - for every `item_id` in `item_ids`, add one of this item
  - else:
    - for index `i`, add # `counts[i]` of `item_ids[i]`
- `peek_item_count(item_id: int) -> int`: returns `0` if `item_id` not found,
- `peek_multi_item_counts(item_ids: List[int]) -> List[Tuple[int, int]]`: returns `0` if `item_id` not found, otherwise the count
- `peek_all_item_counts() -> List[int]`: returns `[(item_id, count), ...]`
- `remove_item(item_id: int, count: int = 1) -> None`: 
  - raises `ValueError` when `item_id` not fount
  - raises `ValueError` when input `count` is more than the count in `_container`
- `remove_multi_items(item_ids: List[int], counts: List[int] = None) -> None`: raises `ValueError` when `item_id` not fount, similar to `add_multi_items(...)`
- `clear() -> None`

## `BagManager` - Class of Bag Management

Attributes

- `_bag_dict`
- `_max_bag_id`

Methods

- `add_bag(...) -> int`: returns event id, refer to `Bag.__init__(...)`
- `get_bag_by_id(bag_id: int) -> .bag.Bag`
