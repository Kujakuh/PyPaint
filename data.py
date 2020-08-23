BLUE = (0, 0, 255)
ERASE = (255, 255, 255)
WHITE = (255, 255, 255)
PEN = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FILL = False

click_id_list = {0o001, 0o002, 0o003}

color_dict = {0o301: PEN, 0o300: ERASE, 0o302: RED, 0o303: GREEN, 0o304: BLUE,
              0o306: YELLOW, 0o305: CYAN, 0o307: MAGENTA, 8: WHITE}

pen_width_dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10, 'f': 15}

circle_color = PEN
mouse_pos = (0, 0)
last_post = (0, 0)
draw_on = False
erase_on = False
radius = 2
line_width = 0
