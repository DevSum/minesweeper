from component.grid import GridComponent

from minesweeper_game.game import Game


def print_msg(i, j):
    return lambda: print(i, j)


class MineSweeperWindows:
    def __init__(self, game: Game):
        self.components = []
        self.game = game

        for i in range(game.row_n):
            for j in range(game.col_n):
                self.components.append({
                    'component': GridComponent(i * 21, j * 21, game.board.get_grid(i, j), click_callback=self.open_grid(i, j)),
                    'position': (i*21, j*21),
                })

    def open_grid(self, row, col):
        return lambda: self.game.open(row, col)

    def flatten_components(self):
        return self.components
