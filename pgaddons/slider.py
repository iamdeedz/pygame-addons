from .base_class import BaseClass
from .errors import PygameNotInstalled

try:
    import pygame as pg

except ImportError:
    raise PygameNotInstalled()


class Slider(BaseClass):

    def __init__(self, pos, size, colour, min_value, max_value, value):
        super().__init__(pos, size, colour)
        self.min_value = min_value
        self.max_value = max_value
        self.value = value

    def draw(self):
        pass
