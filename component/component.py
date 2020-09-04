import pygame


class Component:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left: int = left
        self.top: int = top
        self.width: int = width
        self.height: int = height

        black = pygame.image.load("resources/black.png")
        black = pygame.transform.smoothscale(black, (width, height))
        self.face = black

    def draw(self, screen: pygame.Surface, position):
        screen.blit(self.face, position)

    def get_rect(self):
        return self.width, self.height
