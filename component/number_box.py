import pygame

from component.component import Component
from variables import Constant


class NumberBox(Component):
    def __init__(self, left: int, top: int, width: int, height: int, number: int or callable):
        super().__init__(left, top, width, height)
        self.number = number

    def draw(self, screen: pygame.Surface):
        font_face = pygame.font.SysFont('arial', Constant.GRID_SIDE_LENGTH)
        font_face.set_bold(True)
        screen.blit(font_face.render(
            str(self.number if type(self.number) == int else self.number()),
            True,
            Constant.NUMBER_COLOR,
            Constant.BG_COLOR),
            (self.left + Constant.GRID_SIDE_LENGTH // 4, self.top)
        )

    def setNumber(self, number: int or callable):
        if type(number) == int:
            self.number = number
        else:
            self.number = number()
