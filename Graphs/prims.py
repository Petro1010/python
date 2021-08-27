class Element:

    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.key) + ")"

def prim2(G):  # non lazy implementation
    MST = WeightedGraph(G.number_of_nodes())    # create new weighted graph
    marked = {}
    pred = {}
    for i in range(G.number_of_nodes()):
        marked[0] = False   #non have been visited so mark them
    Q = MinHeap([])
    for i in range(1, G.number_of_nodes()):
        Q.insert(Element(i, 9999))          #all nodes except for starting node start at length estimates infinity
    Q.insert(Element(0,0))
    while not Q.is_empty():   #while queue is not empty
        v = Q.extract_min().value   #get the minimum node
        if v != 0:   #if its not the start node, add the edge to the MST
            MST.add_edge(v, pred[v], G.w(v,pred[v]))
        marked[v] = True    #mark the node as added to MST
        for edge_info in G.adj[v]:   #go through all connecting nodes
            if edge_info[0] in Q.map:
                if edge_info[1] < Q.get_element_from_value(edge_info[0]).key:  #if weight if edge is less than current estimate, update it
                    Q.decrease_key(edge_info[0], edge_info[1])
                    pred[edge_info[0]] = v
    return MST