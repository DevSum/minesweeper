from component.button import Button


class Grid(Button):
    width = height = 20

    def __init__(self, left: int, top: int):
        super().__init__(left, top, self.width, self.height)
