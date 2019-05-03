
class Character:
    _name = "Character"
    _lv = 0
    _hp = 0
    _atkp = 0
    _dtkp = 0
    _money = 0

    def __init__(self,
                 name: str = "NPC",
                 lv: int = 1,
                 hp: int = 1,
                 atkp: int = 0,
                 defp: int = 0,
                 money: int = 0,
                 ):
        self._name  = name
        self._lv    = lv
        self._hp    = hp
        self._atkp  = atkp
        self._defp  = defp
        self._money = money

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
