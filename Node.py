
class Node:

    def __init__(self, n):
        self.name = n
        self.edges = []

    def add_edge(self, node, distance=0):
        self.edges.append([node,distance])

    def edges_as_list(self):
        return [(edge[0].name, edge[1]) for edge in self.edges]

    def edges_as_list_no_weight(self):
        return [edge[0].name for edge in self.edges]