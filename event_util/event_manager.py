from event_util.event import Event
from event_util.event import SCRIPT_PATH


class EventManager:
    _event_dict = {}        # { event_id : Event }
    _max_event_id = 0

    def add_event(self,
                  filename: str,
                  event_id: int = _max_event_id + 1,
                  path:     str = SCRIPT_PATH):
        if event_id in self._event_dict:
            raise ValueError(f"event id {event_id} exists")
        self._event_dict[event_id] = Event(event_id=event_id,
                                           filename=filename,
                                           path=path)
        return event_id

    def get_event_by_id(self, event_id):
        if event_id not in self._event_dict:
            raise ValueError(f"event id {event_id} not found")
        return self._event_dict[event_id]



