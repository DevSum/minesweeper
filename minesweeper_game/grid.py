from enum import Enum


class GridState(Enum):
    CLOSED = 0,
    NUMBER = 1,
    BOMB = 2,
    FLAG = 3,
    ZERO = 4,


class Grid:
    def __init__(self, row: int, col: int, mine: bool = False, flag: bool = False):
        self.number = 0
        self.row = row
        self.col = col
        self.state = GridState.CLOSED
        self.mine = mine
        self.flag = flag

    def set_mine(self, is_mine: bool):
        self.mine = is_mine

    def is_mine(self):
        return self.mine

    def set_number(self, number: int):
        self.number = number

    def get_number(self):
        return self.number

    def new(self):
        self.state = GridState.CLOSED
        self.number = 0
        self.flag = False
        self.mine = False

    def setState(self, state: GridState):
        self.state = state

    def getState(self):
        return self.state
