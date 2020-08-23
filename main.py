# External Libs
import sys
import cv2
import pygame
from pygame.locals import *

# Locals
from assets import *
from data import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
e = pygame.event.wait()


# UI ------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

def sub_window_render():
    img_render(screen, sub_window, (801, 450), (801, 150))


def img_render(surface, picture, coords, size):
    tmp_img = pygame.image.load(picture)
    image = pygame.transform.scale(tmp_img, size)
    image_rect = image.get_rect()
    image_rect.topright = coords
    surface.blit(image, image_rect)
    return image_rect


class Button:
    def __init__(self, surface, picture, coords, size, action_id, event_handled):
        (self.x, self.y) = coords
        self.surface = surface
        self.picture = picture
        self.size = size
        (self.width, self.height) = self.size
        self.click_event = action_id
        self.event_handled = event_handled

    def click_check(self):
        global circle_color, FILL, radius, erase_on
        button_rect = img_render(self.surface, self.picture, (self.x, self.y), self.size)
        if self.event_handled.type == MOUSEBUTTONDOWN and self.event_handled.button == 1:
            mouse_post = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_post):
                if self.click_event in color_dict:
                    if self.click_event == 0o300:
                        erase_on = True
                        FILL = False
                    else:
                        erase_on = False
                    circle_color = color_dict[self.click_event]
                elif self.click_event == 0o001:
                    self.surface.fill(ERASE, (0, 0, 800, 450))  # Canvas erase
                elif self.click_event == 0o002:
                    if FILL:
                        FILL = False
                    elif not erase_on:
                        FILL = True
                elif self.click_event in pen_width_dict:
                    radius = pen_width_dict[self.click_event]
                    FILL = False


# Draw functions ------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


def bucket(surface, coords, fill_color):
    arr = pygame.surfarray.array3d(surface)
    swap_point = (coords[1], coords[0])
    cv2.floodFill(arr, None, swap_point, fill_color)
    pygame.surfarray.blit_array(surface, arr)


def round_line(srf, paint, start, end, l_width, rad=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, paint, (x, y), rad, l_width)


def draw(color):
    global e, draw_on, last_post
    if e.type == pygame.MOUSEBUTTONDOWN:
        draw_on = True
        (x, y) = e.pos
        if draw_on and y < 450 and not FILL:
            pygame.draw.circle(screen, color, e.pos, radius, line_width)
        elif draw_on and y < 450 and FILL:
            bucket(screen, e.pos, color)
    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False
    if e.type == pygame.MOUSEMOTION:
        (x, y) = e.pos
        if draw_on and y < 450 and not FILL:
            pygame.draw.circle(screen, color, e.pos, radius, line_width)
            round_line(screen, color, e.pos, last_post, line_width, radius)
        last_post = e.pos


# MAIN ----------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

def main():
    global e, draw_on, circle_color

    pygame.display.set_caption("Blackboard")
    screen.fill(ERASE)

    running = True
    while running:
        for e in pygame.event.get():

            sub_window_render()

            clean_button = Button(screen, clean_img, (750, 500), (50, 50), 0o001, e)
            paint_bucket = Button(screen, bucket_button, (180, 490), (36, 36), 0o002, e)
            red = Button(screen, red_button, (255, 490), (35, 35), 0o302, e)
            green = Button(screen, green_button, (290, 490), (35, 35), 0o303, e)
            blue = Button(screen, blue_button, (325, 490), (35, 35), 0o304, e)
            cyan = Button(screen, cyan_button, (255, 525), (35, 35), 0o305, e)
            yellow = Button(screen, yellow_button, (290, 525), (35, 35), 0o306, e)
            magenta = Button(screen, magenta_button, (325, 525), (35, 35), 0o307, e)
            pen = Button(screen, pen_button, (215, 493), (32, 32), 0o301, e)
            white = Button(screen, white_button, (215, 525), (32, 32), 8, e)
            eraser = Button(screen, eraser_button, (180, 526), (36, 36), 0o300, e)

            a1 = Button(screen, a_1, (65, 490), (36, 36), 'a', e)
            a2 = Button(screen, a_2, (100, 490), (36, 36), 'b', e)
            a3 = Button(screen, a_3, (135, 490), (36, 36), 'c', e)
            a4 = Button(screen, a_4, (65, 525), (36, 36), 'd', e)
            a5 = Button(screen, a_5, (100, 525), (36, 36), 'e', e)
            a6 = Button(screen, a_6, (135, 525), (36, 36), 'f', e)

            clean_button.click_check()
            red.click_check()
            green.click_check()
            blue.click_check()
            cyan.click_check()
            yellow.click_check()
            magenta.click_check()
            pen.click_check()
            white.click_check()
            eraser.click_check()
            paint_bucket.click_check()
            a1.click_check()
            a2.click_check()
            a3.click_check()
            a4.click_check()
            a5.click_check()
            a6.click_check()

            draw(circle_color)

            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
