from typing import List
from pygame.event import get, Event


def events() -> List[Event]:
    """Returns a list of game events."""
    return get()
