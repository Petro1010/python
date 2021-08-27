def topo_sort(G):
    nodes = list(G.adj.keys())
    colours = {}
    sched = []
    for node in nodes:
        colours[node] = "white"
    for node in nodes:
        if colours[node] == "white":
            topo_visit(G, node, colours, sched)
    sched.reverse()
    return sched


def topo_visit(G, node, colours, sched):
    colours[node] = "cyan"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            topo_visit(G, neighbour, colours, sched)
    colours[node] = "crimson"
    sched.append(node)