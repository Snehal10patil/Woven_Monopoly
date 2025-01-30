from typing import List, Dict

class Board:
    def __init__(self, spaces: List[Dict]):
        self.spaces = spaces
        self.size = len(spaces)

    def get_space(self, position: int) -> Dict:
        return self.spaces[position % self.size]