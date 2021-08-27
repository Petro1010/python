import Board
import View
from pygame import *
import sys

def play_2048():

    init()
    coord_width = 100
    size = width, height = 800, 600 #size of window, will be exact size of grid
    screen = display.set_mode(size)  #displaying window

    myFont= font.SysFont("monospace",40)  #Needed to write words on screen
    clock = time.Clock()
    
    reset_button = Rect(180, 20, 200, 70)

    #colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 128, 0)
    YELLOW = (255, 255, 0)
    GREEN = (128, 255, 0)
    TORQ = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (127, 0, 255)
    GREY = (160, 160, 160)
    PINK = (255, 153, 255)
    BEIGE = (255, 229, 204) 
    colours = [BLACK, RED, ORANGE, YELLOW, BEIGE, PINK, GREEN, TORQ, BLUE, PURPLE, GREY]

    invalid = False


    boardd = Board.game_board()


    not_done = True
    while not_done:
        
        for i in event.get():      #If event type is hitting the red x than program is shut
            if i.type == QUIT:
                sys.exit()

            if i.type == MOUSEBUTTONDOWN:
                 # If the user clicked on the input_box rect.
                 if reset_button.collidepoint(i.pos):  #if position of click is in one of input box
                 # Toggle the active variable.
                    boardd.reset_board()

            if not boardd.is_any_valid_move(): #no moves remain
                continue

            if i.type == KEYDOWN:
                if boardd.is_game_won():  #game is won
                    invalid = False
                    break
                if i.key == K_UP:
                    #print("yes")
                    try:
                       invalid = False 
                       boardd.make_move(Board.MoveType.up)
                    except:
                        invalid = True

                if i.key == K_DOWN:
                    try:
                        invalid = False
                        boardd.make_move(Board.MoveType.down)
                    except:
                        invalid = True

                if i.key == K_RIGHT:
                    try:
                        invalid = False
                        boardd.make_move(Board.MoveType.right)
                    except:
                        invalid = True

                if i.key == K_LEFT:
                    try:
                        invalid = False
                        boardd.make_move(Board.MoveType.left)
                    except:
                        invalid = True

                

        screen.fill(WHITE)   #Fill background with white
        View.print_board(screen, boardd.get_board(), colours, coord_width, myFont)
        View.print_score(screen, BLACK, myFont, boardd.get_score())
        View.reset_button(screen, BLACK, myFont, reset_button)

        if invalid:
            View.print_invalid(screen, BLACK, myFont)

        if boardd.is_game_won():
            View.print_won(screen, BLACK, myFont)

        if not boardd.is_any_valid_move():
            View.print_lost(screen, BLACK, myFont)



        
        clock.tick(30)
        display.update()   #update graphics on to window

play_2048()