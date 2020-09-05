class Grid:
    def __init__(self, row: int, col: int, mine: bool = False, flag: bool = False):
        self.number = -1
        self.row = row
        self.col = col
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
        self.number = -1
        self.flag = False
        self.mine = False
