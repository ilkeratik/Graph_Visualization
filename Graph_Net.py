import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from Node import Node


class GraphNet:

    def __init__(self):
        self.nodes = []
        self.nodes.append(Node('Istanbul'))

    def add_node(self,node):
        self.nodes.append(node)

    def add_edges_from_csv_file(self, path, is_bidirectional=False):
        '''
            Adds edges from given path, creates nodes first(once)(for all unique strings) then adds its neighbors
        '''
        cities_w_name = np.zeros((0,2))
        # print(cities_w_name)
        cities_w_name = np.concatenate([cities_w_name,[[i.name, i] for i in self.nodes]])
        
        file = pd.read_csv(path,header=None)

        for _i, row in file.iterrows():
            start_node, end_node = None, None
            if not row[0] in cities_w_name[:,0]:
                start_node = Node(row[0])
                self.add_node(start_node)
                cities_w_name = np.concatenate([cities_w_name, [[start_node.name,start_node]]])
            else:
                start_node = cities_w_name[np.where(cities_w_name[:,0] == row[0])][0][1]

            if not row[1] in cities_w_name[:,0]:
                end_node = Node(row[1])
                self.add_node(end_node)
                cities_w_name = np.concatenate([cities_w_name, [[end_node.name,end_node]]])
            else:
                end_node = cities_w_name[np.where(cities_w_name[:,0] == row[1])][0][1]

            start_node.add_edge(end_node, distance=row[2])

            if is_bidirectional:
                end_node.add_edge(start_node, distance=row[2])
        # print(cities_w_name)
        
    def edges_as_list(self):
        edges_arr = np.array([np.array([node.name, node.edges_as_list()]) for node in self.nodes])
        print(edges_arr.shape)
        new = []
        for i,city in enumerate(edges_arr[:,0]):
            for edge in edges_arr[i,1]:
                new.append([city, edge[0], edge[1]])
        # print(new)
        return new

    def edges_as_dict(self):
        edge_dict = {}
        for node in self.nodes:
            edge_dict[node.name] = node.edges_as_list()
        
        return edge_dict

    def get_edges_of_node(self, _name):
        for node in self.nodes:
            if node.name == _name:
                edges = node.edges_as_list()
                break
        return edges

    def visualize(self):
        G = nx.Graph()
        G.add_weighted_edges_from(gg.edges_as_list())

        pos = nx.spring_layout(G, seed=5465465)
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[('Istanbul','Izmit')],
            width=3,
            edge_color="tab:red",
        )
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw(G,pos, with_labels = True)

        print(nx.info(G))
        plt.show()


if __name__ == "__main__":
    gg = GraphNet()

    gg.add_edges_from_csv_file('distances.csv')
    print(gg.get_edges_of_node('Kirikkale'))
    gg.visualize()
    
