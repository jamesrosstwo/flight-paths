import os

import pygame

pygame.init()

BOARDWIDTH = 1500
BOARDHEIGHT = 800
FRAMERATE = 60


def load_images():
    out = {}
    images_path = 'resources/images'
    for filename in os.listdir(images_path):
        name = filename.split('.')
        out[name[0]] = pygame.image.load(images_path + '/' + filename)
    return out


def populate_locations():
    out = {}
    out['New York City'] = (440, 318)
    out['Toronto'] = (421, 304)
    out['Detroit'] = (406, 311)
    out['Mexico City'] = (335, 417)
    out['Delhi'] = (1070, 379)
    out['Tokyo'] = (1332, 342)
    out['Los Angeles'] = (254, 350)
    out['Dallas'] = (346, 359)
    out['Chicago'] = (382, 312)
    out['Philadelphia'] = (434, 329)
    out['Atlanta'] = (395, 352)
    out['Miami'] = (414, 388)
    out['Houston'] = (358, 371)

def draw_window():
    global images
    map = images['map']
    size = map.get_rect().size
    ratio = BOARDWIDTH / size[0]
    images['map'] = pygame.transform.smoothscale(map, (int(size[0] * ratio), int(size[1] * ratio)))
    win.blit(map, (0, 0))
    pygame.display.update()


win = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))
pygame.display.set_caption("Flight Paths")
images = load_images()

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == 5:
            print(event.pos)
        if event.type == pygame.QUIT:
            run = False

    draw_window()
    pygame.time.delay(1000 // FRAMERATE)
