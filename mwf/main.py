import mwf

import random
import time

MAX_X = 3
MAX_Y = 3

def log(*args, **kwargs):
    print(*args, **kwargs)

def run(debug=False):
    log("Prototype of My Wuxia Fantasy")
    log("Still Developing")

    log("Loading ", end="")

    bag_manager = mwf.BagManager()
    char_manager = mwf.CharacterManager()
    event_manager = mwf.EventManager()
    item_manager = mwf.ItemManager()
    map = mwf.Map(size=(MAX_X, MAX_Y))

    log("...", end="")

    # create the greeting event
    event_id = event_manager.add_event(filename="greeting.json")

    # create the NPC
    npc_id = char_manager.add_npc(rel_events={event_id},
                                  move_method=mwf.character_util.npc.random_move)

    # create player
    player = char_manager.create_player()

    # add npcs to map
    npc_pos = mwf.Position(random.randrange(MAX_X), random.randrange(MAX_Y))
    map.add_char(char_id=npc_id,
                 init_pos=npc_pos)

    log("...", end="")

    # generate player pos
    while True:
        player_pos = mwf.Position(random.randrange(MAX_X), random.randrange(MAX_Y))
        if player_pos == npc_pos:
            continue
        else:
            break

    log(" Done!", end="")

    if debug:
        log("=== initial map ===\n", map.gen_str_with_player(player_pos=player_pos))

    # repl
    while True:
        command = input("please input command: ")
        if command.lower() == "stop":
            print("terminates")
            break
        elif command.lower().startswith("s"):
            buf = player_pos
        elif command.lower().startswith("u"):
            buf = player_pos + (-1, 0)
        elif command.lower().startswith("d"):
            buf = player_pos + (1, 0)
        elif command.lower().startswith("l"):
            buf = player_pos + (0, -1)
        elif command.lower().startswith("r"):
            buf = player_pos + (0, 1)
        else:
            print("please input correct command (up/down/left/right/stay)")
            continue

        if buf not in map:
            print("cannot move: going out of bound")
            continue

        player_pos = buf

        if debug:
            log("=== current ===\n", map.gen_str_with_player(player_pos=player_pos))

        char_ids = map.get_char_id_by_pos(pos=player_pos)
        for c_id in char_ids:
            npc = char_manager.get_npc_by_id(c_id)
            for e_id in npc.rel_events:
                event = event_manager.get_event_by_id(e_id)
                while not event.is_end():
                    content = event.current_node_content
                    print(content["text"])
                    for choice_id, choice_content in content["choices"].items():
                        print(choice_id, choice_content["text"])
                    user_choice = input().strip()
                    event.choose(user_choice)

        # advance on time
        npc_new_pos = {}
        for npc_id in char_manager.npc_ids:
            npc_new_pos[npc_id] = char_manager.get_npc_by_id(npc_id)\
                                    .move_method(
                                        map=map,
                                        p=map.get_pos_by_char_id(char_id=npc_id)
                                    )
        map.advance_on_time(npc_new_pos)

        if debug:
            time.sleep(1)
            log("=== day ends ===\n", map.gen_str_with_player(player_pos=player_pos))
