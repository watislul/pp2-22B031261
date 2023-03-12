import pygame
pygame.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
x = y = 500
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 20
    if keys[pygame.K_a]:
        x -= 20
    if keys[pygame.K_s]:
        y += 20
    if keys[pygame.K_d]:
        x += 20
    if x > 1025:
        x = -25
    if x < -25:
        x = 1025
    if y > 1025:
        y = -25
    if y < -25:
        y = 1025
    screen.fill((255, 255, 255))
    pygame.draw.circle(surface=screen, color=(243, 11, 11), center=(x, y), radius=25)
    pygame.display.flip()