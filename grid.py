class Grid:
    def __init__(self, row: int, col: int, mine: bool, flag: bool):
        self.number = 0
        self.row = row
        self.col = col
        self.mine = mine
        self.flag = flag

    def set_mine(self, is_mine: bool):
        self.mine = is_mine

    def is_mine(self):
        return self.mine

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number
