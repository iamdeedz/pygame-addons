from pgessentials import Button
import time
import pygame as p

width = height = 500
p.init()
screen = p.display.set_mode((width, height))
button = Button((150, 75), (175, 212.5),  p.Color("grey 33"), text="Hello World", text_colour=p.Color("grey 66"), font="verdana", font_size=25)
clock = p.time.Clock()
x = 0


def on_click():
    global x
    x += 1


button.on_click = on_click

running = True
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        elif event.type == p.MOUSEBUTTONDOWN:
            if button.x < p.mouse.get_pos()[0] < button.x + button.width and button.y < p.mouse.get_pos()[1] < button.y + button.height:
                button.on_click()

    screen.fill(p.Color("white"))

    text = p.font.SysFont("verdana", 25).render(f"The button was clicked {x} times.", True, p.Color("grey 33"))
    text_rect = text.get_rect()
    text_rect.center = (width / 2, 133)
    screen.blit(text, text_rect)

    clock.tick(60)
    button.draw(screen)
    p.display.update()
