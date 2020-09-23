import pygame

from variables import Resource
from .component import Component


class Button(Component):
    def __init__(self, left: int, top: int, width: int, height: int, click_callback=None):
        super().__init__(left, top, width, height)
        self.click = click_callback

    def click(self, *args):
        if self.click:
            return self.click(args)

    def draw(self, screen: pygame.Surface):
        white = pygame.image.load(Resource.BUTTON_RESTART)
        white = pygame.transform.smoothscale(white, (self.width, self.height))
        self.face = white
        screen.blit(self.face, (self.left, self.top))
