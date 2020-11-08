import pygame
import time
import a_star_algo as algo

pygame.init()
W, H = algo.grid_w + 20, algo.grid_h + 20
node_w = 20
WIN = pygame.display.set_mode((W, H))
pygame.display.set_caption('A* Search')

running = True
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (248, 255, 1)
red = (255, 0, 0)
start_selected = False
end_selected = False
mouse_pressed = False
check = False
rects_drawn = []
clock = pygame.time.Clock()


def draw_components():
    global W, WIN, black, node_w
    WIN.fill(white)
    for x in range(0, W + 1, node_w):
        pygame.draw.line(WIN, black, (x, 0), (x, H))  # Vertical lines
        pygame.draw.line(WIN, black, (0, x), (W, x))  # Horizontal lines
    for coords, color, dim in rects_drawn:
        pygame.draw.rect(WIN, color, (coords[0] + 1, coords[1] + 1, dim[0] - 1, dim[1] - 1))


def mouse_logic(mouse_coords, node_coords):
    # could be simplified like wall logic
    global rects_drawn, start_selected, start, end, end_selected, check, white, green, blue
    if not start_selected and WIN.get_at(mouse_coords)[0:3] == white:
        start = (node_coords, green, (node_w, node_w))
        start_selected = True
        rects_drawn.append(start)
        check = False
    elif WIN.get_at(mouse_coords)[0:3] == green:
        start = None
        start_selected = False
        rects_drawn = [(coords, color, dim) for coords, color, dim in rects_drawn if color != green]
        check = False
    else:
        if not end_selected and WIN.get_at(mouse_coords)[0:3] == white:
            end = (node_coords, blue, (node_w, node_w))
            end_selected = True
            rects_drawn.append(end)
            check = False
        elif WIN.get_at(mouse_coords)[0:3] == blue:
            end = None
            end_selected = False
            rects_drawn = [(coords, color, dim) for coords, color, dim in rects_drawn if color != blue]
            check = False
        else:
            check = True


def wall_logic(m_coords, n_coords):
    global WIN, rects_drawn, node_w, black, white
    if WIN.get_at(m_coords)[0:3] == white:
        wall = (n_coords, black, (node_w, node_w))
        rects_drawn.append(wall)


def single_click_wall(m_coor, n_coor):
    global WIN, rects_drawn, black
    if WIN.get_at(m_coor)[0:3] == black:
        rects_drawn = [(coords, color, dim) for coords, color, dim in rects_drawn if coords != n_coor]
        time.sleep(0.1)


def main_loop():
    global running, WIN, mouse_pressed, rects_drawn, start, end
    while running:
        mouse_coords = pygame.mouse.get_pos()
        calc_x = (mouse_coords[0] // node_w) * node_w
        calc_y = (mouse_coords[1] // node_w) * node_w
        node_coords = (calc_x, calc_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                single_click_wall(mouse_coords, node_coords)
                mouse_logic(mouse_coords, node_coords)
                mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass # run algo
        if mouse_pressed and check:
            wall_logic(mouse_coords, node_coords)
        draw_components()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main_loop()