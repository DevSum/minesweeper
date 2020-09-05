from minesweeper_game.board import Board


class Game:
    def __init__(self, game_custom: list):
        self.row_n: int = game_custom[0]
        self.col_n: int = game_custom[1]
        self.mine_count: int = game_custom[2]
        self.gaming = False
        self.opened_grid = [[False for _ in range(self.col_n)] for _ in range(self.row_n)]
        self.board = Board(self.row_n, self.col_n)

    def new_game(self):
        self.board.refresh_grid()
        self.board.generate_mine(self.mine_count)
        self.opened_grid = [[False for _ in range(self.col_n)] for _ in range(self.row_n)]
        self.gaming = True

    def game_over(self):
        self.gaming = False

    def open(self, row: int, col: int):
        if not self.gaming:
            return False

        if self.opened_grid[row][col]:
            return False

        self.opened_grid[row][col] = True

        if self.board.get_grid(row, col).is_mine():
            self.game_over()
            return True

        mine_neighbor = self.get_neighbor(row, col)
        self.board.get_grid(row, col).set_number(mine_neighbor)
        if mine_neighbor == 0:
            self.open_neighbor(row, col)

    def get_neighbor(self, row, col):
        mine_count: int = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i < 0 or row + i >= self.row_n or col + j < 0 or col + j >= self.col_n:
                    continue
                if self.board.get_grid(row+i, col+j).is_mine():
                    mine_count += 1
        return mine_count

    def open_neighbor(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i < 0 or row + i >= self.row_n or col + j < 0 or col + j >= self.col_n:
                    continue
                if not self.opened_grid[row+i][col+j]:
                    self.open(row+i, col+j)
