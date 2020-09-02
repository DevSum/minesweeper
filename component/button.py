from .component import Component


class Button(Component):
    def __init__(self, left: int, top: int, width: int, height: int):
        super().__init__(left, top, width, height)
