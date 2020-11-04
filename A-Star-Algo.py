from queue import PriorityQueue as pq
import math
from flask import Flask


def a_star_algo():
    open_nodes = []
    pass


def h_heuristic(curr_node, end_node):
    """Calculates approximate distance between two nodes

       Used to calculate the distance between two points
       on a graph, which will be used to determine the f
       heuristic in the A* algorithm

       :arg
       curr_node (node object) - current node being checked
       end_node (node object) - target node

       :return
       h (int) - calculated value
    """

    h = math.sqrt(((end_node.x - curr_node.x)**2) + ((end_node.y - curr_node.y)**2))
    return h


def g_heuristic():
    """Calculates cost

       Used to calculate the distance between two points
       on a graph, which will be used to determine the f
       heuristic in the A* algorithm

       :arg

       :return
       h (int) - calculated value
    """

    g = 0

    return g


def f_heuristic():
    pass


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