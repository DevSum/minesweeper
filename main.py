import sys

from event import Event, EventType
from game_windows import GameWindows
from game import Game
from mine_sweeper_windows import MineSweeperWindows


class Main:
    def __init__(self):
        row_n: int = 20
        col_n: int = 20
        mine_count: int = 10
        self.game_custom = [row_n, col_n, mine_count]

        self.game_windows = GameWindows()
        self.game = Game(self.game_custom)
        self.mine_sweeper_windows = MineSweeperWindows(self.game_custom)
        self.game_windows.set_component(self.mine_sweeper_windows.flatten_components())

        self.game.new_game()

    def deal_event(self, event: Event):
        if event.type == EventType.CLICK_WINDOWS:
            print(event.msg())
        elif event.type == EventType.EXIT:
            sys.exit()
        elif event.type == EventType.FLIP:
            pass

    def start(self):
        while True:
            for event in self.game_windows.tic():
                self.deal_event(event)


game = Main()
game.start()
