import os
import pygame as pg

pg.init()

class SOUND:
    def __init__(self, path_to_sound, path_to_photo):
        self.sound = pg.mixer.Sound('music/' + path_to_sound)
        self.photo = pg.image.load('assets/sound_images/' + path_to_photo)
        self.is_playing = True

    def placePhoto(self, screen):
        self.photo = pg.transform.scale(self.photo, (300, 300))
        screen.blit(self.photo, (262, 168))

path_to_sound = os.listdir('music/')
path_to_photo = os.listdir('assets/sound_images/')
path_to_sound.sort()
path_to_photo.sort()

sounds = []

path_to_photo.remove('.DS_Store')

for index in zip(path_to_photo, path_to_sound):
    print(index)
    print(index[0])
    sound = SOUND(path_to_photo = index[0], path_to_sound = index[1])
    sounds.append(sound)

screen = pg.display.set_mode((800, 600))

BACKGROUND = pg.image.load('assets/bg.png').convert()
screen.blit(BACKGROUND, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            if 489 <= pg.mouse.get_pos()[1] <= 569 and 350 <= pg.mouse.get_pos()[0] <= 450:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 75 <= pg.mouse.get_pos()[0] <= 140 and 484 <= pg.mouse.get_pos()[1] <= 574:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == 0):
                    sound_index = len(sounds)
                sound_index -= 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 668 <= pg.mouse.get_pos()[0] <= 733 and 484 <= pg.mouse.get_pos()[1] <= 574:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == len(sounds) - 1):
                    sound_index = -1
                sound_index += 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
    pg.display.flip()
