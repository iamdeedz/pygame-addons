from .errors import InvalidFont
import pygame as p


class Button:

    def __init__(self, size, pos, colour, text="", text_colour=p.Color("white"), font="arial", font_size=30):
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]
        self.colour = colour
        self.has_text = True if text else False

        if self.has_text:
            self.text = text
            self.text_colour = text_colour
            self.font = font.lower()
            self.font_size = font_size
            if self.font not in p.font.get_fonts():
                raise InvalidFont(self.font)

    def draw(self, screen):
        p.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        if self.has_text:
            font = p.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, True, self.text_colour)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def on_click(self):
        pass
