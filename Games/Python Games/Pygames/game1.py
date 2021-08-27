from pygame import *
import sys
import random

init()
size= width,length= 800, 600

screen= display.set_mode(size)   #Create display screen for game

gameOver= False


playerSize=50     #Assumes player is a square
green= (0,255,0)
red= (255,0,0)
black=(0,0,0)
yellow=(255,255,0)
playerPosition= [width/2,length-playerSize-10]  #starts player at middle of screen, a little bit above the bottom

enemySize= playerSize
enemyPosition= [random.randrange(0,width-enemySize),0]  #Must take into account that the left of the block could be at width, which is outside the screen
enemyList=[enemyPosition]

clock= time.Clock()  #defining a clock for our game


score=0

myFont= font.SysFont("monospace",35)
	
	#Defining these variables helps to get rid of "magic numbers" that float around and may not have value to a reader


def dropEnemies(enemyList):
	delay= random.random() #selects number between 0 and 1

	if len(enemyList) < 10 and delay >0.9:      #Delay attachment slows down time enemies are added so they arent all added at the same time
		x_pos= random.randrange(0,width-enemySize)
		y_pos= 0

		enemyList.append([x_pos,y_pos])

def drawEnemies(enemyList):
	for i in enemyList:
		draw.rect(screen,red,(i[0],i[1],enemySize,enemySize))

def updateEnemies(enemyList,score,speed):
	for idx, i in enumerate(enemyList):
		#Updates position of falling blocks
		if i[1]>=0 and i[1]<length:
			i[1]+= speed     #If enemy is on screen, it will keep falling until it is off screen

		else:  #Off screen
			score+= 1
			enemyList.pop(idx)  #If an enemy goes off screen, it is taken off the list, and a new one is generated


	return score

def setLevel(score):    #determines the speed of falling blocks based on score
	if score< 20 :
		speed= 6
		return speed

	elif score < 40:
		speed= 7
		return speed


	elif score < 60:
		speed= 9
		return speed

	elif score < 100:
		speed= 12
		return speed

	elif score< 150:
		speed= 15
		return speed

	else:
		speed= 20
		return speed









def detectingCollisions(playerPosition,enemyPosition):   #function to detect if the blocks have collided

	playerX= playerPosition[0]
	playerY= playerPosition[1]
	
	enemyX= enemyPosition[0]
	enemyY= enemyPosition[1]

	if 	(playerX +playerSize >=enemyX >= playerX)   or (enemyX + enemySize  >=playerX >= enemyX): 
		if (playerY+ playerSize>= enemyY >= playerY or (enemyY<=playerY<=enemyY + enemySize)):
			return True			#If there is an intersection in both the y and x, then collision is true


	return False  #Otherwise it is false






while not gameOver:  
	

	for i in event.get():   #Generic for a pygame program, determines if x button is clicked and program is shut down
		if i.type == QUIT:
			sys.exit()

	
		if i.type == KEYDOWN:
			x=playerPosition[0]
			y=playerPosition[1]

			if i.key == K_LEFT:
				x= x - playerSize


			elif i.key == K_RIGHT:
				x= x + playerSize

			playerPosition=[x,y]





	screen.fill(black)	#erases previous images using black colour	
	




	
	
	dropEnemies(enemyList)
	score= updateEnemies(enemyList,score,setLevel(score))   #updates enemy positions and holds value of new score

	text= "Score:{0}".format(score)
	label= myFont.render(text, 1, yellow)    #Creates text, parameters are text, horizontal/vertical, and colour

	screen.blit(label,(width-200, length-40)) #Labels the screen with your text in the position you want it to appear

	
	#detecting collision between blocks
	for i in enemyList:	
		if detectingCollisions(playerPosition,i):
			gameOver= True


	drawEnemies(enemyList)


	
	draw.rect(screen,green,(playerPosition[0],playerPosition[1],playerSize,playerSize))  #Green rectangle to the screen, Enter the parameters of the rectangle (left, top and then width and height)
	
	
	clock.tick(30)   #Screen will move at 30 frames/sec

	display.update()  #updates screen with new configurations
