from typing import Set
from typing import Callable


TYPE_REL_EVENTS = Set[int]
TYPE_LV_UP_CAL = Callable[[int], int]

class Character:
    _name = "Character"
    _lv = 0
    _hp = 0
    _atkp = 0
    _dtkp = 0

    def __init__(self,
                 name: str = "NPC",
                 lv: int = 1,
                 hp: int = 1,
                 atkp: int = 0,
                 defp: int = 0,
                 ):
        self._name  = name
        self._lv    = lv
        self._hp    = hp
        self._atkp  = atkp
        self._defp  = defp

    @classmethod
    def setter(cls, attr, req_type):
        def set_any(self, value):
            nonlocal attr, req_type
            if not isinstance(value, req_type):
                raise ValueError(f"value {value} is not type {req_type}")
            setattr(self, attr, value)
        return set_any

    @classmethod
    def getter(cls, attr):
        def get_any(self):
            nonlocal attr
            if not hasattr(self, attr):
                raise ValueError(f"attribute {attr} not found")
            return getattr(self, attr)
        return get_any




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


def lv_up_linear(k):
    def helper(lv):
        nonlocal k
        return k * (1+lv) * lv // 2
    return helper

def lv_up_quad(k):
    def helper(lv):
        nonlocal k
        return k * lv * (lv+1) * (2*lv+1) // 6
    return helper

LV_UP_CONSTANT = 100


class Player(Character):
    _exp = 0
    def __init__(self,
                 name:  str = "Player",
                 lv:    int = 1,
                 hp:    int = 1,
                 atkp:  int = 0,
                 defp:  int = 0,
                 exp:   int = 0,
                 lv_up_cal: TYPE_LV_UP_CAL = lv_up_linear(LV_UP_CONSTANT)):
        super().__init__()
        self._name = name
        self._lv   = lv
        self._hp   = hp
        self._atkp = atkp
        self._defp = defp
        self._exp  = exp
        self._lv_up_cal = lv_up_cal

    def __repr__(self):
        return f"Player(name={self._name}," \
               f"lv={self._lv}," \
               f"hp={self._hp}," \
               f"atkp={self._atkp}," \
               f"defp={self._defp}," \
               f"exp={self._exp}," \
               f"lv_up_cal={self._lv_up_cal})"

    def __str__(self):
        return f"Player: {self._name}, Level: {self._lv}, HP: {self._hp}, " \
               f"ATK: {self._atkp}, DEF: {self._defp}, EXP: {self._exp}, EXP to Level Up: {self.req_exp_to_lv_up}"


    name = property(fset=Character.setter("_name", str), fget=Character.getter("_name"))
    lv = property(fset=Character.setter("_lv", int), fget=Character.getter("_lv"))
    hp = property(fset=Character.setter("_hp", int), fget=Character.getter("_hp"))
    atkp = property(fset=Character.setter("_atkp", int), fget=Character.getter("_atkp"))
    defp = property(fset=Character.setter("_defp", int), fget=Character.getter("_defp"))

    @property
    def lv_up_call(self):
        return self._lv_up_cal

    @property
    def exp(self):
        return self._exp

    def add_exp(self, value):
        self._exp += value
        while self.lv_up_call(self._lv) <= self._exp:
            self._lv += 1
        return self._lv

    @property
    def req_exp_to_lv_up(self):
        return self.lv_up_call(self._lv)


if __name__ == "__main__":
    p = Player()
    print(p.exp)
    print(p.lv)
    p.add_exp(1)
    print(p.exp, p.lv, p.req_exp_to_lv_up)
    p.add_exp(LV_UP_CONSTANT)
    print(p.exp, p.lv, p.req_exp_to_lv_up)
    p.add_exp(LV_UP_CONSTANT * 100)
    print(p.exp, p.lv, p.req_exp_to_lv_up)
    print(p)
    print(repr(p))