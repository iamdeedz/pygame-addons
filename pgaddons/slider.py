from .base_class import BaseClass
import pygame as pg


class Slider(BaseClass):

    def __init__(self, pos, size, colour, min_value, max_value, value):
        super().__init__(pos, size, colour)
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
