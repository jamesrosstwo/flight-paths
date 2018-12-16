import os

import pygame

pygame.init()

BOARDWIDTH = 1500
BOARDHEIGHT = 800
FRAMERATE = 60


def loadImages():
    out = {}
    images_path = 'resources/images'
    for filename in os.listdir(images_path):
        name = filename.split('.')
        out[name[0]] = pygame.image.load(images_path + '/' + filename)
    return out


def drawWindow():
    global images
    map = images['map']
    size = map.get_rect().size
    ratio = BOARDWIDTH / size[0]
    images['map'] = pygame.transform.smoothscale(map, (int(size[0] * ratio), int(size[1] * ratio)))

    win.blit(map, (0, 0))
    pygame.display.update()


win = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))
pygame.display.set_caption("Flight Paths")
images = loadImages()

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(1000 // FRAMERATE)

    drawWindow()
