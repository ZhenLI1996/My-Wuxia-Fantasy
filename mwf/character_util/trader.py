from mwf.character_util.npc import NPC
from mwf.character_util.npc import TYPE_REL_EVENTS

# TODO:
# not finished yet!


class Trader(NPC):
    def __init__(self,
                 npc_id:    int = -1,
                 name:  str = "Trader",
                 lv:    int = 1,
                 hp:    int = 1,
                 atkp:  int = 0,
                 defp:  int = 0,
                 money:  int = 0,
                 rel_events: TYPE_REL_EVENTS = None):
        super().__init__(
            npc_id=npc_id,
            name=name,
            lv=lv,
            hp=hp,
            atkp=atkp,
            defp=defp,
            money=money,
            rel_events=rel_events,
        )




if __name__ == "__main__":
    t = Trader()