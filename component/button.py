from .component import Component


class Button(Component):
    def __init__(self, left: int, top: int, width: int, height: int, click_callback=None):
        super().__init__(left, top, width, height)
        self.click = click_callback

    def click(self, *args):
        if self.click:
            return self.click(args)
