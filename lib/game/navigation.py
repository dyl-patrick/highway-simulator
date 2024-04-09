from enum import Enum
from typing import Tuple

from pygame import (
    KEYDOWN,
    KEYUP,
    K_a,
    K_d,
    K_w,
    K_s,
    K_p,
    QUIT
)
from pygame import mouse
from pygame.event import Event


class Navigation(Enum):
    """Navigation keyboards for a game."""

    navigate_down: int = KEYDOWN
    navigate_up: int = KEYUP
    navigate_left: int = K_a
    navigate_right: int = K_d
    navigate_accelerate: int = K_w
    navigate_brake: int = K_s
    navigate_pause:int = K_p
    navigate_quit: int = QUIT

    @classmethod
    def is_down(cls, event: Event) -> bool:
        return event.type == cls.navigate_down.value

    @classmethod
    def is_up(cls, event: Event) -> bool:
        return event.type == cls.navigate_up.value

    @classmethod
    def is_left(cls, event: Event) -> bool:
        return event.key == cls.navigate_left.value

    @classmethod
    def is_right(cls, event: Event) -> bool:
        return event.key == cls.navigate_right.value

    @classmethod
    def is_accelerate(cls, event: Event) -> bool:
        return event.key == cls.navigate_accelerate.value

    @classmethod
    def is_brake(cls, event: Event) -> bool:
        return event.key == cls.navigate_brake.value
    
    @classmethod
    def is_pause(cls, event: Event) -> bool:
        return event.key == cls.navigate_pause.value

    @classmethod
    def is_quit(cls, event: Event) -> bool:
        return event.type == cls.navigate_quit.value

    @classmethod
    def get_mouse_position(cls) -> Tuple[int, int]:
        return mouse.get_pos()

    @classmethod
    def get_mouse_pressed(cls) -> Tuple[int, int, int]:
        return mouse.get_pressed()
