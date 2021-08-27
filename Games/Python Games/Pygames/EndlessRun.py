from pygame import *

import sys
import random

init()
size= width, height= 800,600       #set size

screen= display.set_mode(size)   #create window

gameOver= False

green= (0,255,0)     #Define colours
black= (0,0,0)
blue=(0,0,255)
sky_blue=(135,206,235)

playerSize= 40   #Player definitions
x=(width/160)+40 
y=2*height/3-playerSize
playerPosition= [x,y]

jumpCount= 10  #used for jumps
jump= False

enemySizeY= 50   #Enemy information
enemySizeX= enemySizeY/3
enemyX= 790-enemySizeX
enemyY= 2*height/3-enemySizeY
enemyPosition= [enemyX,enemyY]
enemy1= (enemyPosition[0],enemyPosition[1],enemySizeX,enemySizeY)

enemyType= 0

speed= 15
score=0
medium=False
hard=False
level= [medium,hard]

clock= time.Clock()   #needed to define frames

myFont= font.SysFont("monospace",35)  #Needed to write words on screen

def updateEnemy(enemyPosition,score,speed):
	if enemyPosition[0]>=0 and enemyPosition[0]<width:      #If enemy is on screen, keep it moving left
		enemyPosition[0]-= speed

	else:    #When it goes off screen, reset it
		score+= 1
		enemyPosition[0]= enemyX

	return score


def detectingCollisions(playerPosition,enemyPosition):   #function to detect if the blocks have collided

	playerX= playerPosition[0]
	playerY= playerPosition[1]
	
	enemyX= enemyPosition[0]
	enemyY= enemyPosition[1]

 
	if (enemyX<=playerX <= enemyX+ enemySizeX) or (playerX<=enemyX<=playerX+ playerSize):
		if ((playerY+ playerSize>= enemyY >= playerY ) or (enemyY<=playerY<=enemyY + enemySizeY)):
			return True			#If there is an intersection in both the y and x, then collision is true

	
	return False


def setLevel(score,level):
	if score<5:
		speed=10
		return speed

	elif score< 10:
		speed= 15
		return speed

	elif score< 20:
		speed=20
		level[0]= True
		return speed

	elif score< 40:
		speed= 25
		level[1]= True
		level[0]= False
		return speed

	else:
		speed= 35
		return speed

while not gameOver:      #Game loop
	time.delay(50)   #adds a delay between when you can hit buttons 

	for i in event.get():      #If event type is hitting the red x than program is shut
		if i.type == QUIT:
			sys.exit()


		if i.type == KEYDOWN:
			if i.key == K_UP:  #Jump code sequence, if up button is pressed, character will jump
				jump= True

				

	if jump:
	
		if jumpCount>= -10:
			neg= 1

			if jumpCount< 0:
				neg= -1      #When jump count is in its second half, then the object should start falling back down, so the function should be reversed

			playerPosition[1]=playerPosition[1]-((jumpCount**2)*neg*0.5)   # This is a quadratic function which will cause the y position to change in a parabolic manner.

			jumpCount-= 1

		else:
			jumpCount= 10   #Once the jumpcount is past -10, it needs to be reset back to its original so the character can jump again
			jump= False



	if level[0]:

		enemy2SizeX= enemySizeX+ enemySizeY*2
		enemy2SizeY= enemySizeY + 20
		enemy2= (enemyPosition[0],enemyPosition[1],enemy2SizeX,enemy2SizeY)


		enemyType= random.randrange(0,2)


	if level[1]:

		enemy3SizeY= enemySizeY*2

		enemy3= (enemyPosition[0],enemyPosition[1],enemySizeX,enemy3SizeY)


		enemyType= random.randrange(0,3)





	
	screen.fill(sky_blue)   #Fill background with light blue
	

	score= updateEnemy(enemyPosition,score,setLevel(score,level))   #allows the enemy to move across the screen, and keeps track of score
	
	if detectingCollisions(playerPosition,enemyPosition):  #If the collision detection is true, than the game is over
		gameOver= True

	

	text= "Score:{0}".format(score)
	label= myFont.render(text, 1, black)    #Creates text, parameters are text, horizontal/vertical, and colour

	screen.blit(label,(width-200, height/15)) #Labels the screen with your text in the position you want it to appear



	draw.rect(screen,green,(0,2*height/3,width,height/3))    #Draw grass
	draw.rect(screen,blue,(playerPosition[0],playerPosition[1],playerSize,playerSize))   #Draw player

	if enemyType== 0:
		draw.rect(screen,black,(enemyPosition[0],enemyPosition[1],enemySizeX,enemySizeY))  #draw enemy

	elif enemyType == 1:
		draw.rect(screen,black,(enemyPosition[0],enemyPosition[1],enemy2SizeX,enemy2SizeY))

	else:
		draw.rect(screen,black,(enemyPosition[0],enemyPosition[1],enemySizeX,enemy3SizeY))


	clock.tick(30)   #Screen will move at 30 frames/sec
	display.update()   #update graphics on to window






		#NEXT STEPS:
	
		#CREATE MULTIPLE DIFFERENT TYPES OF ENEMIES
		#SEE IF PICTURES CAN BE INSERTED


