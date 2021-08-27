#Depth First Search
def DFS(G, node1, node2):   #determines if there is a path between 2 nodes
    S = [node1]   #start with initial node
    marked = {}
    for node in G.adj:
        marked[node] = False    #mark all nodes as not visited yet
    while len(S) != 0:
        current_node = S.pop()    #get node of 'stack'
        if not marked[current_node]:   #if its already marked, ignore it
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)    #append all neighbors to stack
    return False

def has_cycle(G):
    marked = {}                 # contains what has already been visited
    for node1 in G.adj:
        marked[node1] = False    #mark all inital nodes as unvisited

    for i in G.adj:
        if not marked[i]:
            if DFS3rec_cyc(G, i, -100, marked):  #initalize parent to -100 as starting node has no parent
                return True

    return False

def DFS3rec_cyc(G, node, parent, marked):
    marked[node] = True             #node has been passed through
    for i in G.adj[node]:
        if not marked[i]:       #if not marked, visit it and make parent current node
            if (DFS3rec_cyc(G, i, node, marked)):
                return True

        elif i != parent:    #if the node is marked and is not the predessor, then there is a cyle
            return True

    return False

def is_connected(G):
    #conduct regular DFS from node 0
    S = [0]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)

    for i in range(len(marked)):     #If any of the nodes were not visited from the starting node, then the graph is not connected
        if marked[i] == False:
            return False

    return True