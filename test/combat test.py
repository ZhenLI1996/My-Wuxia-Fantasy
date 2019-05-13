import mwf

char_manager = mwf.CharacterManager()

char_manager.create_player(
    name="Warrior",
    lv=3,
    hp=100,
    max_hp=100,
    atkp=10,
    defp=5,
    exp=30
)

opponent_id = char_manager.add_npc(
    name="Tiger",
    lv=2,
    hp=80,
    max_hp=80,
    atkp=8,
    defp=4
)

player = char_manager.player
opponent = char_manager.get_npc_by_id(opponent_id)

