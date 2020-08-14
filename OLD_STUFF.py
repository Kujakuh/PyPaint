# OLD STUFF
def draw_check():
    global draw_on
    if e.type == MOUSEBUTTONDOWN and e.button == 1:
        draw_on = True
    if e.type == MOUSEBUTTONUP and e.button == 1:
        draw_on = False


def round_line(srf, paint, start, end, rad=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, paint, (x, y), rad)


def draw():
    global last_post
    if draw_on:
        e.pos = pygame.mouse.get_pos()
        (x, y) = e.pos
        if y < 450:
            pygame.draw.circle(screen, circle_color, e.pos, radius, 1)
            round_line(screen, circle_color, e.pos, last_post, radius)
        last_post = e.pos

