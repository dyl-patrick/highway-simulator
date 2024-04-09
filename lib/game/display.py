from typing import Type, Union, Tuple
from pygame import display, time, Surface, Rect
from lib.game.properties import Display


class GameSurface:
    """A surface for a game."""

    def __init__(self, surface: Surface) -> None:
        self._surface = surface

    @property
    def surface(self) -> Surface:
        return self._surface

    def blit(self, source: Union[str, Surface], dest: Union[Tuple[int, int], Rect]) -> Rect:
        return self._surface.blit(
            source,
            dest
        )

    def fill(self, color: Tuple[int, int, int]) -> Rect:
        return self._surface.fill(color)


class GameDisplay:
    """Display of a game."""

    def __init__(self, option: Type[Display]) -> None:
        self._option = option
        self._display = display

    def set_title(self) -> None:
        self._display.set_caption(self._option.caption.value)

    def set_size(self) -> Surface:
        return self._display.set_mode(
            (
                self._option.width.value,
                self._option.height.value
            )
        )


class Clock:
    """Game time clock."""

    def __init__(self) -> None:
        self._clock: time.Clock = time.Clock()

    def tick(self, seconds: int) -> int:
        return self._clock.tick(seconds)
