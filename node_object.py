class Node:

    def __init__(self, x, y, color=(255, 255, 255), last_node=None, g=9999, h=9999, width=20, height=20):
        self.x = x
        self.y = y
        self.last_node = last_node
        self.width = width
        self.height = height
        self.f = g + h
        self.g = g
        self.h = h
        self.color = color
        self.neighbors = []
        self.neighbor_index = 0

    def __lt__(self, other):  # used when two Node instances are compared and have same f_val in PriorityQueue
        return self           # could use h-heuristic as tiebreaker

    def is_wall(self):
        return self.color == (0, 0, 0)

    def is_start(self):
        return self.color == (0, 255, 0)

    def is_end(self):
        return self.color == (0, 0, 255)

    def set_last_node(self, parent):  # may not need but will improve readability
        self.last_node = parent

    def calculate_f(self):
        if self.g != 9999 and self.h != 9999:
            f_val = self.g + self.h
        else:
            f_val = None
        return f_val

    def next_node(self):  # might not need
        if self.neighbors and self.neighbor_index < len(self.neighbors):
            next_n = self.neighbors[self.neighbor_index]
            self.neighbor_index += 1
        else:
            next_n = None
        return next_n

    def find_neighbors(self, node_obj_lst, grid_wid, grid_h):
        # Can be optimized
        # Based on input from front end - currently works for lst containing start, walls, and end(?) from front-end
        x_values = [self.x - self.width, self.x, self.x + self.width]
        y_values = [self.y - self.height, self.y, self.y + self.height]
        node_map = {}
        for node in node_obj_lst:
            node_map[(node.x, node.y)] = node.color
        for x_val in x_values:
            for y_val in y_values:
                if (0 <= x_val <= grid_wid and 0 <= y_val <= grid_h) and not (x_val == self.x and y_val == self.y):
                    if (x_val, y_val) not in node_map:
                        self.neighbors.append(Node(x_val, y_val, last_node=self))


