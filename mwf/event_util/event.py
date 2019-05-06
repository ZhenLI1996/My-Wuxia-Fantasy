import json
import os

_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

SCRIPT_PATH = os.path.join(_CURRENT_DIR, "scripts")

# TODO:
# 1. event condition


class Event:
    def __init__(self,
                 event_id: int,
                 filename: str,
                 path:     str = SCRIPT_PATH):
        self._event_id = event_id
        self._full_path = os.path.join(path, filename)
        with open(self._full_path, "r", encoding="utf-8") as fin:
            self._j = json.load(fin)
        self._condition = lambda _ : True  # TODO (event condition)
        self._node = self._j["content"]["start_node_id"]

    @property
    def event_id(self):
        return self._event_id

    @property
    def condition(self):
        return self._condition

    @property
    def current_node_content(self):
        return self._j["content"]["nodes"][self._node]


    def is_end(self):
        return self._node is None

    def choose(self, choice_id):
        choices_buf = self._j["content"]["nodes"]\
                                 [self._node]["choices"]
        if choice_id not in choices_buf:
            raise ValueError(f"choice id {choice_id} not found")
        self._node = choices_buf[choice_id]["next"]


if __name__ == "__main__":
    e = Event(event_id=0, filename="greeting.json")
    print(e.event_id)
    while not e.is_end():
        content = e.current_node_content
        print(content["text"])
        for choice_id, choice_content in content["choices"].items():
            print(choice_id, choice_content["text"])
        user_choice = input().strip()
        e.choose(user_choice)
