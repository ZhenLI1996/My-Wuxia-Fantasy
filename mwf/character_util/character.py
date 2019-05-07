# from typing import Callable, Any

from mwf.infra import getter, setter

class DeathError(Exception):
    pass


def adder(attr: str, callback_name: str = "", debug: bool = False):
    def add_any(self, value):
        nonlocal attr, callback_name, debug
        setattr(self, attr, getattr(self, attr) + value)
        callback = getattr(self, callback_name, None)
        if callback is not None:
            callback(value=value, debug=debug)

    return add_any


def reducer(attr, checker_name: str = "", callback_name: str = "", debug: bool = False):
    def reduce_any(self, value):
        nonlocal attr, checker_name, callback_name, debug
        checker = getattr(self, checker_name, None)
        if checker is not None:
            checker(value=value, debug=debug)
        setattr(self, attr, getattr(self, attr) - value)
        callback = getattr(self, callback_name, None)
        if callback is not None:
            callback(value=value, debug=debug)


    return reduce_any



class Character:
    _name = "Character"
    _lv = 0
    _hp = 0
    _max_hp = 0
    _atkp = 0
    _defp = 0
    _money = 0
    _bag_id = None

    def __init__(self,
                 name: str = "NPC",
                 lv: int = 1,
                 hp: int = 1,
                 max_hp: int = 1,
                 atkp: int = 0,
                 defp: int = 0,
                 money: int = 0,
                 bag_id: int = -1,
                 ):
        self._name  = name
        self._lv    = lv
        self._hp    = hp
        self._max_hp    = max_hp
        self._atk  = atkp
        self._def  = defp
        self._money = money
        self._bag_id = bag_id

    name = property(fset=setter("_name", str), fget=getter("_name"))
    lv = property(fset=setter("_lv", int), fget=getter("_lv"))
    hp = property(fset=setter("_hp", int), fget=getter("_hp"))
    max_hp = property(fset=setter("_max_hp", int), fget=getter("_max_hp"))
    atkp = property(fset=setter("_atkp", int), fget=getter("_atkp"))
    defp = property(fset=setter("_defp", int), fget=getter("_defp"))
    money = property(fset=setter("_money", int), fget=getter("_money"))
    bag_id = property(fset=setter("_bag_id", int), fget=getter("_bag_id"))

    def callback_debug_log(self, callback_name: str, debug: bool = False):
        if debug:
            print(f"`Character` callback debug log: in object (id={id(self)}) callback={callback_name}")

    def add_max_hp_callback(self, value=None, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="add_max_hp_callback")
        if value is not None:
            self._hp += value

    add_max_hp = adder(attr="max_hp", callback_name="add_max_hp_callback", debug=False)

    def check_reduce_max_hp(self, value, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="check_reduce_max_hp")
        if self._max_hp - value <= 0:
            raise ValueError(f"cannot reduce max_hp to <= 0, now {self._max_hp} - {value} = {self._max_hp - value}")

    def reduce_max_hp_callback(self, value=None, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="reduce_max_hp_callback")
        if value is not None:
            self._hp = min(self._max_hp, self._hp)

    reduce_max_hp = reducer(attr="max_hp", checker_name="check_reduce_max_hp",
                            callback_name="reduce_max_hp_callback")

    def add_hp_callback(self, value=None, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="add_hp_callback")
        if value is not None:
            self._hp = min(self._max_hp, self._hp)

    add_hp = adder(attr="hp", callback_name="add_hp_callback")

    def reduce_hp_callback(self, value=None, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="reduce_hp_callback")
        if self._hp <= 0:
            self._hp = 0
            raise DeathError()

    reduce_hp = reducer(attr="hp", callback_name="reduce_hp_callback")

    add_atkp = adder(attr="atkp")
    reduce_atkp = reducer(attr="atkp")
    add_defp = adder(attr="defp")
    reduce_defp = reducer(attr="defp")

    def check_reduce_money(self, value, debug: bool = False):
        self.callback_debug_log(debug=debug, callback_name="check_reduce_money")
        if self._money - value <= 0:
            raise ValueError(f"cannot reduce money to <= 0, now {self._money} - {value} = {self._money - value}")

    add_money = adder(attr="money")
    reduce_money = reducer(attr="money", checker_name="check_reduce_money")

# # adder & reducer
# # it seems that this hack does not work
# # because __dict__ is read-only
#
#
# # ====== in class ======
#     def callback_debug_log(self, callback_name: str, debug: bool = False):
#         if debug:
#             print(f"in object (id={id(self)}) callback={callback_name}")
#
#
#     def add_max_hp_callback(self, value=None, debug: bool = False):
#         self.callback_debug_log(debug=debug, callback_name="add_max_hp_callback")
#         if value is not None:
#             self._hp += value
#
#     def check_reduce_max_hp(self, value):
#         if self._max_hp - value <= 0:
#             raise ValueError(f"cannot reduce max_hp to <= 0, now {self._max_hp} - {value} = {self._max_hp - value}")
#
#     def reduce_max_hp_callback(self, value=None):
#         self._hp = min(self._hp, self._max_hp)
#
# # ====== out of class ======
#
# def adder(attr: str, callback_name: str, debug: bool = False):
#     def add_any(self, value):
#         nonlocal attr, callback_name, debug
#         setattr(self, attr, getattr(self, attr) + value)
#         call_back = self.__dict__.get(callback_name, None)
#         if call_back is not None:
#             call_back(self=self, value=value, debug=debug)
#
#     return add_any
#
#
# def reducer(attr):
#     def reduce_any(self, value):
#         nonlocal attr
#         setattr(self, attr, getattr(self, attr) - value)
#
#     return reduce_any
#
#
# attrs = ["hp", "max_hp", "atkp", "defp", "money"]
# for attr in attrs:
#     Character.__dict__.put(f"add_{attr}", adder(f"_{attr}", callback_name="add_max_hp_callback", debug=True))
#     # Character.__dict__[f"add_{attr}"] = adder(f"_{attr}", callback_name="add_max_hp_callback", debug=True)
#     # Character.__dict__[f"reduce_{attr}"] = reducer(f"_{attr}")