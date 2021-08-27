from pygame import *

import sys

#This is how to initialize a pygame program:
init()



size=width,length=1200,800   #By setting up size like this, we create a tuple that contains both width and length. It is good to have these seperated so we can use them in code later

screen= display.set_mode(size)    #In order to create your screen, use set_mode method and enter a tuple containing width and height of screen in pixels

speed=[2,2] #Set up the speed of the moving ball, it will move 2 pixels right and up

ball=image.load("soccer_ball.gif")  #load in image you would like to use

ballrect= ball.get_rect()   #creates "rectangle" around your object of choice
black= 0,0,0   #RGB colour style
while True:
	for i in event.get():
		if i.type == QUIT:
			sys.exit()


	ballrect= ballrect.move(speed)    #The ball rectangle will move 2 pixels up and 2 pixels right

	if ballrect.left<0 or ballrect.right> width:  #If the left or right of the ball rectangle leaves the space of the window, than the speed in the x is reversed so it moves in the opposite direction
		speed[0]= -speed[0]

	if ballrect.top<0 or ballrect.bottom>length:
		speed[1]= -speed[1]       #If the bottom or top of the ball rectangle leaves the screen, then the speed in the y is reversed so it moves in the opposite direction


	screen.fill(black)   #erase the image using black colour (needs to be done so no trail is left), Colour is inputed through a RGB system (blend of Red, blue and green)
	screen.blit(ball,ballrect)  #draws the ball to the screen
	display.flip() #makes everything drawn on the screen become visible







