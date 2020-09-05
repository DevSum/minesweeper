import pygame
import sys
from event import Event, EventType
from component.component import Component


class GameWindows:
    def __init__(self):
        self.bg = (0, 0, 0)
        self.screen: pygame.Surface | None = None
        self.size = 800, 600
        self.components = []

        self.windows_init()

    def windows_init(self):
        pygame.init()
        self.bg = (117, 214, 251)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("mine sweeper")
        pygame.display.set_icon(pygame.image.load("resources/icon.jpg"))

    def show_component(self, screen: pygame.Surface):
        for component in self.components:
            component.draw(screen)

    def analyze_click_event_on_component(self, click_position):
        for component in self.components:
            component_position = component.left, component.top
            if component.left <= click_position[0] and component.top <= click_position[1]:
                component_rect = component.get_rect()
                if component.left + component_rect[0] >= click_position[0] and \
                        component.top + component_rect[1] >= click_position[1]:
                    # TODO random component click event returned
                    return Event(
                        EventType.CLICK_COMPONENT,
                        'click at component',
                        args=component
                    )
        return Event(EventType.CLICK_WINDOWS, 'click at ' + str(click_position))

    def tic(self):
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                yield self.analyze_click_event_on_component(event.pos)

            if event.type == pygame.QUIT:
                yield Event(EventType.EXIT, 'exit')

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
