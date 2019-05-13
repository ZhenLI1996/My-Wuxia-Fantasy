from mwf.character_util import CharacterManager
from mwf.infra.mwf_errors import DeathError

def log(message, *objs):
    print(message)
    for obj in objs:
        print("\t", obj)


char_manager = CharacterManager()


# Player

# create
print("=== player ===")
char_manager.create_player(
    name="new_player",
    lv=2,
    hp=100,
    max_hp=110,
    atkp=10,
    defp=10,
    exp=0,
    money=400,
)
player = char_manager.player
log("create player", player)

log("single attr", player.hp)

# change name
player.name = "yay!"
log("change player name", player)

# add exp
old_lv = player.lv
new_lv = player.add_exp(1000)
log("add exp", *("level up to {}".format(i) for i in range(old_lv + 1, new_lv + 1)), player)

# add max hp
player.add_max_hp(100)
log("add max hp", player)

# reduce max hp
player.reduce_max_hp(50)
log("reduce max hp", player)

# before add hp, set hp to < max_hp for testing
player.hp = player.max_hp // 2
log("before manipulating hp, reduce hp down", player)

# add hp
player.add_hp(10)
log("add small hp", player)
player.add_hp(1000)
log("add huge hp", player)

# reduce hp
player.reduce_hp(10)
log("reduce small hp", player)
try:
    player.reduce_hp(1000)
except DeathError:

    log("reduce huge hp", player, "DEAD!")

# add hp
player.add_hp(1)

# add atkp
player.add_atkp(10)
log("add atkp", player)

# reduce atkp
player.reduce_atkp(10)
log("reduce atkp", player)

# add defp
player.add_defp(10)
log("add defp", player)

# reduce defp
player.reduce_defp(10)
log("reduce defp", player)

# add money
player.add_money(10)
log("add money", player)

# reduce money
player.reduce_money(10)
log("reduce money", player)
