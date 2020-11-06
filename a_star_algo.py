from queue import PriorityQueue
import math
from flask import Flask
from node_object import Node


# TODO update start and end when acquiring information from frontend
start = None
end = None
open_nodes = PriorityQueue()
closed_nodes = []
node_objects_list = []


def a_star():
    pass


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
       h (float) - h value for current node, rounded to one decimal place
    """

    # proportional to g by converting pixels into cost units
    dx = (end_node.x - curr_node.x) // end_node.width
    dy = (end_node.y - curr_node.y) // end_node.height
    h = math.sqrt((dx ** 2) + (dy ** 2))
    # TODO insert logic to check whether to put calculated h in node obj (or can be done during algo)
    return round(h, 1)


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

    current_n.g += current_n.last_node.g  # Don't know if this works
    x_diff = abs(current_n.x - next_n.x) // current_n.width
    y_diff = abs(current_n.y - next_n.y) // current_n.height
    if x_diff == y_diff:
        travel_cost = round(math.sqrt(2), 1)
    else:  # shouldn't have another case, but not sure, this is second case: elif x_diff == 0 or y_diff == 0:
        travel_cost = 1
    g_of_neighbor = current_n.g + travel_cost
    # TODO insert logic to check whether to put calculated h in node obj (or can be done during algo)
    return g_of_neighbor


def f_val(current_node):  # may not need
    """Actual value used to compare the optimal paths between nodes

       :arg
       current_n (node object) - current node being checked
    """
    current_node.f = current_node.g + current_node.h


def save_state():
    pass


# setting up app for API
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/AStarAlgo', methods=['GET'])
def a_star_algo_runner():
    pass


# Run app
app.run()
