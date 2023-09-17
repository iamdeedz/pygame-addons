from .base_class import BaseClass
from .errors import InvalidFont
import pygame as pg


class InputField(BaseClass):
    def __init__(self, pos, size, colour, active_colour, background_text="", text_colour=pg.Color("white"), font="arial", font_size=30):
        super().__init__(pos, size, colour)
        self.active_colour = active_colour
        self.text_colour = text_colour
        self.font = font.lower()
        self.font_size = font_size
        self.text = ""
        self.bg_text = background_text
        self.active = False
        self.locked = False
        if self.font not in pg.font.get_fonts():
            raise InvalidFont(self.font)

    def draw(self, screen):
        pg.draw.rect(screen, self.colour if not self.active else self.active_colour, (self.x, self.y, self.width, self.height))
        font = pg.font.SysFont(self.font, self.font_size, italic=True if not self.text else False)
        text = font.render(self.text, True, self.text_colour) if self.text else font.render(self.bg_text, True, self.text_colour)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def on_key_press(self, key):
        if self.active:
            if key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += pg.key.name(key)
