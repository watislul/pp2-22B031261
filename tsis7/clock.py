import pygame as pg
import datetime

pg.init()

screen = pg.display.set_mode((1400,1050))
bg = pg.image.load('assets_for_clock/bg.png')
screen.fill((0, 0, 156))
screen.blit(bg, (0, 0))

minutes = pg.image.load('assets_for_clock/minutes.png')
orig_minutes = minutes
rect_minutes = minutes.get_rect()

seconds = pg.image.load('assets_for_clock/seconds.png')
orig_seconds = seconds
rect_seconds = seconds.get_rect()

def rotate(hand, rect, angle):
    new_hand = pg.transform.rotate(hand, angle)
    rect = new_hand.get_rect(center=rect.center)
    return new_hand, rect

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    a = datetime.datetime.now()
    b = a.microsecond + a.second * (10 ** 6)
    c = a.minute
    minutes, rect_minutes = rotate(orig_minutes, rect_minutes, -(c * 6))
    seconds, rect_seconds = rotate(orig_seconds, rect_seconds, -(b * 0.000006))

    screen.blit(bg, (0, 0))
    screen.blit(minutes, rect_minutes)
    screen.blit(seconds, rect_seconds)
    pg.display.flip()
