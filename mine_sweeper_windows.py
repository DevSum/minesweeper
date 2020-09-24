import pygame

from component.grid import GridComponent
from component.button import Button
from component.number_box import NumberBox
from minesweeper_game.game import Game
from timer import Timer
from variables import Constant


def print_msg(i, j):
    return lambda: print(i, j)


class MineSweeperWindows:
    def __init__(self, game: Game):
        self.components = []
        self.game = game

        for i in range(game.row_n):
            for j in range(game.col_n):
                self.components.append(GridComponent(
                    i * Constant.GRID_SIDE_LENGTH,
                    j * Constant.GRID_SIDE_LENGTH,
                    game.board.get_grid(i, j),
                    click_callback=self.open_grid_func(i, j),
                    right_callback=self.mark_grid_func(i, j)
                ))
        self.components.append(Button(
            Constant.NEW_GAME_POSITION[0],
            Constant.NEW_GAME_POSITION[1],
            Constant.BUTTON_WIDTH,
            Constant.BUTTON_HEIGHT,
            click_callback=self.new_game
        ))
        self.components.append(NumberBox(
            Constant.BOMB_COUNT_POSITION[0],
            Constant.BOMB_COUNT_POSITION[1],
            Constant.NUMBER_BOX_WIDTH,
            Constant.NUMBER_BOX_HEIGHT,
            number=lambda: self.game.bomb_number()
        ))

        self.components.append(NumberBox(
            Constant.TIMER_POSITION[0],
            Constant.TIMER_POSITION[1],
            Constant.NUMBER_BOX_WIDTH,
            Constant.NUMBER_BOX_HEIGHT,
            number=lambda: self.game.timer.time()
        ))

    def open_grid_func(self, row, col):
        return lambda: self.game.open(row, col)

    def mark_grid_func(self, row, col):
        return lambda: self.game.mark(row, col)

    def flatten_components(self):
        return self.components

    def new_game(self):
        self.game.new_game()
