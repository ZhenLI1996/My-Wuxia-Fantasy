# Map Design

- class `Position`: `map_util.Position`
- class `Map`: `map_util.Map`

## `Position` - Class of Positions on Map

**Immutable**

Attributes

- `_x`
- `_y`

Properties

- `x`: getter
- `y`: getter

Methods

- `__add__(other: Position) -> Position`: returns a new `Position` object of the sum of inputs

Class Methods

- `Position.manhattan_distance(p0: Position, p1: Position) -> int`: returns the manhattan distance between `p0` and `p1`

## `Map` - Class of Maps

Attributes

- `_size`
- `_char2pos`: dict `{char_id : Position}`
- `_pos2chars`: dict `{Position: List[char_id]}`

Properties

- `size`: getter, (x, y)

Methods

- `add_char(char_id: int, init_pos: Position) -> None`: raises `ValueError` when `Position` not in map
- `get_pos_by_char_id(char_id: int) -> Position`: raises `ValueError` when not in 
- `get_char_ids_by_pos(pos: Position) -> List[int]`: raises `ValueError` when not in 
- `advance_on_time(new_pos_dict: Dict[int, Position]) -> None`: move all characters