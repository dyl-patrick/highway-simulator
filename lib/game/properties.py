import os
from enum import Enum
from typing import Iterable

_images: str = os.path.join('lib/images/')


class Colors(Enum):
    """Represent set of colors for a game"""

    gray: Iterable[int] = (
        119,
        118,
        110
    )
    black: Iterable[int] = (
        0,
        0,
        0
    )
    red: Iterable[int] = (
        244,
        67,
        54,
        96
    )
    green: Iterable[int] = (
        83,
        194,
        87,
        76
    )
    blue: Iterable[int] = (
        33,
        150,
        243,
        95
    )
    button_gray: Iterable[int] = (
        173,
        173,
        173,
        68
    )
    dark_red: Iterable[int] = (
        211,
        47,
        47,
        83
    )
    dark_green: Iterable[int] = (
        56,
        142,
        60,
        56
    )
    dark_blue: Iterable[int] = (
        25,
        118,
        210,
        82
    )
    dark_gray: Iterable[int] = (
        128,
        128,
        128,
        50
    )


class Display(Enum):
    """Represent display properties."""

    width: int = 800
    height: int = 600
    caption: str = 'Racing Game'


class Images(Enum):
    """Represent game images."""

    car: str = f'{_images}car.jpg'
    car_one: str = f'{_images}car1.jpg'
    car_two: str = f'{_images}car2.jpg'
    car_three: str = f'{_images}car3.jpg'
    car_four: str = f'{_images}car4.jpg'
    car_five: str = f'{_images}car5.jpg'
    car_six: str = f'{_images}car6.jpg'
    grass: str = f'{_images}grass.jpg'
    white_strip: str = f'{_images}white_strip.png'
    strip: str = f'{_images}strip.jpg'
    back: str = f'{_images}back.jpg'
    back_alternative: str = f'{_images}back_alternative.jpg'


class Car(Enum):
    """Represents single car element."""

    height: int = 124
    width: int = 56
