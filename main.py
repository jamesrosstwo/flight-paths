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
    out['Bogota'] = (442, 479)
    out['Lima'] = (432, 550)
    out['Sao Paulo'] = (555, 599)
    out['Santiago'] = (455, 644)
    out['Belo Horizonte'] = (565, 577)
    out['Rio de Janeiro'] = (568, 594)
    out['Buenos Aires'] = (504, 650)
    out['Lagos'] = (768, 471)
    out['Abidjan'] = (732, 477)
    out['Kinshasa'] = (811, 519)
    out['Luanda'] = (807, 538)
    out['Madrid'] = (735, 323)
    out['Barcelona'] = (759, 316)
    out['Paris'] = (760, 279)
    out['London'] = (751, 263)
    out['St. Petersburg'] = (878, 214)
    out['Moscow'] = (907, 237)
    out['Istanbul'] = (872, 318)
    out['Cairo'] = (878, 370)
    out['Khartoum'] = (882, 438)
    out['Riyadh'] = (948, 398)
    out['Baghdad'] = (936, 358)
    out['Karachi'] = (1029, 390)
    out['Ahmedabad'] = (1054, 404)
    out['Mumbai'] = (1058, 419)
    out['Hyderabad'] = (1068, 437)
    out['Chennai'] = (1082, 445)
    out['Bangalore'] = (1073, 455)
    out['Calcutta'] = (1113, 409)
    out['Lahore'] = (1058, 356)
    out['Dhaka'] = (1129, 400)
    out['Chittagong'] = (1136, 409)
    out['Bangkok'] = (1170, 441)
    out['Ho Chi Minh City'] = (1195, 456)
    out['Singapore'] = (1183, 492)
    out['Jakarta'] = (1202, 526)
    out['Foshan'] = (1211, 405)
    out['Guangzhou'] = (1216, 404)
    out['Shenzhen'] = (1225, 406)
    out['Dongguan'] = (1223, 400)
    out['Hong Kong'] = (1232, 408)
    out['Manila'] = (1253, 439)
    out['Chongqing'] = (1196, 379)
    out['Chengdu'] = (1182, 365)
    out['Wuhan'] = (1218, 375)
    out['Hangzhou'] = (1245, 384)
    out['Shanghai'] = (1254, 370)
    out['Nanjing'] = (1237, 364)
    out['Beijing'] = (1233, 322)
    out['Tienjin'] = (1238, 332)
    out['Seoul'] = (1280, 337)
    out['Shenyang'] = (1256, 310)
    out['Harbin'] = (1273, 291)
    out['Osaka'] = (1273, 291)
    return out

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
locations = populate_locations()

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
