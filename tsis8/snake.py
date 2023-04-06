import pygame as pg
import random
pg.init()

class Snake(pg.sprite.Sprite):
    head = (100, 0)
    body = [(50, 0),(0, 0)]


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
        self.image = pg.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.PlaceApple()

    def PlaceApple(self):
        x, y = random.randrange(0, 750, 50), random.randrange(0, 550, 50)
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen):
        pg.draw.rect(screen, 'green', self.rect)
screen = pg.display.set_mode((800, 600))


snake = Snake()
apple = Apple()
our_keyses = {'W': True, 'S': True, 'D': True, 'A': False}

clock = pg.time.Clock()
dx = 1
dy = 0
speed_count = 1
speed = 10
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    if snake.has_colise(apple, dx, dy):
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
    screen.fill('black')
    speed_count += 1
    if speed_count % speed == 0:
        snake.update(dx, dy)
    snake.draw(screen)
    apple.draw(screen)
    pg.display.flip()
    if snake.isDead():
        exit()
    clock.tick(60)
