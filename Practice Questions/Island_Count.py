def island_count(n, m, i):
    marked = [[False for k in range(m)] for j in range(n)]  #all the nodes that have been visited
    islands = 0
    rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNum = [-1, 0, 1, -1, 1, -1, 0, 1]
    for ind in range(n):
        for ind2 in range(m):
            if marked[ind][ind2]:  #if already checked, continue
                continue
            if i[ind][ind2] == str(1):  #if start of island, find rest of island
                islands += 1
                
                #begin DFS
                points = [(ind, ind2)]
                while len(points) != 0:
                    curNode1, curNode2 = points.pop()
                    if not(marked[curNode1][curNode2]):    #if its not marked check its adjacent nodes
                        marked[curNode1][curNode2] = True
                        #check all adjacent nodes
                        for x in range(8):
                            adjNode1, adjNode2 = curNode1 + rowNum[x], curNode2 + colNum[x]
                            
                            if in_range(adjNode1, adjNode2, n, m) and i[adjNode1][adjNode2] == str(1):
                                points.append((adjNode1, adjNode2))

    print(f"The amount of islands is {islands}")
    return islands

def in_range(i, j, n, m):
    return i > -1 and i < n and j > -1 and j < m


i = [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]]
island_count(4, 5, i)