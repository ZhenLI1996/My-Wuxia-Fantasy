from typing import Tuple
from mwf.infra import getter
import itertools
from .position import Position

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


    def __init__(self,
                 size: Tuple[int, int]):
        if size[0] <= 0 or size[1] <= 0:
            raise ValueError(f"size must be positive, not {size}")
        self._size = size
        self._char2pos = {}
        self._pos2chars = {
            pos : []
            for pos in itertools.product(range(size[0]), range(size[1]))
        }


    @property
    def size(self):
        return (self._size[0], self._size[1])


    def __contains__(self, item: Position):
        return item.x >= 0 and item.x < self._size[0] \
                and item.y >= 0 and item.y < self._size[1]

    def get_pos_by_char_id(self, char_id: int):
        if char_id not in self._char2pos:
            raise ValueError(f"character id {char_id} not found in map")
        return self._char2pos[char_id]

    def get_char_id_by_pos(self, pos: Position):
        if pos not in self._char2pos:
            raise ValueError(f"Position {pos} out of bound")
        return self._pos2chars[pos]
