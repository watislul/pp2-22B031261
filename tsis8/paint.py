import pygame as pg
pg.init()
# Дал размер экрану
screen = pg.display.set_mode((1000, 800))
# Заполнил экран белым
screen.fill('white')
# Загрузил картинку своей менюшки
menu = pg.image.load('menu_bar.png')
# Поменял размер этой картинки
menu = pg.transform.scale(menu, (100, 800))

# Class Button - нужен для того, чтобы мы создавали кнопки на экране и могли их выбрать
class Button(pg.sprite.Sprite):
    # Инициализурую класс, принимаю координаты где будет отрисована кнопка и путь к её картинке
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pg.image.load('assets/' + path)
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_selected = False

    # Нужен для того чтобы менять картинку на картинку выбранной кнопки и менять поле is_selected на True
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
    # Метод который делает стандартную картинку для всех кнопок кроме выбранной
    def make_default(self, group):
        try:
            self.image = self.prev_image
            self.is_selected = False
        except:
            pass

# Нужна для того чтобы реализовать рисование кистью
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
            pg.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pg.draw.circle(screen, color, (x, y), width)


# Нужна для того чтобы нарисовать прямоугольник
def drawRectangle(surface, color, x, y, x1, y1, size):
    if x > x1:
        x, x1 = x1, x
    if y > y1:
        y, y1 = y1, y

    pg.draw.rect(surface, color, [x, y, abs(x1 - x), abs(y - y1)], size)

# Нужна для того чтобы нарисовать эллипсоиду
def drawCircle(surface, color, x, y, x1, y1, size):
    if x > x1:
        x, x1 = x1, x
    if y > y1:
        y, y1 = y1, y

    pg.draw.ellipse(surface, color, [x, y, abs(x1 - x), abs(y - y1)], size)

# Создаю кнопки инструментов
brush = Button(5, 5, 'brush.png')
draw_rect = Button(55, 5, 'rect.png')
draw_circle = Button(5, 55, 'circle.png')
eraser = Button(55, 55, 'eraser.png')
# Создаю кнопки цветов
red_color = Button(5, 105, 'red.png')
black_color = Button(55, 105, 'black.png')
blue_color = Button(5, 155, 'blue.png')
green_color = Button(55, 155, 'green.png')
# Создал группу кнопок, которая отвечает за инструменты
all_buttons = pg.sprite.Group()
all_buttons.add(brush, draw_rect)
all_buttons.add(draw_circle)
all_buttons.add(eraser)

# Создаю группу спрайтов, которая отвечает за кнопки цветов
colors = pg.sprite.Group()
colors.add(red_color)
colors.add(black_color)
colors.add(blue_color)
colors.add(green_color)

# Нужно чтобы по началу цвет был черным
black_color.make_selected('black_selected.png', colors)
color = 'black'

# Нужно для того чтобы по началу была выбрана кисть
brush.make_selected('brush_selected.png', all_buttons)

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
            if eraser.rect.collidepoint(event.pos):
                eraser.make_selected('eraser_selected.png', all_buttons)
            if red_color.rect.collidepoint(event.pos):
                red_color.make_selected('red_selected.png', colors)
                color = 'red'
            if black_color.rect.collidepoint(event.pos):
                black_color.make_selected('black_selected.png', colors)
                color = 'black'
            if blue_color.rect.collidepoint(event.pos):
                blue_color.make_selected('blue_selected.png', colors)
                color = 'blue'
            if green_color.rect.collidepoint(event.pos):
                green_color.make_selected('green_selected.png', colors)
                color = 'green'
            last_pos = event.pos
            is_drawing = True

        if event.type == pg.MOUSEBUTTONUP:
            is_drawing = False
            end_pos = event.pos

        if brush.is_selected:
            if is_drawing and event.type == pg.MOUSEMOTION:
                drawLine(screen, last_pos, event.pos, 5, color)
                last_pos = event.pos
        elif draw_rect.is_selected:
            if event.type == pg.MOUSEBUTTONUP:
                drawRectangle(screen, color, *last_pos, *end_pos, 5)
        elif draw_circle.is_selected:
            if event.type == pg.MOUSEBUTTONUP:
                drawCircle(screen, color, *last_pos, *end_pos, 5)
        elif eraser.is_selected:
            if is_drawing and event.type == pg.MOUSEMOTION:
                drawLine(screen, last_pos, event.pos, 20, 'white')
    screen.blit(menu, (0, 0))
    colors.update()
    all_buttons.update()
    all_buttons.draw(screen)
    colors.draw(screen)
    pg.display.flip()