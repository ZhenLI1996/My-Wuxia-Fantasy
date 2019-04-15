from character_util.character import NPC, Player
from character_util.character import TYPE_LV_UP_CAL, TYPE_REL_EVENTS
from character_util.character import lv_up_linear, lv_up_quad
from character_util.character import LV_UP_CONSTANT


class CharacterManager:
    _player = None
    _npc_dict = {}       # [ npc_id ]
    _max_npc_id = 0

    @property
    def player(self):
        return self._player

    def create_player(self,
                      name: str = "Player",
                      lv:   int = 1,
                      hp:   int = 1,
                      atkp: int = 0,
                      defp: int = 0,
                      exp:  int = 0,
                      lv_up_cal: TYPE_LV_UP_CAL = lv_up_linear(LV_UP_CONSTANT)):
        self._player = Player(name=name, lv=lv, hp=hp, atkp=atkp, defp=defp, exp=exp, lv_up_cal=lv_up_cal)


    @property
    def npc_dict(self):
        return self._npc_dict

    def add_npc(self,
                npc_id:     int = _max_npc_id+1,
                name:   str = "NPC",
                lv:     int = 1,
                hp:     int = 1,
                atkp:   int = 0,
                defp:   int = 0,
                rel_events: TYPE_REL_EVENTS = None):
        if npc_id in self._npc_dict:
            raise ValueError(f"npc id {npc_id} exists")

        self._npc_dict[npc_id] = NPC(npc_id=npc_id, name=name, lv=lv, hp=hp,
                                     atkp=atkp, defp=defp, rel_events=rel_events)

    def get_npc_by_id(self, npc_id):
        if npc_id not in self._npc_dict:
            raise ValueError(f"npc id {npc_id} not found")
        return self._npc_dict[npc_id]

if __name__ == "__main__":
    char_manager = CharacterManager()
    char_manager.create_player(
        name="Player",
        lv=1,
        hp=30,
        atkp=5,
        defp=2,
        exp=0,
        lv_up_cal=lv_up_quad(500)
    )
    player = char_manager.player
    player.add_exp(9873)
    print(player.lv, player.exp, player.req_exp_to_lv_up)

    char_manager.add_npc(
        name="NPC_1",
        lv=3,
        hp=100,
        atkp=1,
        defp=1,
        rel_events=set()
    )

    print(char_manager.npc_dict)