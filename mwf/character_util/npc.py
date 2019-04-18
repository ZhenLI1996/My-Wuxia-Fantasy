from .character import Character

from typing import Set
TYPE_REL_EVENTS = Set[int]


class NPC(Character):
    _npc_id = -1
    def __init__(self,
                 npc_id:    int = -1,
                 name:  str = "NPC",
                 lv:    int = 1,
                 hp:    int = 1,
                 atkp:  int = 0,
                 defp:  int = 0,
                 rel_events: TYPE_REL_EVENTS = None):
        super().__init__()
        self._npc_id = npc_id
        self._name = name
        self._lv = lv
        self._hp = hp
        self._atkp = atkp
        self._defp = defp
        self._rel_events = rel_events if rel_events else set()     # {event_id}

    def __repr__(self):
        return f"NPC(npc_id={self._npc_id}," \
               f"name={self._name}," \
               f"lv={self._lv}," \
               f"hp={self._hp}," \
               f"atkp={self._atkp}," \
               f"defp={self._defp}," \
               f"rel_events={self.rel_events})"

    def __str__(self):
        return f"NPC: {self._name}, Level: {self._lv}, HP: {self._hp}, " \
               f"ATK: {self._atkp}, DEF: {self._defp}"


    npc_id = property(fset=Character.setter("_npc_id", int), fget=Character.getter("_npc_id"))
    name = property(fset=Character.setter("_name", str), fget=Character.getter("_name"))
    lv = property(fset=Character.setter("_lv", int), fget=Character.getter("_lv"))
    hp = property(fset=Character.setter("_hp", int), fget=Character.getter("_hp"))
    atkp = property(fset=Character.setter("_atkp", int), fget=Character.getter("_atkp"))
    defp = property(fset=Character.setter("_defp", int), fget=Character.getter("_defp"))

    @property
    def rel_events(self):
        return self._rel_events

    def add_event(self, event_id: int):
        self._rel_events.add(event_id)

    def del_event(self, event_id: int):
        try:
            self._rel_events.remove(event_id)
        except KeyError:
            pass


