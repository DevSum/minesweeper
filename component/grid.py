import pygame

from component.button import Button
from minesweeper_game.grid import GridState


class GridComponent(Button):
    width = height = 20

    def __init__(self, left: int, top: int, grid, click_callback=None):
        super().__init__(left, top, self.width, self.height, click_callback=click_callback)
        self.grid = grid

        black = pygame.image.load("resources/black.png")
        black = pygame.transform.smoothscale(black, (self.width, self.height))
        self.black_face = black
        white = pygame.image.load("resources/white.png")
        white = pygame.transform.smoothscale(white, (self.width, self.height))
        self.white_face = white

    def draw(self, screen: pygame.Surface):
        state: GridState = self.grid.getState()
        if state == GridState.CLOSED:
            screen.blit(self.black_face, (self.left, self.top))
        elif state == GridState.ZERO:
            screen.blit(self.white_face, (self.left, self.top))
        elif state == GridState.NUMBER:
            font_face = pygame.font.SysFont('宋体', 20)
            screen.blit(font_face.render('1', True, (255, 0, 0), (0, 255, 255)), (self.left, self.top))



