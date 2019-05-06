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

TODO