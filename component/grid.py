import pygame

from component.button import Button
from minesweeper_game.grid import GridState
from variables import Style, Resource


class GridComponent(Button):
    width = height = Style.GRID_SIDE_LENGTH

    def __init__(self, left: int, top: int, grid, click_callback=None, right_callback=None):
        super().__init__(left, top, self.width, self.height, click_callback=click_callback)
        self.grid = grid

        black = pygame.image.load(Resource.GRID_CLOSED)
        black = pygame.transform.smoothscale(black, (self.width, self.height))
        self.black_face = black
        white = pygame.image.load(Resource.GRID_OPENED)
        white = pygame.transform.smoothscale(white, (self.width, self.height))
        self.white_face = white
        flag = pygame.image.load(Resource.FLAG)
        flag = pygame.transform.smoothscale(flag, (self.width, self.height))
        self.flag_face = flag
        bomb = pygame.image.load(Resource.BOMB)
        bomb = pygame.transform.smoothscale(bomb, (self.width, self.height))
        self.bomb_face = bomb

        self.right_click = right_callback

    def draw(self, screen: pygame.Surface):
        state: GridState = self.grid.getState()
        if state == GridState.CLOSED:
            screen.blit(self.black_face, (self.left, self.top))
        elif state == GridState.ZERO:
            screen.blit(self.white_face, (self.left, self.top))
        elif state == GridState.NUMBER:
            font_face = pygame.font.SysFont('arial', Style.GRID_SIDE_LENGTH)
            font_face.set_bold(True)
            screen.blit(font_face.render(
                str(self.grid.get_number()),
                True,
                Style.NUMBER_COLOR,
                Style.BG_COLOR),
                (self.left+Style.GRID_SIDE_LENGTH//4, self.top)
            )
        elif state == GridState.BOMB:
            screen.blit(self.bomb_face, (self.left, self.top))
        elif state == GridState.FLAG:
            screen.blit(self.flag_face, (self.left, self.top))

    def right_click(self, *args):
        if self.click:
            return self.click(args)
