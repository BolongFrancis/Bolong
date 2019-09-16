from collections import defaultdict

# Create Object Graph to store the Graph

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight, h1, h2):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        # When calculate the weight, consider the H() as an additional condition
        self.weights[(from_node, to_node)] = weight + h1
        self.weights[(to_node, from_node)] = weight + h2

graph = Graph()

# Type the value of Weights of each edges
# The format is (start node, destnation node, weight between them, h()value of start node, h()value of destination node)
# When we calculate the weight, h()is an additional condition to determine which point is the best point as the shortest path

edges = [
    ('A', 'D', 4, 9, 8),
    ('A', 'S', 7, 9, 10),
    ('A', 'B', 3, 9, 7),
    ('B', 'H', 1, 7, 6),
    ('C', 'L', 2, 8, 6),
    ('D', 'F', 5, 8, 6),
    ('F', 'H', 3, 6, 2),
    ('G', 'E', 2, 3, 0),
    ('H', 'G', 2, 6, 3),
    ('I', 'K', 4, 4, 3),
    ('J', 'K', 4, 4, 3),
    ('K', 'E', 5, 3, 0),
    ('L', 'J', 4, 6, 4),
    ('L', 'I', 4, 6, 4),
    ('S', 'B', 2, 10, 7),
    ('S', 'C', 3, 10, 8),
]

# Scan and add edges
for edge in edges:
    graph.add_edge(*edge)

# Define Astar algorithm implement, to some extent, it is very similar to Dijkstra Shortest Path Algorithm
def Astar(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    # Initial all

    # Always find the nodes
    while current_node != end:
        # Add new node
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

# Output
print('the path is:')
print (Astar(graph, 'S', 'E'))