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
                Style.COLOR_RED,
                Style.BG_COLOR),
                (self.left+Style.GRID_SIDE_LENGTH//4, self.top)
            )
        elif state == GridState.BOMB:
            pygame.draw.circle(
                screen,
                Style.COLOR_RED,
                (self.left+Style.GRID_SIDE_LENGTH//2, self.top++Style.GRID_SIDE_LENGTH//2),
                Style.GRID_SIDE_LENGTH//2
            )
        elif state == GridState.FLAG:
            pygame.draw.circle(
                screen,
                Style.COLOR_BLUE,
                (self.left + Style.GRID_SIDE_LENGTH // 2, self.top + +Style.GRID_SIDE_LENGTH // 2),
                Style.GRID_SIDE_LENGTH // 2
            )

    def right_click(self, *args):
        if self.click:
            return self.click(args)
