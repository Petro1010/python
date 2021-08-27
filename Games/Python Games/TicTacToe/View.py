# Mathew Petronilho
# July 12 2021
# Description: GUI for tictactoe board

from pygame import *

# @breif creates a replica of the board with rectangles
def create_grid(coord_width):   #create model of the grid
    grid = []
    x, y = 100, 100
    for i in range(3):
        inner = []
        for j in range(3):
            inner.append(Rect(x, y, coord_width, coord_width))  #drawing squares with border
            x += coord_width
        grid.append(inner)
        y += coord_width
        x = 100

    return grid

# @brief displays the game board
def print_board(screen, board, colour, coords, font):
    for i in range(3):
        for j in range(3):
            #draw board
            coord = coords[i][j]
            draw.rect(screen, colour, coord, 2)

            #draw the symbol
            txt = font.render(board[i][j], True, colour) #render text
            text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2))     #CENTERING TEXT*****************
            screen.blit(txt, text_rect)

# @breif displays message if game won
def print_won(screen, colour, x_turn, box_colour, font):
    coord = Rect(200, 250, 200, 100)
    draw.rect(screen, box_colour, coord)

    if x_turn:
        message = "O Wins!"
    else:
        message = "X Wins!"

    txt = font.render(message, True, colour) #render text
    text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

# @breif displays message if the game ends in a tie
def print_tie(screen, colour, box_colour, font):
    coord = Rect(200, 250, 200, 100)
    draw.rect(screen, box_colour, coord)

    txt = font.render("Tie!", True, colour) #render text
    text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

# @breif displays the reset board button after a game is over
def reset_button(screen, colour, box_colour, font, coord):
    draw.rect(screen, box_colour, coord)

    txt = font.render("Reset", True, colour) #render text
    text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)