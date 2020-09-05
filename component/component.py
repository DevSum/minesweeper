import pygame


class Component:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left: int = left
        self.top: int = top
        self.width: int = width
        self.height: int = height

    def draw(self, screen: pygame.Surface):
        pass

    def get_rect(self):
        return self.width, self.height
