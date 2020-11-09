import pygame
import a_star_algo as algo
import time

pygame.init()
W, H = 200, 200
node_w = 20
node_h = 20
WIN = pygame.display.set_mode((W, H))
pygame.display.set_caption('A* Search')
FPS = 60
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (248, 255, 1)
red = (255, 0, 0)

# TODO Finish adding doc strings and clean up code and check globals on each method

running = True
start_selected = False
end_selected = False
mouse_pressed = False
check = False
erase_mode = False
running_algo = False
rects_drawn = []
start = None
end = None


def ask_dim():
    global W, H, node_w, node_h, WIN
    # TODO Currently, height of node and width of node do not work, but W and H do, lines that don't work are commented
    #node_w = int(input("Enter the length of each node in pixels: "))
    #node_h = int(input("Enter the height of each node in pixels: "))
    w_grid = int(input("Enter the width of the grid in pixels: "))
    w_grid = node_w * round(w_grid / node_w)
    h_grid = int(input("Enter the height of the grid in pixels: "))
    h_grid = node_h * round(h_grid / node_h)
    print(w_grid, "and", h_grid, "were used to make the grid proportional to node size.")
    W = w_grid
    H = h_grid
    WIN = pygame.display.set_mode((W, H))
    algo.set_grid_dim(W - node_w, H - node_h, node_w, node_h)


def draw_components(rect_list):
    global W, WIN, node_w, node_h
    WIN.fill(white)
    if erase_mode:
        grid_color = red
    else:
        grid_color = black
    for x in range(0, W + 1, node_w):
        pygame.draw.line(WIN, grid_color, (0, x), (W, x))  # Horizontal lines
    for y in range(0, H + 1, node_h):
        pygame.draw.line(WIN, grid_color, (y, 0), (y, H))  # Vertical lines
    for coords, color, dim in rect_list:
        pygame.draw.rect(WIN, color, (coords[0] + 1, coords[1] + 1, dim[0] - 1, dim[1] - 1))


def mouse_logic(mouse_coords, node_coords):
    # TODO could be simplified like wall logic
    global rects_drawn, start_selected, start, end, end_selected, check, white, green, blue
    if not start_selected and WIN.get_at(mouse_coords)[0:3] == white:
        start = (node_coords, green, (node_w, node_h))
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
            end = (node_coords, blue, (node_w, node_h))
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
        wall = (n_coords, black, (node_w, node_h))
        rects_drawn.append(wall)


def wall_erase(m_coor, n_coor):
    global WIN, rects_drawn, black
    if WIN.get_at(m_coor)[0:3] == black:
        rects_drawn = [(coords, color, dim) for coords, color, dim in rects_drawn if coords != n_coor]


def prep_input():
    global rects_drawn, start
    input_nodes = [start[:2]]
    for pos, color, dim in rects_drawn:
        if color != green:
            input_nodes.append((pos, color))
    return input_nodes


def run_algo():
    global start_selected, end_selected, erase_mode, running_algo
    if start_selected and end_selected:
        erase_mode = False
        inputs = prep_input()
        running_algo = True
        algo.start_algo(inputs)
        states = algo.get_states()
        for state in states:
            draw_components(state)
            pygame.display.update()
            time.sleep(0.1)
        print("Done")
        # TODO code dialog box that notifies user to reset
    else:
        pass  # TODO incorporate pop up message saying no start or end detected


def reset():
    global start_selected, end_selected, mouse_pressed, check, erase_mode, running_algo, rects_drawn, start, end
    start_selected = False
    end_selected = False
    mouse_pressed = False
    check = False
    erase_mode = False
    running_algo = False
    rects_drawn = []
    start = None
    end = None


def main_loop():
    global running, WIN, mouse_pressed, rects_drawn, start, end, erase_mode, running_algo
    while running:
        mouse_coords = pygame.mouse.get_pos()
        calc_x = (mouse_coords[0] // node_w) * node_w
        calc_y = (mouse_coords[1] // node_h) * node_h
        node_coords = (calc_x, calc_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not running_algo:
                    mouse_logic(mouse_coords, node_coords)
                mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_algo()
                if event.key == pygame.K_e:
                    erase_mode = not erase_mode
                if event.key == pygame.K_r:
                    reset()  # could add option to reset but keep start stop and walls using key_pressed()
                    algo.reset()

        if mouse_pressed and check and not erase_mode and not running_algo:
            wall_logic(mouse_coords, node_coords)
        elif mouse_pressed and check and erase_mode and not running_algo:
            wall_erase(mouse_coords, node_coords)
        if not running_algo:
            draw_components(rects_drawn)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    ask_dim()
    main_loop()
