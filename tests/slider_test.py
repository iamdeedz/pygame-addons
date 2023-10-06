from pgaddons import Slider
import pygame as p


p.init()
screen = p.display.set_mode((500, 500))
clock = p.time.Clock()
slider = Slider((0, 0), (300, 50), p.Color("red"), 0, 100, 50)

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill((0, 0, 0))
    slider.draw(screen)
    p.display.update()
    clock.tick(60)
