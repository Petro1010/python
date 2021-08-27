from collections import deque
#Breadth First Search
def BFS(G, node1, node2):    #finds if there is a path between 2 nodes
    Q = deque([node1])
    marked = {node1 : True}   #already been to first node
    for node in G.adj:
        if node != node1:
            marked[node] = False   #all the other nodes have yet to be visited
    while len(Q) != 0:  #while queue is not empty
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:   #if node is not already visited, add it to the queue to explore its neighbors and mark it as visited
                Q.append(node)
                marked[node] = True
    return False