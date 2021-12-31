def findMazePath(maze):
	nodes = [(0,0)]   #starting point is (0,0)
	n = len(maze)
	m = len(maze[0])
	if maze[0][0] == 0 or maze[n - 1][m - 1] == 0:
		return -1

	marked = [[False for i in range(m)] for j in range(n)]
	rowNum = [0, 0, 1, -1]   #up, down, right, left
	colNum = [-1, 1, 0, 0]

	parents = [[(None, None) for i in range(m)] for j in range(n)]   #parents of each node visited

	while len(nodes) != 0:
		ind1, ind2 = nodes.pop()
		if not(marked[ind1][ind2]):
			marked[ind1][ind2] = True

			for i in range(4):
				nextInd1, nextInd2 = ind1 + colNum[i], ind2 + rowNum[i]
				if isValid(nextInd1, nextInd2, n, m) and maze[nextInd1][nextInd2] == 1:
					if not(marked[nextInd1][nextInd2]):
						parents[nextInd1][nextInd2] = (ind1, ind2)   #if it does not have a parent, mark their parent
					nodes.append((nextInd1, nextInd2))

	if not marked[n - 1][m - 1]:
		return -1

	ans = [[0 for i in range(m)] for j in range(n)]
	point = (n - 1, m - 1)
	while point != (0, 0):
		ans[point[0]][point[1]] = 1
		point = parents[point[0]][point[1]]

	ans[0][0] = 1
	return ans


def isValid(i, j, n, m):
	return i < n and i > -1 and j < m and j > -1


i = [[1,0,0,0,1],
     [0,1,1,1,0],
     [1,1,1,0,1],
     [1,1,1,1,1],
     [1,1,1,1,1]]

print(findMazePath(i))
