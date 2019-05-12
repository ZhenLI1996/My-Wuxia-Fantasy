import mwf

import random

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

    # repl
    while True:
        if debug:
            log("=== map ===\n", map)
        # TODO