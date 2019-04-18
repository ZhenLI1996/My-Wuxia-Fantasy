from character_util.character_manager import CharacterManager
from event_util.event_manager import EventManager

char_manager = CharacterManager()
event_manager = EventManager()


# create the greeting event
event_id = event_manager.add_event(filename="greeting.json")

# create the NPC
npc_id = char_manager.add_npc(rel_events={event_id})

# create player
player = char_manager.create_player()

# TODO:
# 1. map module

# === run ===

print("test starts")

input("输入任意字符前进一步，你将会遇到NPC\n")

NPC = char_manager.get_npc_by_id(npc_id)
event = None
for event_id in NPC.rel_events:
    temp_event = event_manager.get_event_by_id(event_id)
    if temp_event.condition({}):
        event = temp_event
        break
if event:
    while not event.is_end():
        content = event.current_node_content
        print(content["text"])
        for choice_id, choice_content in content["choices"].items():
            print(choice_id, choice_content["text"])
        user_choice = input().strip()
        event.choose(user_choice)

print("test ends")
