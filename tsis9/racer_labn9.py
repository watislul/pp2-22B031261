from random import randint, randrange
import pygame as pg
import sys
pg.init()

screen = pg.display.set_mode((400, 600))
bg = pg.image.load('assets_for_racer/bg.png')
bg_x = 0
bg_y = 0

STEP_ENEMY = 10
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets_for_racer/Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500

    def update(self, x=0):
        if 0 > self.rect.x :
            x = 0
            self.rect.x = 1
        if self.rect.x > 351:
            x = 0
            self.rect.x = 350
        self.rect.move_ip(x, 0)


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets_for_racer/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 360)
        self.rect.y = -100

    def update(self):
        if self.rect.y > 700:
            self.rect.y = -100
            self.rect.x = randint(0, 360)
        self.rect.move_ip(0, STEP_ENEMY)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets_for_racer/coin.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 360)
        self.rect.y = -100

    def update(self):
        if self.rect.y > 650:
            self.new_coordinates()
        self.rect.move_ip(0, 10)

    def new_coordinates(self):
        self.rect.y = -100
        self.rect.x = randint(0, 350)
        return randint(1, 3)

font = pg.font.Font(None, 50)
cnt = 0

player = Player()
enemy = Enemy()
coin = Coin()
sprites = pg.sprite.Group()
sprites.add(player)
sprites.add(enemy)
sprites.add(coin)

clock = pg.time.Clock()
while 1:
    bg_y %= 600

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    keys = pg.key.get_pressed()


    if keys[pg.K_d]:
        player.update(5)
    elif keys[pg.K_a]:
        player.update(-5)

    if enemy.rect.collideobjects([player]):
        pg.quit()

    if coin.rect.collideobjects([player]):
        cnt += coin.new_coordinates()
        if(cnt >= 10):
            STEP_ENEMY = 20
    screen.blit(bg, (0, -600 + bg_y))
    screen.blit(bg, (0, bg_y))
    bg_y += 5
    screen.blit(font.render(f'Вы набрали {cnt} монет', 1 ,'black'), (0, 0))
    sprites.update()
    sprites.draw(screen)

    pg.display.flip()


    clock.tick(60)