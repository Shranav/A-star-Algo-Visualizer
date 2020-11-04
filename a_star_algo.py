from queue import PriorityQueue as pq
import math
from flask import Flask
from node_object import Node


open_nodes = []
node_objects_list = []
# Initialize priority queue


def a_star():
    pass


def process_input(json_file):
    # TODO create objects of walls, start, and end
    pass


def h_heuristic(curr_node, end_node):
    """Calculates approximate distance between two nodes

       Used to calculate the distance between two points
       on a graph, which will be used to determine the f
       heuristic in the A* algorithm

       :arg
       curr_node (node object) - current node being checked
       end_node (node object) - target node
    """

    curr_node.h = math.sqrt(((end_node.x - curr_node.x) ** 2) + ((end_node.y - curr_node.y) ** 2))


def g_heuristic(current_n):
    """Calculates cost of traveling from the starting node to current node

       Used to calculate the current cost of traveling to the current nodes
       from the starting node, which will be used to determine the f
       heuristic in the A* algorithm

       :arg
       current_n (node object) - current node being checked
    """

    # TODO need to fix method logic
    current_n.g += current_n.last_node.g  # Don't know if this works


def f_heuristic(current_node):
    """Actual heuristic used to compare the optimal paths between nodes

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
