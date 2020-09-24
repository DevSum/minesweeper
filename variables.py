class Style:
    COLOR_RED = (255, 0, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_WHITE = (255, 255, 255)

    GRID_SIDE_LENGTH = 30
    BG_COLOR = COLOR_WHITE
    WINDOW_SIZE = (920, 550)
    TITLE = "mine sweeper"
    BUTTON_WIDTH = 50
    BUTTON_HEIGHT = 40
    NEW_GAME_POSITION = 410, 500
    NUMBER_COLOR = COLOR_RED


class Resource:
    GRID_CLOSED = "resources/closed.png"
    GRID_OPENED = "resources/blank.png"
    FLAG = "resources/flag.png"
    BOMB = "resources/bomb.png"
    BUTTON_RESTART = "resources/closed.png"
    WINDOWS_ICON = "resources/icon.jpg"


class Custom:
    GRID_ROW = 30
    GRID_COL = 16
    BOMB_COUNT = 99
