import pygame
from enum import Enum


class EventType(Enum):
    CLICK_WINDOWS = 0,
    EXIT = 1,
    FLIP = 2,
    CLICK_COMPONENT = 3,
    RIGHT_CLICK_COMPONENT = 4,


class Event:
    def __init__(self, event: EventType, message: str, args=None):
        if args is None:
            args = []
        self.type = event
        self.message = message
        self.args = args

    def msg(self):
        return self.message
