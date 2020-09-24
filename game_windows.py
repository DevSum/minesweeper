import pygame
import sys
from event import Event, EventType
from component.component import Component
from variables import Constant, Resource


class GameWindows:
    def __init__(self):
        self.bg = Constant.BG_COLOR
        self.screen: pygame.Surface | None = None
        self.size = Constant.WINDOW_SIZE
        self.components = []

        self.windows_init()

    def windows_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(Constant.TITLE)
        pygame.display.set_icon(pygame.image.load(Resource.WINDOWS_ICON))

    def show_component(self, screen: pygame.Surface):
        for component in self.components:
            component.draw(screen)

    def analyze_click_event_on_component(self, event: pygame.event):
        click_position = event.pos
        MOUSE_LEFT = False
        MOUSE_RIGHT = False
        if pygame.mouse.get_pressed()[0]:
            MOUSE_LEFT = True
        if pygame.mouse.get_pressed()[2]:
            MOUSE_RIGHT = True

        for component in self.components:
            component_position = component.left, component.top
            if component.left <= click_position[0] and component.top <= click_position[1]:
                component_rect = component.get_rect()
                if component.left + component_rect[0] >= click_position[0] and \
                        component.top + component_rect[1] >= click_position[1]:
                    # TODO random component click event returned
                    if MOUSE_LEFT:
                        return Event(
                            EventType.CLICK_COMPONENT,
                            'click at component',
                            args=component
                        )
                    if MOUSE_RIGHT:
                        return Event(
                            EventType.RIGHT_CLICK_COMPONENT,
                            'right click at component',
                            args=component
                        )
        return Event(EventType.CLICK_WINDOWS, 'click at ' + str(click_position))

    def tic(self):
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                yield self.analyze_click_event_on_component(event)

            if event.type == pygame.QUIT:
                yield Event(EventType.EXIT, 'exit')

            if event.type == Constant.SECOND_EVENT:
                yield Event(EventType.TIMER_TIC)

        self.screen.fill(self.bg)
        self.show_component(self.screen)
        pygame.display.flip()
        yield Event(EventType.FLIP, 'screen refreshed')

    def push_component(self, component: Component):
        self.components.append(component)

    def clear_component(self):
        self.components = []

    def set_component(self, components: list):
        self.components = components
