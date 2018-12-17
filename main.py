import os
import pygame as pg

pg.init()

BOARDWIDTH = 1500
BOARDHEIGHT = 800
FRAMERATE = 60

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


def load_images():
    out = {}
    images_path = 'resources/images'
    for filename in os.listdir(images_path):
        name = filename.split('.')
        out[name[0]] = pg.image.load(images_path + '/' + filename)
    return out


def populate_locations():
    out = {'New York City': (440, 318), 'Toronto': (421, 304), 'Detroit': (406, 311), 'Mexico City': (335, 417),
           'Delhi': (1070, 379), 'Tokyo': (1332, 342), 'Los Angeles': (254, 350), 'Dallas': (346, 359),
           'Chicago': (382, 312), 'Philadelphia': (434, 329), 'Atlanta': (395, 352), 'Miami': (414, 388),
           'Houston': (358, 371), 'Bogota': (442, 479), 'Lima': (432, 550), 'Sao Paulo': (555, 599),
           'Santiago': (455, 644), 'Belo Horizonte': (565, 577), 'Rio de Janeiro': (568, 594),
           'Buenos Aires': (504, 650), 'Lagos': (768, 471), 'Abidjan': (732, 477), 'Kinshasa': (811, 519),
           'Luanda': (807, 538), 'Madrid': (735, 323), 'Barcelona': (759, 316), 'Paris': (760, 279),
           'London': (751, 263), 'St. Petersburg': (878, 214), 'Moscow': (907, 237), 'Istanbul': (872, 318),
           'Cairo': (878, 370), 'Khartoum': (882, 438), 'Riyadh': (948, 398), 'Baghdad': (936, 358),
           'Karachi': (1029, 390), 'Ahmedabad': (1054, 404), 'Mumbai': (1058, 419), 'Hyderabad': (1068, 437),
           'Chennai': (1082, 445), 'Bangalore': (1073, 455), 'Calcutta': (1113, 409), 'Lahore': (1058, 356),
           'Dhaka': (1129, 400), 'Chittagong': (1136, 409), 'Bangkok': (1170, 441), 'Ho Chi Minh City': (1195, 456),
           'Singapore': (1183, 492), 'Jakarta': (1202, 526), 'Foshan': (1211, 405), 'Guangzhou': (1216, 404),
           'Shenzhen': (1225, 406), 'Dongguan': (1223, 400), 'Hong Kong': (1232, 408), 'Manila': (1253, 439),
           'Chongqing': (1196, 379), 'Chengdu': (1182, 365), 'Wuhan': (1218, 375), 'Hangzhou': (1245, 384),
           'Shanghai': (1254, 370), 'Nanjing': (1237, 364), 'Beijing': (1233, 322), 'Tienjin': (1238, 332),
           'Seoul': (1280, 337), 'Shenyang': (1256, 310), 'Harbin': (1273, 291), 'Osaka': (1273, 291)}
    return out


def draw_window():
    global images
    map = images['map']
    size = map.get_rect().size
    ratio = BOARDWIDTH / size[0]
    images['map'] = pg.transform.smoothscale(map, (int(size[0] * ratio), int(size[1] * ratio)))
    win.blit(map, (0, 0))
    pg.display.update()


win = pg.display.set_mode((BOARDWIDTH, BOARDHEIGHT))
pg.display.set_caption("Flight Paths")
images = load_images()
locations = populate_locations()

# Game Loop
run = True
while run:
    for event in pg.event.get():
        if event.type == 5:
            print(event.pos)
        if event.type == pg.QUIT:
            run = False

    draw_window()
    pg.time.delay(1000 // FRAMERATE)
