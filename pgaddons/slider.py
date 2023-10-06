from .base_class import BaseClass
from .errors import *
from math import ceil

try:
    import pygame as pg

except ImportError:
    raise PygameNotInstalled()


class Slider(BaseClass):

    def __init__(self, pos, size, colour, min_value, max_value, value,
                 font: str | type[pg.font.Font] | type[pg.font.SysFont] = "freesansbold", font_size=30):

        super().__init__(pos, size, colour)
        self.min_value = min_value
        self.max_value = max_value
        self.value = value

        if isinstance(font, str):
            self.font = font.lower()
            if self.font.removesuffix(".ttf") not in pg.font.get_fonts() and not self.font == "freesansbold":
                raise InvalidFont(self.font)

        else:
            self.font = font

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height), 2, ceil(self.height / 2))


# draw method:
# draw rectangle with rounded corners
# draw circle at the current value's position
# fill in the area before the circle
