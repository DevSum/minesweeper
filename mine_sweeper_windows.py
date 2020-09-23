from component.grid import GridComponent
from component.button import Button
from minesweeper_game.game import Game
from variables import Style


def print_msg(i, j):
    return lambda: print(i, j)


class MineSweeperWindows:
    def __init__(self, game: Game):
        self.components = []
        self.game = game

        for i in range(game.row_n):
            for j in range(game.col_n):
                self.components.append(GridComponent(
                    i * Style.GRID_SIDE_LENGTH,
                    j * Style.GRID_SIDE_LENGTH,
                    game.board.get_grid(i, j),
                    click_callback=self.open_grid_func(i, j),
                    right_callback=self.mark_grid_func(i, j)
                ))
        self.components.append(Button(
            Style.NEW_GAME_POSITION[0],
            Style.NEW_GAME_POSITION[1],
            Style.BUTTON_WIDTH,
            Style.BUTTON_HEIGHT,
            click_callback=self.new_game
        ))

    def open_grid_func(self, row, col):
        return lambda: self.game.open(row, col)

    def mark_grid_func(self, row, col):
        return lambda: self.game.mark(row, col)

    def flatten_components(self):
        return self.components

    def new_game(self):
        self.game.new_game()
