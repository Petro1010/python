
   #Author: Mathew Petronilho, Petronim
   #Revised: July 1, 2021

   #Description: A model module for holding the state and status of the game




#@brief An abstract object that represents the game board and its state
from enum import Enum, auto
import random

## @brief An enumerated type that contains all the types of triangles
class MoveType(Enum):
    down = auto()
    up = auto()
    left = auto()
    right = auto()


class game_board:
    
        #@brief Constructor of board
        #@details Creates a board of zeros with two random values
    
    def __init__(self):
        self.SIZE = 4
        self.score = 0
        self.MAX = 2048
        self.BASE = 2
        self.board = []
        for j in range(self.SIZE):
            inner = []
            for k in range(self.SIZE):
                inner.append(0)
            self.board.append(inner)

        for i in range(2):
            self.random_place() 

        

    
        #@brief Resets board to a starting state
    def reset_board(self):
        self.score = 0
        self.board = [[0 for i in range(self.SIZE)] for i in range(self.SIZE)]
        for i in range(2):
            self.random_place()

    
        #@brief Changes board according to direction given
        #@details Shifts board in specified direction and adds tiles accordingly.
        #@param dir Direction in which the board should be shifted

    def update_board(self, dir):
        if (dir == MoveType.down):
            if (self.is_valid_move_down()):
                self.shift_down()
                self.add_down()
                self.shift_down()
            
            else:
                raise Exception("Not Possible to move down")
            
            
        
        elif (dir == MoveType.up):
            if (self.is_valid_move_up()):
                self.shift_up()
                self.add_up()
                self.shift_up()
            
            else:
                raise Exception("Not Possible to move up")
            
        
        elif (dir == MoveType.left):
            if (self.is_valid_move_left()):
                self.shift_left()
                self.add_left()
                self.shift_left()
            
            else:
                raise Exception("Not Possible to move left")
            
        
        else:
            if (self.is_valid_move_right()):
                self.shift_right()
                self.add_right()
                self.shift_right()
            
            else:
                raise Exception("Not Possible to move right")

        #@brief Spawns a random tile in an unoccupied coordinate on the board
        #@details Numbers spawned and their probability of spawning are determined by the random_num function

    def update_random(self):
        zeros = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if (self.board[i][j] == 0):
                    zeros += 1
                
        if (zeros == 0):
            raise Exception("Can not spawn new tile on full board") 

        NotPlaced = True
        while (NotPlaced):
            x = self.random_coord()
            y = self.random_coord()
            if (self.board[x][y] == 0):
                self.board[x][y] = self.random_num()
                NotPlaced = False
            

        #@brief Changes board according to direction given
        #@details Shifts board in specified direction and adds tiles accordingly. Also spawns a new random tile
        #@param dir Direction in which the board should be shifted

    def make_move(self, dir):
        self.update_board(dir)
        self.update_random()

    
        #@brief Get the score of the current game
        #@return The score of the current game
    def get_score(self):
        return self.score

    
        #@brief Get the board of the current game
        #@return The board of the current game
    
    def get_board(self):
        return self.board

    
        #@brief Determines if any valid move can be made on the current board
        #@return A value representing if there are valid moves left to be made
    
    def is_any_valid_move(self):
        return self.is_valid_move_left() or self.is_valid_move_right() or self.is_valid_move_up() or self.is_valid_move_down()

    
        #@brief Determines if the player has won the game
        #@details The game is considered to be won if the MAX value is on the board
        #@return A value representing if there are valid moves left to be made

    def is_game_won(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if (self.board[i][j] == self.MAX):
                    return True
                
        return False
        

    def is_valid_move_left(self):
        for i in range(self.SIZE):        
            for j in range(1, self.SIZE):  #dont check first column
                if (self.board[i][j] != 0 and (self.board[i][j] == self.board[i][j - 1] or self.board[i][j - 1] == 0)):
                    return True
                
        return False
    
    def is_valid_move_right(self):
        for i in range(self.SIZE):        
            for j in range(self.SIZE - 1): #dont check last column
                if (self.board[i][j] != 0 and (self.board[i][j] == self.board[i][j + 1] or self.board[i][j + 1] == 0)):
                    return True
                
        return False
    
    
    def is_valid_move_up(self):
        for i in range(1, self.SIZE):    #dont check first row
            for j in range(self.SIZE):  
                if (self.board[i][j] != 0 and (self.board[i][j] == self.board[i - 1][j] or self.board[i - 1][j] == 0)):
                    return True
                
        return False
    
    def is_valid_move_down(self):
        for i in range(self.SIZE- 1):        #dont check last row
            for j in range(self.SIZE):  
                if (self.board[i][j] != 0 and (self.board[i][j] == self.board[i + 1][j] or self.board[i + 1][j] == 0)):
                    return True
                
        return False
    
    
    def shift_left(self):
        for j in range(self.SIZE):   #each row
            i = 1                     #start at column 1 (left)
            while (i < self.SIZE):   
                if (self.board[j][i] == 0):       #if the tile itself is 0, move on to next
                    i += 1
                    continue
                
                else:
                    for k in range(i, 0, -1):     #shifts current tile as far left as possible
                        if (self.board[j][k - 1] != 0 ):  #if to the left there is not a 0, we can't shift anymore
                            break
                        
                        self.board[j][k - 1] = self.board[j][k]   #shift tile left
                        self.board[j][k] = 0
                        
                    i += 1

    
    def shift_right(self):
        for j in range(self.SIZE):  #each row
            i = self.SIZE - 2                     #start at last column
            while (i >= 0):   
                if (self.board[j][i] == 0):       #if the tile itself is 0, move on to next
                    i -= 1
                    continue
                
                else:
                    for k in range(i, self.SIZE - 1):  #shifts current tile as far right as possible
                        if (self.board[j][k + 1] != 0 ):  #if to the right there is not a 0, we can't shift anymore
                            break
                        
                        self.board[j][k + 1] = self.board[j][k]  #shift tile right
                        self.board[j][k] = 0
                        
                    
                    i -= 1
                    
    
    def shift_up(self):
        for j in range(self.SIZE): 
            i = 1                     
            while (i < self.SIZE):   
                if (self.board[i][j] == 0):       #if the tile itself is 0, move on to next
                    i += 1
                    continue
                
                else:
                    for k in range(i, 0, -1):     #shifts current tile as far up as possible
                        if (self.board[k - 1][j] != 0 ):  #if to the above there is not a 0, we can't shift anymore
                            break
                        
                        self.board[k - 1][j] = self.board[k][j]   #shift tile up
                        self.board[k][j] = 0
                        
                    
                    i += 1
                    
    
    def shift_down(self):
        for j in range(self.SIZE):
            i = self.SIZE - 2                     
            while (i >= 0):   
                if (self.board[i][j] == 0):       #if the tile itself is 0, move on to next
                    i -= 1
                    continue
                
                else:
                    for k in range(i, self.SIZE - 1):     #shifts current tile as far down as possible
                        if (self.board[k + 1][j] != 0 ):  #if below there is not a 0, we can't shift anymore
                            break
                        
                        self.board[k + 1][j] = self.board[k][j]   #shift tile down
                        self.board[k][j] = 0
                        
                    
                    i -= 1
                    
    
    def add_left(self):
        for i in range(self.SIZE):   #each row
            for j in range(self.SIZE - 1):  #column
                if (self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0):
                    self.board[i][j] = self.board[i][j] + self.board[i][j + 1]
                    self.board[i][j + 1] = 0
                    self.score += self.board[i][j]
                
            
    
    def add_right(self):
        for i in range(self.SIZE):   #each row
            for j in range(self.SIZE - 1, 0, -1):  #column
                if (self.board[i][j] == self.board[i][j - 1] and self.board[i][j] != 0):
                    self.board[i][j] = self.board[i][j] + self.board[i][j - 1]
                    self.board[i][j - 1] = 0
                    self.score += self.board[i][j]
    
    def add_up(self):
        for i in range(self.SIZE):   #each column
            for j in range(self.SIZE - 1):  #row
                if (self.board[j][i] == self.board[j + 1][i] and self.board[j][i] != 0):
                    self.board[j][i] = self.board[j][i] + self.board[j + 1][i]
                    self.board[j + 1][i] = 0
                    self.score += self.board[j][i]
    
    def add_down(self):
        for i in range(self.SIZE):   #each column
            for j in range(self.SIZE - 1, 0, - 1):  #row
                if (self.board[j][i] == self.board[j - 1][i] and self.board[j][i] != 0):
                    self.board[j][i] = self.board[j][i] + self.board[j - 1][i]
                    self.board[j - 1][i] = 0
                    self.score += self.board[j][i]
                

    def random_place(self):
        NotPlaced = True
        while (NotPlaced):
            x = self.random_coord()
            y = self.random_coord()
            if (self.board[x][y] == 0):
                self.board[x][y] = self.random_num()
                NotPlaced = False

    def random_coord(self):
        num = random.random()
        
        if (num < 0.25):
            return 0
        elif (num < 0.5):
           return 1
        elif (num < 0.75):
            return 2
        else: 
            return 3
    
    def random_num(self):
        num = random.random()
        
        if (num < 0.2):
            return self.BASE*self.BASE   #20% chance that 4 will occur
        else:
            return self.BASE