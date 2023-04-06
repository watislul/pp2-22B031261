rom cmath import rect
from turtle import circle
import pygame as pg
pg.init()

screen = pg.display.set_mode((1000, 800))
menu = pg.image.load('menu_bar.png')
menu = pg.transform.scale(menu, (100, 800))

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pg.image.load('assets/' + path)
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_selected = False

    def make_selected(self, path ,group):
        if not self.is_selected:
            self.prev_image = self.image.copy()
            self.image = pg.image.load('assets/' + path)
            self.image = pg.transform.scale(self.image, (40, 40))
            self.is_selected = True
        else:
            self.image = self.prev_image
            self.is_selected = False
        for i in group.sprites():
            if i == self:
                continue
            i.make_default(group)
    def make_default(self, group):
        try: 
            self.image = self.prev_image
            self.is_selected = False
        except:
            pass
def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            print(x, y)
            pg.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pg.draw.circle(screen, color, (x, y), width)

def draw_rectangle(screen, start, end, width, color):
    pg.draw.rect(screen, color, (start, end), width)

brush = Button(5, 5, 'brush.png')
draw_rect = Button(55, 5, 'rect.png')
draw_circle = Button(5, 55, 'circle.png')

all_buttons = pg.sprite.Group()
all_buttons.add(brush, draw_rect)
all_buttons.add(draw_circle)

last_pos = (0, 0)
end_pos = (0, 0)
is_drawing = False
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN: 
            if brush.rect.collidepoint(event.pos):
                brush.make_selected('brush_selected.png', all_buttons)
            if draw_rect.rect.collidepoint(event.pos):
                draw_rect.make_selected('rect_selected.png', all_buttons)
            if draw_circle.rect.collidepoint(event.pos):
                draw_circle.make_selected('circle_selected.png', all_buttons)
            last_pos = event.pos
            is_drawing = True

        if event.type == pg.MOUSEBUTTONUP:
            is_drawing = False
            end_pos = event.pos

        if brush.is_selected:
            if is_drawing and event.type == pg.MOUSEMOTION:
                drawLine(screen, last_pos, event.pos, 5, 'white')
                print(event.pos)
                last_pos = event.pos
        elif draw_rect.is_selected:
            if event.type == pg.MOUSEBUTTONUP:
                draw_rectangle(screen, last_pos, end_pos, 5, 'white')
    screen.blit(menu, (0, 0))
    all_buttons.update()
    all_buttons.draw(screen)
    pg.display.flip()
