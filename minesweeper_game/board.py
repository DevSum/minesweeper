import random

from minesweeper_game.grid import Grid


class Board:
    def __init__(self, row_n: int, col_n: int):
        self.row_n = row_n
        self.col_n = col_n

        self.board = [[Grid(i, j) for j in range(col_n)] for i in range(row_n)]

    def refresh_grid(self):
        for row in self.board:
            for col in row:
                col.new()

    def get_grid(self, row, col):
        return self.board[row][col]

    def generate_mine(self, mine_count: int):
        bomb_positions = []
        for i in range(mine_count):
            row = random.randint(0, self.row_n - 1)
            col = random.randint(0, self.col_n - 1)
            while self.get_grid(row, col).is_mine():
                row = random.randint(0, self.row_n - 1)
                col = random.randint(0, self.col_n - 1)

            self.get_grid(row, col).set_mine(True)
            bomb_positions.append((row, col))
        return bomb_positions

    def new_game(self, mine_count: int):
        self.refresh_grid()
        self.generate_mine(mine_count)
