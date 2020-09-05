from component.grid import GridComponent
from component.button import Button
from minesweeper_game.game import Game


def print_msg(i, j):
    return lambda: print(i, j)


class MineSweeperWindows:
    def __init__(self, game: Game):
        self.components = []
        self.game = game

        for i in range(game.row_n):
            for j in range(game.col_n):
                self.components.append(GridComponent(i * 21, j * 21, game.board.get_grid(i, j), click_callback=self.open_grid(i, j)))
        # self.components.append(Button(600, 600))

    def open_grid(self, row, col):
        return lambda: self.game.open(row, col)

    def flatten_components(self):
        return self.components
