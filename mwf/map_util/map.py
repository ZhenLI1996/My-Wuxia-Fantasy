from typing import Tuple, Dict
# from mwf.infra import getter
import itertools
from .position import Position
import copy


# TODO: Map

class Map:
    # pass
    # def __init__(self,
    #              size: Tuple[int, int],
    #              char_manager):
    #     from mwf.character_util import CharacterManager
    #     if not isinstance(char_manager, CharacterManager):
    #         raise ValueError(f"char_manager must be a CharacterManager object, not {type(char_manager)}")
    #     if size[0] <= 0 or size[1] <= 0:
    #         raise ValueError(f"size must be positive, not {size}")
    #     if char_manager is None:
    #         raise ValueError(f"char_manager cannot be None")
    #     self._size = size
    #     self._char_manager = char_manager

    @classmethod
    def gen_char2pos(cls):
        return {}

    @classmethod
    def gen_pos2chars(cls, size: Tuple[int, int]):
        return {
            xy : []
            for xy in itertools.product(range(size[0]), range(size[1]))
        }

    def __init__(self,
                 size: Tuple[int, int]):
        if size[0] <= 0 or size[1] <= 0:
            raise ValueError(f"size must be positive, not {size}")
        self._size = size
        # self._char2pos = copy.deepcopy(self._init_char2pos)
        # self._pos2chars = copy.deepcopy(self._init_pos2chars)
        self._char2pos = Map.gen_char2pos()
        self._pos2chars = Map.gen_pos2chars(size=self._size)
        self._player_pos = Position(0, 0)

    @property
    def size(self):
        return (self._size[0], self._size[1])

    def __contains__(self, item: Position):
        return item.x >= 0 and item.x < self._size[0] \
                and item.y >= 0 and item.y < self._size[1]

    def __str__(self):
        return "\n".join(
            "; ".join(
                f"({x},{y}): {self.get_char_id_by_pos((x, y))}"
                for y in range(self._size[1])
            )
            for x in range(self._size[0])
        )

    def gen_str_with_player(self, player_pos):
        if (isinstance(player_pos, Position) or isinstance(player_pos, tuple)) \
                and player_pos in self._pos2chars:
            self._pos2chars[player_pos].append("player")
            buf = str(self)
            self._pos2chars[player_pos].remove("player")
            return buf
        else:
            raise TypeError(f"argument pos must be Position or Tuple[int, int], not {type(player_pos)}")

    def add_char(self, char_id: int, init_pos: Position):
        if init_pos not in self._pos2chars:
            raise ValueError(f"init Position {init_pos} out of bound")
        if char_id in self._char2pos:
            raise ValueError(f"character id {char_id} already exists")
        self._char2pos[char_id] = init_pos
        self._pos2chars[init_pos].append(char_id)

    def get_pos_by_char_id(self, char_id: int):
        if char_id not in self._char2pos:
            raise ValueError(f"character id {char_id} not found in map")
        return self._char2pos[char_id]

    def get_char_id_by_pos(self, pos):
        if isinstance(pos, Position) or isinstance(pos, tuple):
            if pos not in self._pos2chars:
                raise ValueError(f"Position {pos} out of bound")
            return self._pos2chars[pos]
        raise TypeError(f"argument pos must be Position or Tuple[int, int], not {type(pos)}")

    def advance_on_time(self, new_pos_dict: Dict[int, Position]):
        new_pos2chars = Map.gen_pos2chars(size=self._size)
        new_char2pos = Map.gen_char2pos()
        for char_id, new_pos in new_pos_dict.items():
            if char_id not in self._char2pos:
                raise ValueError(f"character id {char_id} not found in map")
            if new_pos not in self._pos2chars:
                raise ValueError(f"Position {new_pos} out of bound")
        for char_id, new_pos in new_pos_dict.items():
            new_pos2chars[new_pos].append(char_id)
            new_char2pos[char_id] = new_pos
        del self._pos2chars
        self._pos2chars = new_pos2chars
        del self._char2pos
        self._char2pos = new_char2pos

