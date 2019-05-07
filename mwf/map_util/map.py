from typing import Tuple

# TODO: Map

class Map:
    # pass
    def __init__(self,
                 size: Tuple[int, int],
                 char_manager):
        from mwf.character_util import CharacterManager
        if not isinstance(char_manager, CharacterManager):
            raise ValueError(f"char_manager must be a CharacterManager object, not {type(char_manager)}")
        if size[0] <= 0 or size[1] <= 0:
            raise ValueError(f"size must be positive, not {size}")
        if char_manager is None:
            raise ValueError(f"char_manager cannot be None")
        self._size = size
        self._char_manager = char_manager



    # def