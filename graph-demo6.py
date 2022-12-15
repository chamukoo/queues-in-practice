# Dijkstra’s Algorithm Using a Priority Queue

import networkx as nx
from graph import City, load_graph, ddijkstra_shortest_path

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Setting the two nodes to london and edinburgh
city1 = nodes["london"]
city2 = nodes["edinburgh"]

def distance(weights):
    return float(weights["distance"])

for city in ddijkstra_shortest_path(graph, city1, city2,distance):
    print(city.name)
