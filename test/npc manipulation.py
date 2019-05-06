# from mwf.map_util import Map
# TODO: I have to import Map first to avoid circular import problem. fix it asap!
from mwf.character_util import CharacterManager, DeathError

def log(message, *objs):
    print(message)
    for obj in objs:
        print("\t", obj)


char_manager = CharacterManager()


# Player

# create
print("=== npc ===")
npc_id = char_manager.add_npc(
    name="fridge",
    lv=99,
    hp=1000,
    max_hp=9999,
    atkp=1552,
    defp=1248,
    money=400,
)
npc = char_manager.get_npc_by_id(npc_id=npc_id)
log("create npc", "npc_id = {}".format(npc_id), npc)

# change name
npc.name = "yay!"
log("change npc name", npc)

# add max hp
npc.add_max_hp(100)
log("add max hp", npc)

# reduce max hp
npc.reduce_max_hp(50)
log("reduce max hp", npc)

# before add hp, set hp to < max_hp for testing
npc.hp = npc.max_hp // 2
log("before manipulating hp, reduce hp down", npc)

# add hp
npc.add_hp(1000)
log("add small hp", npc)
npc.add_hp(10000)
log("add huge hp", npc)

# reduce hp
npc.reduce_hp(10)
log("reduce small hp", npc)
try:
    npc.reduce_hp(100000)
except DeathError:

    log("reduce huge hp", npc, "DEAD!")

# add hp
npc.add_hp(1)

# add atkp
npc.add_atkp(10)
log("add atkp", npc)

# reduce atkp
npc.reduce_atkp(10)
log("reduce atkp", npc)

# add defp
npc.add_defp(10)
log("add defp", npc)

# reduce defp
npc.reduce_defp(10)
log("reduce defp", npc)

# add money
npc.add_money(10)
log("add money", npc)

# reduce money
npc.reduce_money(10)
log("reduce money", npc)
