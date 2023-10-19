from .errors import *
from .base_class import BaseClass

try:
    import pygame as pg

except ImportError:
    raise PygameNotInstalled()


class Button(BaseClass):

    def __init__(self, pos, size, colour, text="", font_colour: str | tuple[int, int, int] | pg.Color = pg.Color("white"),
                 font: str | type[pg.font.Font] | type[pg.font.SysFont] = "freesansbold", font_size=30):

        super().__init__(pos, size, colour)
        self.has_text = True if text else False

        if self.has_text:
            self.text = text
            self.font_colour = font_colour
            self.font_size = font_size
            if isinstance(font, str):
                self.font = font.lower()
                if self.font.removesuffix(".ttf") not in pg.font.get_fonts() and self.font != "freesansbold":
                    raise InvalidFont(self.font)

                else:
                    self.font = pg.font.SysFont(font, font_size)

            else:
                self.font = font

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        if self.has_text:
            text = self.font.render(self.text, True, self.font_colour)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def on_click(self):
        pass
