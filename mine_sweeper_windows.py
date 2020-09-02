from component.grid import Grid


class MineSweeperWindows:
    def __init__(self, game_custom: list):
        self.components = []

        for i in range(game_custom[0]):
            for j in range(game_custom[1]):
                self.components.append({'component': Grid(i*21, j*21), 'position': (i*21, j*21)})

    def flatten_components(self):
        return self.components
