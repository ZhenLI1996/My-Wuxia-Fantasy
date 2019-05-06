# Events Design

- class `Event`: `event_util.Event`
- class `EventManager`: `event_util.EventManager`

## `Event` - Class of Events

Attributes

- `_event_id`
- `_full_path`: full path of corresponding scripts
- `_condition`: `callable` to check if this event should be triggered
- `_node`: current node in the FSM

Properties

- `event_id`: getter
- `condition`: getter
- `current_node_content`: getter, get current node of this event

Methods

- `is_end() -> bool`: returns `True` if current node is `None` (i.e. the event has already ended)
- `choose(choice_id: int) -> None`: choose certain option based on `choice_id`, raises `ValueError` when `choice_id` is not found

## `EventManager` - Class of Event Management Utility

Attributes

- `_event_dict`
- `_max_event_id`

Methods

- `add_event(...) -> int`: returns event id, refer to `Event.__init__(...)`
- `get_event_by_id(event_id: int) -> .event_manager.Event`
