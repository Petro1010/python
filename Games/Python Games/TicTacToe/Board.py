# Mathew Petronilho
# July 12 2021
# Description: Module that represents the board of a tictactoe game

class TicTacToe:

    # @brief initalizer for the game board
    def __init__(self):

        self.board = [["" for j in range(3)] for i in range(3)]
        self.is_x_turn = True

    def get_board(self):
        return self.board

    def get_is_x_turn(self):
        return self.is_x_turn

    # @breif resets board back to original state
    def reset_board(self):
        self.board = [["" for j in range(3)] for i in range(3)]
        self.is_x_turn = True

    # @breif determines if coord is empty
    def is_empty(self, coord):
        return self.board[coord[0]][coord[1]] == ''

    # @breif makes move on the board    
    def make_move(self, coord):
        if not self.is_empty(coord):
            return

        if self.is_x_turn:
            self.board[coord[0]][coord[1]] = "X"
            self.is_x_turn = False
        else:
            self.board[coord[0]][coord[1]] = "O"
            self.is_x_turn = True

    # @brief determines if board is full        
    def full_board(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    count += 1
        return count == 0

    # @breif determines if there is 3 in a row    
    def game_won(self):
        return self.check_horizontals() or self.check_verticals() or self.check_diagonals()

    # @brief determines if all moves has been played and there is no 3 in a row    
    def game_tie(self):
        return not self.game_won() and self.full_board()

    def check_horizontals(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != '':
                return True
        return False

    def check_verticals(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != '':
                return True
        return False

    def check_diagonals(self):
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != '') or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][1] != ''):
            return True
        else:
            return False

    # def print_board(self):
    #     for i in self.board:
    #         print(str(i))



# x = TicTacToe()
# x.make_move((0,0))
# x.make_move((1,1))
# x.make_move((1,0))
# x.make_move((2,1))
# x.make_move((2,0))
# x.make_move((2,2))
# x.make_move((0,1))
# x.make_move((0,2))
# x.make_move((1,2))
# x.print_board()
# print(x.full_board())
# print(x.check_verticals())
# print(x.check_horizontals())
# print(x.check_diagonals())
# print(x.game_won())
# print(x.game_tie())