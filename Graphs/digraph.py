#directed graph using adjacency list
class DiGraph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node2 not in self.adj[node1]:  # if they are not already connected
            self.adj[node1].append(node2)

    def number_of_nodes(self):
        return len(self.adj)

def DFS(G, root):
    colours = {}
    for i in range(G.number_of_nodes()):
        colours[i] = "white"
    DFS_visit(G, root, colours)

def DFS_visit(G, node, colours):
    colours[node] = "cyan"
    print("Colouring cyan: " + str(node))
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            DFS_visit(G, neighbour, colours)
    colours[node] = "crimson"
    print("Colouring crimson: " + str(node))