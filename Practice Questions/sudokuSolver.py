def solve(board):
    point = getPoint(board)
    #print(point)
    if point == -1:   #if no points to find, we are done
        return True
        
    x, y = point
    #print(x, y)
    for i in range(1, 10):
        if checkValid(board, x, y, str(i)):
            board[x][y] = str(i)
            
            if solve(board):   #apply procedure again with the new board
                return True
                
            board[x][y] = "."     #if that number did not work, reset it
        
        
    return False #None of the numbers worked, reset the last number
        
        
        
    
def getPoint(board):   #look for unoccupied spot in matrix
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return (i, j)
    return -1
    
def checkValid(board, x, y, num):
        
    #check the row
    for i in range(9):
        if board[x][i] == num and y != i:
            return False
        
    #check the column
    for i in range(9):
        if board[i][y] == num and x != i:
            return False
        
            
    subGridX, subGridY = x // 3, y // 3    #Finding the sub grid that the point is a part of
    for k in range(subGridX*3, subGridX*3 + 3):
        for g in range(subGridY*3, subGridY*3 + 3):
            if board[k][g] == num:
                return False
        
    return True    #true if it passes all the checks



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solve(board)

print(board)