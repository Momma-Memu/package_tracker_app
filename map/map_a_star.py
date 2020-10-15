# A simple graph representing a series of cities and the connections between
# them.

map = {
    "Seattle": {("San Francisco", 679)},
    "San Francisco": {("Seattle", 679), ("Los Angeles", 381), ("Denver", 474)},
    "Los Angeles": {("San Francisco", 381), ("Phoenix", 357)},
    "Phoenix": {("Los Angeles", 357), ("Denver", 586)},
    "Denver": {("Phoenix", 586), ("San Francisco", 474), ("Houston", 878), ("Kansas City", 557)},
    "Kansas City": {("Denver", 557), ("Houston", 815), ("Chicago", 412), ("Nashville", 554)},
    "Houston": {("Kansas City", 815), ("Denver", 878)},
    "Chicago": {("Kansas City", 412), ("New York", 712)},
    "Nashville": {("Kansas City", 554), ("Houston", 665), ("Miami", 817)},
    "New York": {("Chicago", 712), ("Washington D.C.", 203)},
    "Washington D.C.": {("Chicago", 701), ("Nashville", 566), ("Miami", 926)},
    "Miami": {("Washington D.C.", 926), ("Houston", 483), ("Nashville", 817)}
}

DELIVERED = "Delivered"
############################################################
class Node():
    def __init__(self, city):
        self._city = city
        # self._parent = None
        self._edges = []

class Edge():
    def __init__(self, node1, node2, dist):
        self._node1 = node1
        self._node2 = node2
        self._dist = dist

all_nodes = {Node(city) for city in map.keys()}


def make_edges(map, all_nodes)


class Path


def find_shortest_path_a_star(map=map, start, end):
    neighbors = map[start]  # dict of tuples of (city, dist)
    path = []
    visited = []

    if end in neighbors:
        return [start, end]

    # while pa







# update to use A* algorithm...
def find_shortest_path(start, end):
    # Question:  Why is a Python list acceptable to use for this queue?
    qq = []
    qq.append([start])
    visited = set()

    while len(qq) > 0:
        path = qq.pop()
        city = path[-1]

        if city == end:
            return path
        else:
            if city not in visited:
                visited.add(city)
                for connection in map[city]:
                    new_path = list(path)
                    new_path.append(connection)
                    qq.insert(0, new_path)

    return "Error: Path not found"


# Determine the next step via BFS.  Set location to delivered at end.
def advance_delivery(location, destination):
    print("advancing", location, destination)
    # shouldn't be called in this case
    if location == DELIVERED:
        return DELIVERED
    if location == destination:
        return DELIVERED

    path = find_shortest_path(location, destination)
    # Safe to say there is a next city if we get here
    return path[1]


#while len(path) > 0: Testing
# print(find_shortest_path("Seattle", "Kansas City"))
