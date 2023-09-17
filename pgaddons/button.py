from .errors import InvalidFont
from .base_class import BaseClass
import pygame as pg


class Button(BaseClass):

    def __init__(self, size, pos, colour, text="", text_colour=pg.Color("white"), font="arial", font_size=30):
        super().__init__(pos, size, colour)
        self.has_text = True if text else False

        if self.has_text:
            self.text = text
            self.text_colour = text_colour
            self.font = font.lower()
            self.font_size = font_size
            if self.font not in pg.font.get_fonts():
                raise InvalidFont(self.font)

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        if self.has_text:
            font = pg.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, True, self.text_colour)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def on_click(self):
        pass
