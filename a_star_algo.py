from queue import PriorityQueue
import math
from flask import Flask
from node_object import Node
from random import randint, randrange

# TODO update start and end when acquiring information from frontend
start = None
end = None
open_nodes = PriorityQueue()
closed_nodes = []
node_objects_list = []
grid_w = 180
grid_h = 180


def a_star():
    print("Starting Algo...")
    global start, end, open_nodes, closed_nodes, node_objects_list, grid_w, grid_h
    h_heuristic(start, end)
    f_val(start)
    open_nodes.put((start.f, start))  # should be taken care of in process_input
    while not open_nodes.empty():
        current_node = open_nodes.get()[1]
        current_node.find_neighbors(node_objects_list, grid_w, grid_h)
        closed_nodes.append(current_node)
        print("Expanding Node at ", current_node.x, ", ", current_node.y, " f = ", current_node.f, " h=",
              current_node.h)
        if current_node.x != end.x or current_node.y != end.y:
            for neighbor_node in current_node.neighbors:
                h_heuristic(neighbor_node, end)
                g_val(current_node, neighbor_node)
                f_val(neighbor_node)
                if check_closed_list(closed_nodes, neighbor_node):
                    #print("skipped")
                    continue
                if check_open_list(open_nodes.queue, neighbor_node):
                    #print("skipped")
                    continue
                print("Neigbhor F: ", neighbor_node.f, " for node at ", neighbor_node.x, ", ",
                      neighbor_node.y, " h = ", neighbor_node.h, " g = ", neighbor_node.g)
                try:
                    closed_nodes.remove(neighbor_node)
                    open_nodes.queue.remove((neighbor_node.f, neighbor_node))
                    print("removed")
                except ValueError:
                    #print("Node was not in open nor closed lists")
                    pass
                open_nodes.put((neighbor_node.f, neighbor_node))
        else:
            path_found(current_node)
            return "A path has been found!"
    return "FAILED: Did not find a viable path"


def check_open_list(node_lst, checking_node):
    for f, node_obj in node_lst:
        if checking_node.x == node_obj.x and checking_node.y == node_obj.y:
            if checking_node.f >= node_obj.f:
                return True
    return False


def check_closed_list(lst_of_nodes, node):
    for list_node in lst_of_nodes:
        if node.x == list_node.x and node.y == list_node.y:
            if node.f >= list_node.f:
                return True
    return False


def path_found(c_node):
    end_node = c_node
    node_pointer = c_node
    path_order = [("x=" + str(end_node.x), " y=" + str(end_node.y), " f=" + str(end_node.f), " g=" + str(end_node.g),
                   " h= " + str(end_node.h), end_node)]
    while node_pointer.x != start.x or node_pointer.y != start.y:
        node_pointer = node_pointer.last_node
        path_order.append(("x=" + str(node_pointer.x), " y=" + str(node_pointer.y), " f=" + str(node_pointer.f),
                           " g=" + str(node_pointer.g), " h= " + str(node_pointer.h), node_pointer))
    print("\n\nFound path:")
    for ind in range(1, len(path_order) + 1):
        print(str(ind) + ": " + str(path_order[-ind]))


def single_case_test(num_walls=0):
    global start, end, node_objects_list
    start = Node(0, 20, "green", g=0)
    end = Node(40, 80, "blue")
    node_objects_list.append(start)
    walls = [Node(0, 40, "black"), Node(20, 40, "black"), Node(40, 40, "black"), Node(20, 20, "black"), Node(0, 0, "black"), Node(20, 0, "black")]
    if 0 < num_walls <= len(walls):
        gen_ed_walls = walls[0:num_walls]
        node_objects_list += walls[0:num_walls]
    print("Start:", start.x, ",", start.y)
    print("End:", end.x, ",", end.y)
    for wall in gen_ed_walls:
        print("Wall", wall.x, ",", wall,y)
    print("\n\n")


def testing():
    global grid_w, grid_h, start, end, node_objects_list
    num_walls = randint(1, 10)
    start = Node(randrange(0, grid_w + 1, 20), randrange(0, grid_h + 1, 20), "green", g=0)
    print("Start coords: ", start.x, ", ", start.y)
    x = randrange(0, grid_w + 1, 20)
    y = randrange(0, grid_h + 1, 20)
    node_objects_list.append(start)
    while x == start.x or y == start.y:
        x = randrange(0, grid_w + 1, 20)
        y = randrange(0, grid_h + 1, 20)
    end = Node(x, y, "blue")
    h_heuristic(start, end)
    f_val(start)
    print("End coords: ", x, ", ", y)
    cords_used_x = [start.x, end.x]
    cords_used_y = [start.y, end.y]
    for _ in range(1, num_walls + 1):
        x1 = randrange(0, grid_w + 1, 20)
        y1 = randrange(0, grid_h + 1, 20)
        while x1 in cords_used_x or y1 in cords_used_y:
            x1 = randrange(0, grid_w + 1, 20)
            y1 = randrange(0, grid_h + 1, 20)
        generated_node = Node(x1, y1, "black")
        node_objects_list.append(generated_node)
        cords_used_x.append(x1)
        cords_used_y.append(y1)
        print("Wall Coords: ", x1, ", ", y1)
    print("Done Generating test data\n")


def process_input(json_file):
    # TODO create objects of walls, start, and end
    pass


def h_heuristic(curr_node, end_node):
    """Calculates approximate distance between two nodes

       Used to calculate the distance between two points
       on a graph, which will be used to determine f
       values in the A* algorithm

       :arg
       curr_node (node object) - current node who's h is being calculated
       end_node (node object) - target node

       :return
       curr_node.h (float) - h value for current node, rounded to one decimal place
    """

    # proportional to g by converting pixels into cost units
    dx = (end_node.x - curr_node.x) // end_node.width
    dy = (end_node.y - curr_node.y) // end_node.height
    h = math.sqrt((dx ** 2) + (dy ** 2))
    curr_node.h = round(h, 1)
    return curr_node.h


def g_val(current_n, next_n):
    """Calculates cost of traveling from the starting node to current node

       Used to calculate the current cost of traveling to the current nodes
       from the starting node, which will be used to determine f
       values in the A* algorithm

       :arg
       current_n (node object) - current node being checked
       next_n (node object) - neighbor of current_n who's g is being calculated

       :return
       g_of_neighbor (float) - g cost of neighbor rounded to 1 decimal
    """

    # current_n.g += current_n.last_node.g  # Don't know if this works
    x_diff = abs(current_n.x - next_n.x) // current_n.width
    y_diff = abs(current_n.y - next_n.y) // current_n.height
    if x_diff == y_diff:
        cost = math.sqrt(2)
        travel_cost = round(cost, 1)
    else:  # shouldn't have another case, but not sure, this is second case: elif x_diff == 0 or y_diff == 0:
        travel_cost = 1
    g_of_neighbor = current_n.g + travel_cost
    # TODO insert logic to check whether to put calculated h in node obj (or can be done during algo)
    next_n.g = round(g_of_neighbor, 1)
    return g_of_neighbor


def f_val(current_node):  # may not need
    """Actual value used to compare the optimal paths between nodes

       :arg
       current_n (node object) - current node being checked
    """
    current_node.f = round(current_node.g + current_node.h, 1)


def save_state():
    pass


# setting up app for API
# app = Flask(__name__)
# app.config["DEBUG"] = True


# @app.route('/AStarAlgo', methods=['GET'])
# def a_star_algo_runner():
#    pass


# Run app
# app.run()
if __name__ == "__main__":
    # testing()
    walls_num = input("Num walls? ")
    single_case_test(int(walls_num))
    s = a_star()
    print(s)
