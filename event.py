import pygame
from enum import Enum


class EventType(Enum):
    CLICK_WINDOWS = 0,
    EXIT = 1,
    FLIP = 2,


class Event:
    def __init__(self, event: EventType, message: str):
        self.type = event
        self.message = message

    def msg(self):
        return self.message
