# Characters Design

- class `Character`: `character_util.Character`
  - class `NPC`: `character_util.NPC`
    - class `Trader`: `character_util.Trader`
  - class `Player`: `character_util.Player`
- class `CharacterManager`: `character_util.CharacterManager`

## `Character` - Base Class of All Characters

Attributes

- `_name`
- `_lv`
- `_hp`
- `_atkp`
- `_dtkp`
- `_money`
- `_bag_id`

Properties

- `name`: getter & setter
- `lv`: getter & setter
- `hp`: getter & setter
- `atkp`: getter & setter
- `defp`: getter & setter
- `money`: getter & setter
- `bag_id`: getter & setter

Methods:

- `add_money(value: int) -> int`: returns money value after changing
- `reduce_money(value: int) -> int`: returns money value after changing



## `NPC` - Base Class of All NPCs

Attributes

- `_rel_events`: `set` of `int`s
- `_move_method`: `callable` of `(Position) -> Position`

Properties

- `npc_id`: getter & setter
- `rel_events`: getter
- `move_method`: getter

Methods

- `add_event(event_id: int) -> None`
- `del_event(event_id: int) -> None`

## `Trader` - Class of Trader NPCs

TODO

## `Player` - Class of Player

Attributes

- `_exp`
- `_lv_up_cal`

Properties

- `lv_up_call`: getter
- `exp`: getter
- `req_exp_to_lv_up`: getter

Methods

- `add_exp(value: int) -> int`: returns current lv after exp added

## `CharacterManager` - Class of Character Management Utility

Attributes

- `_player`
- `_npc_dict`: `{ npc_id : NPC }`
- `_max_npc_id`

Properties

- `player`: getter
- `npc_dict`: getter

Methods

- `create_player(...) -> None`: parameters refer to `Player.__init__(...)`
- `add_npc(...) -> int`: returns NPC id, parameters refer to `NPC.__init__(...)`
- `get_npc_by_id(npc_id: int) -> .npc.NPC`: returns NPC object, raises `ValueError` when NPC id is not found