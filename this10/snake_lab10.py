import pygame as pg
import random
from random import choice
import psycopg2
from config import data

conn = psycopg2.connect(**data)
conn.autocommit = True
cursor = conn.cursor()

name = input('Введите имя игрока: ')

query = f"""
select * from snake
where name='{name}'
"""

cursor.execute(query)
user = cursor.fetchone()

if (user == None):
    print('Такого игрока нет, желаете создать нового? y\\N')
    answer = input()
    if answer == 'y':
        query = f"""
        insert into snake
        values ('{name}', 0)
        """
        user = (name, 0)
        cursor.execute(query)
    else:
        print('Тогда я не смогу вас пропустить')
        exit()

pg.init()
bg = pg.image.load('bg.jpg')
bg = pg.transform.scale(bg, (800, 600))


class Snake(pg.sprite.Sprite):
    head = (100, 0)
    body = [(50, 0), (0, 0)]

    def __init__(self):
        super().__init__()
        self.logo = pg.image.load('logo.PNG')
        self.logo = pg.transform.scale(self.logo, (49, 49))

    def update(self, dx, dy):
        self.body.insert(0, self.head)
        self.body.pop()
        self.head = list(self.head)
        self.head[0] += dx * 50
        self.head[1] += dy * 50
        self.head = tuple(self.head)

    def draw(self, screen):
        for i in self.body:
            screen.blit(self.logo, (*i, 49, 49))
        pg.draw.rect(screen, 'red', (*self.head, 49, 49))

    def has_colise(self, apple, dx, dy):
        head_rect = pg.Rect(*self.head, 49, 49)
        if head_rect.collideobjects([apple]):
            apple.color = choice(['red', 'green', 'blue'])
            self.body.append((self.body[-1][0] - 5000 * dx, self.body[-1][1] - 5000 * dy))
            return True
        return False

    def isDead(self):
        if self.head in self.body:
            return True
        if self.head[0] > 799 or self.head[0] < 0 or self.head[1] > 599 or self.head[1] < 0:
            return True
        return False


class Apple(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.colors = ['red', 'blue', 'green']
        self.color = choice(self.colors)
        self.image = pg.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.PlaceApple()

    def PlaceApple(self):
        x, y = random.randrange(0, 750, 50), random.randrange(0, 550, 50)
        self.rect.x = x
        self.rect.y = y
        if (self.color == 'green'):
            return 3
        elif self.color == 'blue':
            return 2
        elif self.color == 'red':
            return 1

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)


font = pg.font.Font(None, 30)
screen = pg.display.set_mode((800, 600))

best_score = font.render(f'Ваш лучший результат за пользователя {user[0]} - {user[1]}', 1, 'black', 'green')

snake = Snake()
apple = Apple()
our_keyses = {'W': True, 'S': True, 'D': True, 'A': False}
cnt = 0
clock = pg.time.Clock()
dx = 1
dy = 0
speed_count = 1
speed = 10

apple_ = Apple()
is_exist = False
timer_count = 0
timer = 60
limit = 15
while 1:
    if cnt >= limit and not is_exist and cnt != 0:
        limit += 15
        is_exist = True

    if snake.isDead():
        query = f"""
        UPDATE snake
        SET score={cnt}
        where name='{name}'
        """
        cursor.execute(query)
        exit()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    if snake.has_colise(apple, dx, dy):
        cnt += random.randint(1, 3)
        while (tuple(apple.rect)[:2] in snake.body) or (tuple(apple.rect)[:2] == snake.head):
            apple.PlaceApple()
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and our_keyses['W']:
        dx = 0
        dy = -1
        our_keyses = {'W': True, 'S': False, 'D': True, 'A': True}
    if keys[pg.K_s] and our_keyses['S']:
        dx = 0
        dy = 1
        our_keyses = {'W': False, 'S': True, 'D': True, 'A': True}
    if keys[pg.K_a] and our_keyses['A']:
        dx = -1
        dy = 0
        our_keyses = {'W': True, 'S': True, 'D': False, 'A': True}
    if keys[pg.K_d] and our_keyses['D']:
        dx = 1
        dy = 0
        our_keyses = {'W': True, 'S': True, 'D': True, 'A': False}
    screen.blit(bg, (0, 0))
    speed_count += 1
    text = font.render(f'У тебя {cnt} очков', 1, 'white', pg.color.Color(65, 250, 99))
    if speed_count % speed == 0:
        snake.update(dx, dy)
    if is_exist:
        if snake.has_colise(apple_, dx, dy):
            timer_count = 0
            cnt += 6
            is_exist = False
        apple_.draw(screen)
        timer_count += 1
    if timer == timer_count:
        timer_count = 0
        apple_.PlaceApple()
        is_exist = False

    snake.draw(screen)
    apple.draw(screen)
    screen.blit(text, (0, 0))
    screen.blit(best_score, (0, 50))
    pg.display.flip()
    clock.tick(60)

cursor.close()
conn.close()