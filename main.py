import os
import pygame as pg
from Map import Map
from InputBox import InputBox

pg.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750
FRAME_RATE = 60
# from, to, max distance
current_path = ["", "", 1000]


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
           'Shenzhen': (1225, 406), 'Dongguan': (1223, 400), 'Hong K    ong': (1232, 408), 'Manila': (1253, 439),
           'Chongqing': (1196, 379), 'Chengdu': (1182, 365), 'Wuhan': (1218, 375), 'Hangzhou': (1245, 384),
           'Shanghai': (1254, 370), 'Nanjing': (1237, 364), 'Beijing': (1233, 322), 'Tienjin': (1238, 332),
           'Seoul': (1280, 337), 'Shenyang': (1256, 310), 'Harbin': (1273, 291), 'Osaka': (1273, 291),
           'Nuuk': (540, 179), "Reykjavik": (663, 186), "Freetown": (701, 464)}
    return out


def draw_paths(g):
    # for edge in g.edges.items():
    #     for dest in edge[1]:
    #         print(locations[edge[0]], "->", locations[dest])
    #         pg.draw.line(screen, pg.Color("black"), locations[edge[0]], locations[dest])
    if current_path[0] in locations.keys() and current_path[1] in locations.keys():
        path = map_graph.shortest_path(current_path[0], current_path[1])
        for i in range(len(path) - 1):
            pg.draw.line(screen, pg.Color("black"), locations[path[i]], locations[path[i + 1]])
    pg.display.flip()


def create_map(places):
    g = Map()
    for location in places:
        g.add_vertex(location)
    for i in places.items():
        for j in places.items():
            if i != j:
                dist = Map.distance_between(i[1], j[1])
                if dist < current_path[2]:
                    g.add_bidirectional_edge(i[0], j[0], dist)
    draw_paths(g)
    return g


def populate_input_boxes():
    text_box_size = (140, 40)
    from_box = InputBox(pg,
                        "From",
                        text_box_size[0] / 2,
                        SCREEN_HEIGHT - text_box_size[1] * 1.25,
                        text_box_size[0],
                        text_box_size[1])
    to_box = InputBox(pg,
                      "To",
                      SCREEN_WIDTH / 2 - text_box_size[0] / 2,
                      SCREEN_HEIGHT - text_box_size[1] * 1.25,
                      text_box_size[0],
                      text_box_size[1])
    max_dist_box = InputBox(pg,
                            "Range",
                            SCREEN_WIDTH - text_box_size[0] * 3 / 2,
                            SCREEN_HEIGHT - text_box_size[1] * 1.25,
                            text_box_size[0],
                            text_box_size[1],
                            text='1000')
    return {'from': from_box, 'to': to_box, 'max_dist': max_dist_box}


def draw_window():
    global images
    map = images['map']
    size = map.get_rect().size
    ratio = SCREEN_WIDTH / size[0]
    images['map'] = pg.transform.smoothscale(map, (int(size[0] * ratio), int(size[1] * ratio)))
    screen.blit(map, (0, 0))


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Flight Paths")
images = load_images()
locations = populate_locations()
input_boxes = populate_input_boxes()

map_graph = create_map(locations)

# Main Loop
run = True


def update_boxes():
    global map_graph
    for input_box in input_boxes.items():
        if input_box[0] == "to":
            if input_box[1].text != current_path[0]:
                current_path[0] = input_box[1].text
                map_graph = create_map(locations)
        elif input_box[0] == "from":
            if input_box[1].text != current_path[1]:
                current_path[1] = input_box[1].text
                map_graph = create_map(locations)
        elif input_box[0] == "max_dist":
            try:
                int(input_box[1].text)
            except ValueError:
                return
            if int(input_box[1].text) != int(current_path[2]):
                current_path[2] = int(input_box[1].text)
                map_graph = create_map(locations)


while run:
    draw_window()
    for event in pg.event.get():
        # if event.type == 5:
        #     print(pg.mouse.get_pos())
        if event.type == pg.QUIT:
            run = False
        for box in input_boxes.values():
            box.handle_event(event)

    for box in input_boxes.values():
        box.update()

    for box in input_boxes.values():
        box.draw(screen)

    update_boxes()
    draw_paths(map_graph)

    pg.display.flip()
    pg.time.delay(1000 // FRAME_RATE)
