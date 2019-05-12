# Immutable

class Position:
    def __init__(self,
                 x: int,
                 y: int):
        # self._is_init = True
        # self._x = x
        # self._y = y
        # self._is_init = False
        self.__dict__["_x"] = x
        self.__dict__["_y"] = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __setattr__(self, key, value):
        raise AttributeError("Can't set attribute {}, Position objects are immutable".format(key))
        # if not self._is_init:
        #     raise AttributeError("Can't set attribute {}, Position objects are immutable".format(key))
        # else:
        #     self.__dict__[key] = value

    def __add__(self, other) -> 'Position':
        if isinstance(other, Position):
            return Position(
                x=self._x + other._x,
                y=self._y + other._y
            )
        elif isinstance(other, tuple):
            if len(other) != 2:
                raise ValueError(f"position {other} must be of len 2")
            return Position(
                x=self._x + other[0],
                y=self._y + other[1]
            )
        else:
            raise TypeError("unsupported operand type(s) for +: 'Position' and '{}'".format(type(other)))
    
    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._x == other.x and self._y == other.y
        elif isinstance(other, tuple):
            return len(other) == 2 and self._x == other[0] and self._y == other[1]

    @classmethod
    def manhattan_distance(cls, p0: 'Position', p1: 'Position') -> int:
        return abs(p0._x - p1._x) + abs(p0._y - p1._y)

