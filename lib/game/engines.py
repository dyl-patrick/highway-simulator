import sys
from abc import ABC, abstractmethod
import pygame


class Engine(ABC):
    """Represent engines abstractions."""

    @staticmethod
    @abstractmethod
    def start() -> None:
        pass

    @staticmethod
    @abstractmethod
    def stop() -> None:
        pass


class GameEngine(Engine):
    """Engine for a game."""

    @staticmethod
    def start() -> None:
        pygame.init()

    @staticmethod
    def stop() -> None:
        pygame.quit()
        quit()
        sys.exit()
