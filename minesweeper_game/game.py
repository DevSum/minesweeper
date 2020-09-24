import pygame

from minesweeper_game.board import Board
from minesweeper_game.grid import GridState
from timer import Timer
from variables import Constant


class Game:
    def __init__(self, game_custom: list):
        self.row_n: int = game_custom[0]
        self.col_n: int = game_custom[1]
        self.mine_count: int = game_custom[2]
        self.gaming = False
        self.opened_grid = [[False for _ in range(self.col_n)] for _ in range(self.row_n)]
        self.board = Board(self.row_n, self.col_n)
        self.bomb_list = []

        self.opened_grid_count = 0
        self.flag_count = 0
        self.timer = Timer()

    def bomb_number(self):
        return self.mine_count - self.flag_count

    def new_game(self):
        self.board.refresh_grid()
        self.bomb_list = self.board.generate_mine(self.mine_count)
        self.opened_grid = [[False for _ in range(self.col_n)] for _ in range(self.row_n)]
        self.gaming = True
        self.opened_grid_count = 0
        self.flag_count = 0
        self.timer.reset()

    def game_over(self):
        self.gaming = False
        self.timer.stop()
        for bomb in self.bomb_list:
            self.board.get_grid(bomb[0], bomb[1]).setState(GridState.BOMB)

    def open(self, row: int, col: int):
        if not self.gaming:
            return False

        if self.opened_grid[row][col]:
            return False

        if self.board.get_grid(row, col).getState() == GridState.FLAG:
            return False

        if not self.timer.running:
            self.timer.start()
            pygame.time.set_timer(Constant.SECOND_EVENT, 1000)
        self.opened_grid[row][col] = True
        self.opened_grid_count += 1

        if self.board.get_grid(row, col).is_mine():
            self.game_over()
            return True

        if self.opened_grid_count == self.row_n * self.col_n - self.mine_count:
            self.win()

        mine_neighbor = self.get_neighbor(row, col)
        if mine_neighbor == 0:
            self.open_neighbor(row, col)
            self.board.get_grid(row, col).setState(GridState.ZERO)
        else:
            self.board.get_grid(row, col).setState(GridState.NUMBER)
            self.board.get_grid(row, col).set_number(mine_neighbor)

    def win(self):
        self.timer.stop()
        self.gaming = False

    def mark(self, row: int, col: int):
        if not self.gaming:
            return False

        if self.opened_grid[row][col]:
            return False

        grid = self.board.get_grid(row, col)
        if grid.getState() == GridState.FLAG:
            grid.setState(GridState.CLOSED)
            self.flag_count -= 1
        elif grid.getState() == GridState.CLOSED:
            grid.setState(GridState.FLAG)
            self.flag_count += 1

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
