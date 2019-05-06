from .character import Character
from .character import setter, getter

from typing import Set
TYPE_REL_EVENTS = Set[int]

from mwf.map_util.position import Position
from typing import Callable
TYPE_MOVE_METHOD = Callable[[Position], Position]

import random

def random_move(p: Position) -> Position:
    r = random.randrange(4)
    if r == 0:
        return p + Position(0, 1)
    elif r == 1:
        return p + Position(0, -1)
    elif r == 2:
        return p + Position(1, 0)
    else:
        return p + Position(-1, 0)


class NPC(Character):
    _npc_id = -1
    def __init__(self,
                 npc_id:    int = -1,
                 name:  str = "NPC",
                 lv:    int = 1,
                 hp:    int = 1,
                 max_hp:    int = 1,
                 atkp:  int = 0,
                 defp:  int = 0,
                 money: int = 0,
                 bag_id: int = -1,
                 rel_events: TYPE_REL_EVENTS = None,
                 move_method: TYPE_MOVE_METHOD = random_move):
        super().__init__()
        self._npc_id = npc_id
        self._name = name
        self._lv = lv
        self._hp = hp
        self._max_hp = max_hp
        self._atkp = atkp
        self._defp = defp
        self._money = money
        self._bag_id = bag_id
        self._rel_events = rel_events if rel_events else set()     # {event_id}
        self._move_method = move_method

    def __repr__(self):
        return f"NPC(npc_id={self._npc_id}," \
               f"name={self._name}," \
               f"lv={self._lv}," \
               f"hp={self._hp}," \
               f"atkp={self._atkp}," \
               f"defp={self._defp}," \
               f"money={self._money}," \
               f"bag_id={self._bag_id}," \
               f"rel_events={self.rel_events}," \
               f"move_method={self._move_method})"

    def __str__(self):
        return f"NPC: {self._name}, Level: {self._lv}, HP: {self._hp}, " \
               f"ATK: {self._atkp}, DEF: {self._defp}, money: {self._money}"


    npc_id = property(fset=setter("_npc_id", int), fget=getter("_npc_id"))
    # name = property(fset=Character.setter("_name", str), fget=Character.getter("_name"))
    # lv = property(fset=Character.setter("_lv", int), fget=Character.getter("_lv"))
    # hp = property(fset=Character.setter("_hp", int), fget=Character.getter("_hp"))
    # atkp = property(fset=Character.setter("_atkp", int), fget=Character.getter("_atkp"))
    # defp = property(fset=Character.setter("_defp", int), fget=Character.getter("_defp"))
    # money = property(fset=Character.setter("_money", int), fget=Character.getter("_money"))
    # bag_id = property(fset=Character.setter("_bag_id", int), fget=Character.getter("_bag_id"))

    @property
    def rel_events(self):
        return self._rel_events

    @property
    def move_method(self):
        return self._move_method

    def add_event(self, event_id: int):
        self._rel_events.add(event_id)

    def del_event(self, event_id: int):
        try:
            self._rel_events.remove(event_id)
        except KeyError:
            pass


