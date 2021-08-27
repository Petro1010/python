# Author: Mathew Petronilho
# Revised: July 5, 2021
# Description: GUI for 2048 game

from pygame import *
import math

# @brief displays the view of the main board
def print_board(screen, board, colours, coord_width, font):
    x = 200
    y = 100
    for i in range(len(board[0])):
        for j in range(len(board)):

            if board[i][j] == 2 or board[i][j] == 0:
                colour = colours[0]
            else:
                colour = colours[int(math.log(board[i][j], 2)) - 1]   #colour depends on value
            coord = Rect(x, y, coord_width, coord_width)
            draw.rect(screen, colour, coord, 2)

            value = str(board[i][j])
            if value == "0":  #if 0 do not display on the board
                x += coord_width
                continue

            
            txt = font.render(value, True, colours[0]) #render text
            text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2))     #CENTERING TEXT*****************
            screen.blit(txt, text_rect)
            # if (len(value) == 1):
            #   screen.blit(txt, (coord.x + 40, coord.y + 30))   #display it
            # elif (len(value) == 2):
            #   screen.blit(txt, (coord.x + 30, coord.y + 30))   #display it
            # elif (len(value) == 3):
            #   screen.blit(txt, (coord.x + 20, coord.y + 30))   #display it
            # else:
            #   screen.blit(txt, (coord.x + 10, coord.y + 30))   #display it

            x += coord_width

        y += coord_width
        x = 200

# @brief displays the score board
def print_score(screen, colour, font, score):
    coord = Rect(420, 20, 200, 70)
    draw.rect(screen, colour, coord, 2)
    txt = font.render(str(score), True, colour) #render text
    #screen.blit(txt, (coord.x + 30, coord.y + 30))   #display it

    text_rect = txt.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2 + 20))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

    txt2 = font.render("Score:", True, colour) #render text
    #screen.blit(txt2, (coord.x + 30, coord.y))   #display it
    text_rect2 = txt2.get_rect(center=(coord.x + coord.w//2, coord.y + coord.h//2 - 15))     #CENTERING TEXT*****************
    screen.blit(txt2, text_rect2)

# @brief displays the reset button
def reset_button(screen, colour, font, box):
    draw.rect(screen, colour, box, 2)
    txt = font.render("Reset", True, colour) #render text
    text_rect = txt.get_rect(center=(box.x + box.w//2, box.y + box.h//2))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

# @brief displays the message if you win
def print_won(screen, colour, font):
    txt = font.render("You Won!", True, colour) #render text
    #screen.blit(txt, (350, 520))   #display it
    text_rect = txt.get_rect(center=(400, 550))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

# @brief displays the message if you lose
def print_lost(screen, colour, font):
    txt = font.render("No Valid Moves Remain :(", True, colour) #render text
    #screen.blit(txt, (320, 520))   #display it
    text_rect = txt.get_rect(center=(400, 550))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)

# @brief displays message for an invalid move
def print_invalid(screen, colour, font):
    txt = font.render("Not a Valid Move", True, colour) #render text
    #screen.blit(txt, (320, 520))   #display it
    text_rect = txt.get_rect(center=(400, 550))     #CENTERING TEXT*****************
    screen.blit(txt, text_rect)



print(int("0000000000000000000000000000100", 2))