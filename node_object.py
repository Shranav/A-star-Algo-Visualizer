class Node:

    def __init__(self, x, y, last_node="", width=20, height=20, g=9999, h=9999, color="white"):
        self.x = x
        self.y = y
        self.last_node = last_node
        self.width = width
        self.height = height
        self.f = g + h
        self.g = g
        self.h = h
        self.color = color

    def is_wall(self):
        return self.color == "black"

    def is_start(self):
        return self.color == "green"

    def is_end(self):
        return self.color == "blue"

    def next_node(self, node_obj_lst):
        # TODO: find next node using pixels
        #  check if already exits in node_obj_lst
        #  if not create an obj out of it and add it to lst
        new_x = self.x + self.width
        new_y = self.y + self.height
        next_n = Node(new_x, new_y)  # Dummy value, not sure if correct
        node_obj_lst.append(next_n)
        return next_n, node_obj_lst
