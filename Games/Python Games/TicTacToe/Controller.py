import Board
import View
from pygame import *
import sys

def play_tictactoe():

    init()
    coord_width = 400/3
    size = width, height = 600, 600 #size of window, will be exact size of grid
    screen = display.set_mode(size)  #displaying window

    myFont= font.SysFont("monospace",40)  #Needed to write words on screen
    clock = time.Clock()
    
    reset_button = Rect(225, 400, 150, 100)
    reset_active = False


    board = Board.TicTacToe()
    grid = View.create_grid(coord_width)


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)


    not_done = True
    while not_done:
        
        for i in event.get():      #If event type is hitting the red x than program is shut
            if i.type == QUIT:
                sys.exit()

            if i.type == MOUSEBUTTONDOWN:
                 # If the user clicked on the input_box rect.
                 if reset_active:
                    if reset_button.collidepoint(i.pos):  #if position of click is in one of input box
                     # Toggle the active variable.
                        board.reset_board()
                        reset_active = False
                 else:

                    if not (board.game_won() or board.game_tie()):
                        for k in range(len(grid[0])):
                            for j in range(len(grid)):
                                if grid[k][j].collidepoint(i.pos):
                                    board.make_move(((grid[k][j].y//100) - 1, (grid[k][j].x//100) - 1))

                    else:
                        continue

                

        screen.fill(WHITE)   #Fill background with white
        View.print_board(screen, board.get_board(), BLACK, grid, myFont)

        if board.game_won():
            View.reset_button(screen, WHITE, BLUE, myFont, reset_button)
            View.print_won(screen, WHITE, board.get_is_x_turn(), BLUE, myFont)
            reset_active = True

        elif board.game_tie():
            View.reset_button(screen, WHITE, BLUE, myFont, reset_button)
            View.print_tie(screen, WHITE, BLUE, myFont)
            reset_active = True
        
        clock.tick(30)
        display.update()   #update graphics on to window


play_tictactoe()