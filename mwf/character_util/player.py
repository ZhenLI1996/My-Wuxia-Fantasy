from .character import Character

from typing import Callable
TYPE_LV_UP_CAL = Callable[[int], int]

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
