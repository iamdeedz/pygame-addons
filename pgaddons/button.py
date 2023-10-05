from .errors import *
from .base_class import BaseClass

try:
    import pygame as pg

except ImportError:
    raise PygameNotInstalled()


class Button(BaseClass):

    def __init__(self, pos, size, colour, text="", text_colour=pg.Color("white"), font="arial", font_size=30):
        super().__init__(pos, size, colour)
        self.has_text = True if text else False

        if self.has_text:
            self.text = text
            self.text_colour = text_colour
            self.font = font.lower()
            self.font_size = font_size
            if self.font.removesuffix(".ttf") not in pg.font.get_fonts() and not self.font == "freesansbold":
                raise InvalidFont(self.font)

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        if self.has_text:
            font = pg.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, True, self.text_colour)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def on_click(self):
        pass
