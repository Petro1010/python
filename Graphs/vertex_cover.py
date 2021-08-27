#vertex cover and independant set
class Graph:

    def __init__(self):
        self.adj = {}

    def are_connected(self, node1, node2):
        for node in self.adj[node1]:
            if node == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node2 in self.adj[node1]:
            self.adj[node1].remove(node2)
        if node1 in self.adj[node2]:
            self.adj[node2].remove(node1)

    def remove_incident_edges(self, node):
        for neighbour in self.adj[node]:
            self.adj[neighbour].remove(node)
        self.adj[node] = []

    def has_no_edges(self):
        for node in self.adj:
            if len(self.adj[node]) > 0:
                return False
        return True

    def copy(self):
        new_G = Graph()
        new_G.adj = self.adj.copy()
        for node in self.adj:
            new_G.adj[node] = self.adj[node].copy()
        return new_G

    def number_of_nodes(self):
        return len(self.adj)


#Biggest critique: Time and space, we must keep all of the sets stored at the same time which uses alot of memory. Should really only consider one at a time
def vertex_cover(G):
    nodes = list(G.adj.keys())
    best_cover = nodes   #all the nodes creates a vertex cover
    covers = power_set(nodes) #Generate all possible covers
    for i in covers:
        if is_vertex_cover(G, i):
            if len(i) < len(best_cover): #if cover is smaller than best known, update best cover
                best_cover = i
    #Return best cover
    return best_cover


def is_vertex_cover(G, cover):
    temp_G = G.copy()
    for node in cover:
        temp_G.remove_incident_edges(node)
    if temp_G.has_no_edges():
        return True
    return False


def power_set(elements):
    if elements == []:
        return [[]]
    return add_to_each(power_set(elements[1:]), elements[0]) + power_set(elements[1:])


def add_to_each(sets, element):
    my_sets = sets.copy()
    for my_set in my_sets:
        my_set.append(element)
    return my_sets

#Improvements: we iterate through power sets from biggest to smallest but why not go from smallest to biggest and return the first vertex cover we see
#maximum independent set is everything not in the minimum vertex cover