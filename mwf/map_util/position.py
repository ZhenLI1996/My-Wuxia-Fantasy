# Immutable
class Position:
    def __init__(self,
                 x: int,
                 y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __setattr__(self, key, value):
        raise AttributeError("Can't set attribute {}, Position objects are immutable".format(key))

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(
                x=self._x + other._x,
                y=self._y + other._y
            )
        else:
            raise TypeError("unsupported operand type(s) for +: 'Position' and '{}'".format(type(other)))

    @classmethod
    def manhattan_distance(cls, p0, p1):
        return abs(p0._x - p1._x) + abs(p0._y - p1._y)

