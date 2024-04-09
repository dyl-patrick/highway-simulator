from typing import Type
from pygame import image, Surface
from lib.game.properties import Images


class Image:
    """Unified image."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._image = image

    def load(self) -> Surface:
        return self._image.load(self._name)


class GameImages:
    """Set of images for a game."""

    def __init__(self, images: Type[Images]) -> None:
        self._car: Image = Image(images.car.value)
        self._car_one: Image = Image(images.car_one.value)
        self._car_two: Image = Image(images.car_two.value)
        self._car_three: Image = Image(images.car_three.value)
        self._car_four: Image = Image(images.car_four.value)
        self._car_five: Image = Image(images.car_five.value)
        self._car_six: Image = Image(images.car_six.value)
        self._grass: Image = Image(images.grass.value)
        self._white_strip: Image = Image(images.white_strip.value)
        self._strip: Image = Image(images.strip.value)
        self._back: Image = Image(images.back.value)
        self._back_alter: Image = Image(images.back_alternative.value)

    def car(self) -> Surface:
        return self._car.load()

    def car_one(self) -> Surface:
        return self._car_one.load()

    def car_two(self) -> Surface:
        return self._car_one.load()

    def car_three(self) -> Surface:
        return self._car_one.load()

    def car_four(self) -> Surface:
        return self._car_one.load()

    def car_five(self) -> Surface:
        return self._car_one.load()

    def car_six(self) -> Surface:
        return self._car_one.load()

    def grass(self) -> Surface:
        return self._grass.load()

    def white_strip(self) -> Surface:
        return self._white_strip.load()

    def strip(self) -> Surface:
        return self._strip.load()

    def back(self) -> Surface:
        return self._back.load()

    def back_alter(self) -> Surface:
        return self._back_alter.load()
