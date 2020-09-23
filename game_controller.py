import sys

from event import Event, EventType
from game_windows import GameWindows
from minesweeper_game.game import Game
from mine_sweeper_windows import MineSweeperWindows
from variables import Custom


class GameController:
    def __init__(self):
        row_n: int = Custom.GRID_ROW
        col_n: int = Custom.GRID_COL
        mine_count: int = Custom.BOMB_COUNT
        self.game_custom = [row_n, col_n, mine_count]

        self.game_windows = GameWindows()
        self.game = Game(self.game_custom)
        self.game.new_game()

        self.mine_sweeper_windows = MineSweeperWindows(self.game)
        self.game_windows.set_component(self.mine_sweeper_windows.flatten_components())

    def deal_event(self, event: Event):
        if event.type == EventType.CLICK_WINDOWS:
            print(event.msg())
        elif event.type == EventType.EXIT:
            sys.exit()
        elif event.type == EventType.FLIP:
            pass
        elif event.type == EventType.CLICK_COMPONENT:
            event.args.click()
        elif event.type == EventType.RIGHT_CLICK_COMPONENT:
            event.args.right_click()

    def start(self):
        while True:
            for event in self.game_windows.tic():
                self.deal_event(event)


game = GameController()
game.start()
