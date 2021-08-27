from functools import reduce
from pygame import *
import sys

class Queue:
    def __init__(self):
        self.values = []
        self.length = 0

    def add(self, num):
        self.values.append(num)
        self.length += 1

    def remove(self):
        if (len(self.values) == 0):
            return
        x = self.values.pop(0)  #remove from front of list
        self.length = self.length - 1
        return x

    def print(self):
        print(self.values)

    def getLength(self):
    	return self.length


class Graph:

    def __init__(self, *inp):   #allows for different options depending on the amount of inputs given
        if len(inp) == 2:   #m is vertical input 0, n is horizontal input 1
            graph = []
            for i in range(inp[0]):
                graph.append([False for i in range(inp[1])])

        if len(inp) == 1:   #would have to be fixed
            if reduce(lambda x, y: x and y, [len(inp[0][i]) == len(inp[0][i+1]) for i in range(len(inp[0]) - 1)], True):  #reduce function, make list of booleans to ensure all internal lists are of the same length
                graph = inp[0]
            else:
                raise ValueError("Not a valid matrix")


        self.graph = graph
        self.m = len(self.graph)
        self.n = len(self.graph[0])

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def reset_graph(self):
        for i in range(self.m):
            for j in range(self.n):
                self.graph[i][j] = False

    def __str__(self):
        graph = ""
        for i in range(len(self.graph)):
            graph = graph + str(self.graph[i]) + "\n"
        return graph

    def __repr__(self):
        return self.graph

    #function to find shortest path from one coordinate to another using BFS
    def BFS(self, coord1, coord2, blocked_points):    #finds the shortest path between 2 nodes
        self.reset_graph()
        Q = Queue()
        Q.add(coord1)
        #self.graph = self.graph  #set up self.graph matrix to correspond to visited coordinates
        self.graph[coord1[0]][coord1[1]] = True  #mark beginning
        #To consider blockades placed by user, take in input at this point and mark chosen coords as read
        for i in blocked_points:
                self.graph[i[0]][i[1]] = True     #at the blocked points, it will already be considered visited

        pred = [[(0,0) for i in range(self.n)] for i in range(self.m)]  #keeps track of what coordinate came before each coordinate

        while Q.getLength() != 0:  #while queue is not empty
            current_coord = Q.remove()
            # go to all adjacent coordinates of starting coordinate (consider edge cases)

            if current_coord[0] - 1 >= 0: #left coord case
                if (current_coord[0] - 1, current_coord[1]) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] - 1][current_coord[1]] = current_coord
                    break
                if not self.graph[current_coord[0] - 1][current_coord[1]]:
                    Q.add((current_coord[0] - 1, current_coord[1]))
                    self.graph[current_coord[0] - 1][current_coord[1]] = True
                    pred[current_coord[0] - 1][current_coord[1]] = current_coord

            if current_coord[0] - 1 >= 0 and current_coord[1] - 1 >= 0:  # upper left coord case
                if (current_coord[0] - 1, current_coord[1] - 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] - 1][current_coord[1] - 1] = current_coord
                    break
                if not self.graph[current_coord[0] - 1][current_coord[1] - 1]:
                    Q.add((current_coord[0] - 1, current_coord[1] - 1))
                    self.graph[current_coord[0] - 1][current_coord[1] - 1] = True
                    pred[current_coord[0] - 1][current_coord[1] - 1] = current_coord

            if current_coord[0] - 1 >= 0 and current_coord[1] + 1 < self.m:  # lower left coord case
                if (current_coord[0] - 1, current_coord[1] + 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] - 1][current_coord[1] + 1] = current_coord
                    break
                if not self.graph[current_coord[0] - 1][current_coord[1] + 1]:
                    Q.add((current_coord[0] - 1, current_coord[1] + 1))
                    self.graph[current_coord[0] - 1][current_coord[1] + 1] = True
                    pred[current_coord[0] - 1][current_coord[1] + 1] = current_coord

            if current_coord[0] + 1 < self.n: #right coord case
                if (current_coord[0] + 1, current_coord[1]) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] + 1][current_coord[1]] = current_coord
                    break
                if not self.graph[current_coord[0] + 1][current_coord[1]]:
                    Q.add((current_coord[0] + 1, current_coord[1]))
                    self.graph[current_coord[0] + 1][current_coord[1]] = True
                    pred[current_coord[0] + 1][current_coord[1]] = current_coord

            if current_coord[0] + 1 < self.n and current_coord[1] - 1 >= 0: #upper right coord case
                if (current_coord[0] + 1, current_coord[1] - 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] + 1][current_coord[1] - 1] = current_coord
                    break
                if not self.graph[current_coord[0] + 1][current_coord[1] - 1]:
                    Q.add((current_coord[0] + 1, current_coord[1] - 1))
                    self.graph[current_coord[0] + 1][current_coord[1] - 1] = True
                    pred[current_coord[0] + 1][current_coord[1] - 1] = current_coord

            if current_coord[0] + 1 < self.n and current_coord[1] + 1 < self.m:  # lower right coord case
                if (current_coord[0] + 1, current_coord[1] + 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0] + 1][current_coord[1] + 1] = current_coord
                    break
                if not self.graph[current_coord[0] + 1][current_coord[1] + 1]:
                    Q.add((current_coord[0] + 1, current_coord[1] + 1))
                    self.graph[current_coord[0] + 1][current_coord[1] + 1] = True
                    pred[current_coord[0] + 1][current_coord[1] + 1] = current_coord

            if current_coord[1] + 1 < self.m :  #  below coord case
                if (current_coord[0], current_coord[1] + 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0]][current_coord[1] + 1] = current_coord
                    break
                if not self.graph[current_coord[0]][current_coord[1] + 1]:
                    Q.add((current_coord[0], current_coord[1] + 1))
                    self.graph[current_coord[0]][current_coord[1] + 1] = True
                    pred[current_coord[0]][current_coord[1] + 1] = current_coord

            if current_coord[1] - 1 >= 0: #above coord case
                if (current_coord[0], current_coord[1] - 1) == coord2:  #coordinate wanted is found
                    pred[current_coord[0]][current_coord[1] - 1] = current_coord
                    break
                if not self.graph[current_coord[0]][current_coord[1] - 1]:
                    Q.add((current_coord[0], current_coord[1] - 1))
                    self.graph[current_coord[0]][current_coord[1] - 1] = True
                    pred[current_coord[0]][current_coord[1] - 1] = current_coord

        start = coord2
        trace = [start]
        while not (start == coord1):   #start at coord2 and work way backwards to coord1
            trace.append(pred[start[0]][start[1]]) #append where it came from
            start = pred[start[0]][start[1]] #go to where it came from
        trace.reverse()
        return trace

def create_grid(m, n, coord_width):   #create model of the grid
    grid = []
    x, y = 0, 0
    for i in range(m):
        inner = []
        for j in range(n):
            inner.append(Rect(x, y, coord_width, coord_width))  #drawing squares with border
            x += coord_width
        grid.append(inner)
        y += coord_width
        x = 0

    return grid

def draw_grid(screen, colour, block_colour, grid, blocked_points, coord_width):
    #x, y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j].left//coord_width, grid[i][j].top//coord_width) in blocked_points:
                draw.rect(screen, block_colour, grid[i][j])
            #else:
            draw.rect(screen, colour, grid[i][j], 2)  #drawing squares with border
            #x += coord_width
        #y += coord_width
        #x = 0

def string_to_coord(string):
    try:
        coords = string.split(",")
        coords_new = [i.strip() for i in coords]
        x = int(coords_new[0])
        y = int(coords_new[1])
        return (x, y)
    except:
        return (0,0)

def main(m, n):
    #Start of program
    init()

    coord_width = 30
    size = width, height = n*coord_width, m*coord_width + 110 #size of window, will be exact size of grid
    screen = display.set_mode(size)  #displaying window

    myFont= font.SysFont("monospace",20)  #Needed to write words on screen
    clock = time.Clock()
    input_box1 = Rect((n*coord_width)//2 - 10, m*coord_width + 3, (n*coord_width)//2, 32)  #take in first point
    input_box2 = Rect((n*coord_width)//2 - 10, m*coord_width + 38, (n*coord_width)//2, 32) #take in second point
    enter_box = Rect((n*coord_width)//2 - coord_width, m*coord_width + 75, (n*coord_width)//8, 25)  #enter button
    color_inactive = Color('lightskyblue3')
    color_active = Color('dodgerblue2')
    active = False
    box1, box2 = False, False   #tells which box is active
    text1, text2 = '', ''   #text entered into text boxes
    label1 = "Enter First Coord:"
    label2 = "Enter Second Coord:"
    label3 = "Enter"
    coord1 = (0, 0)  #default coordinates
    coord2 = (0, 0)
    grid = create_grid(m, n, coord_width)   #model grid to determine blocked points
    blocked_points = []

    #colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


    not_done = True
    while not_done:

        for i in event.get():      #If event type is hitting the red x than program is shut
            if i.type == QUIT:
                sys.exit()

            if i.type == MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box1.collidepoint(i.pos):  #if position of click is in one of input box
                    # Toggle the active variable.
                    box1 = True
                    box2 = False
                elif input_box2.collidepoint(i.pos):
                    box2 = True
                    box1 = False
                elif enter_box.collidepoint(i.pos):  #if enter button clicked on
                    coord1 = string_to_coord(text1)
                    text1 = ''
                    coord2 = string_to_coord(text2)
                    text2 = ''
                    box1, box2 = False, False

                else:
                    for k in range(len(grid[0])):
                        for j in range(len(grid)):
                            if grid[k][j].collidepoint(i.pos):   #blocked coordinate that has not been selected
                                if not ((grid[k][j].left//coord_width, grid[k][j].top//coord_width) in blocked_points):
                                    blocked_points.append((grid[k][j].left//coord_width, grid[k][j].top//coord_width))  
                                else:
                                    blocked_points.remove((grid[k][j].left//coord_width, grid[k][j].top//coord_width))  #if already selected deselect
                    box1, box2 = False, False
                # Change the current color of the input box.
                #color = color_active if box1 or box2 else color_inactive
            if i.type == KEYDOWN:
                if box1:
                    #if i.key == K_RETURN:
                     #   coord1 = string_to_coord(text1)
                      #  text1 = ''
                    if i.key == K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += i.unicode

                if box2:
                    #if i.key == K_RETURN:
                     #   coord2 = string_to_coord(text2)
                      #  text2 = ''
                    if i.key == K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += i.unicode



        screen.fill(WHITE)   #Fill background with black

        txt_surface = myFont.render(text1, True, BLACK) #render text
        screen.blit(txt_surface, (input_box1.x+5, input_box1.y+5))   #display it
        
        if box1:
            draw.rect(screen, color_active, input_box1, 2)  #display box
        else:
            draw.rect(screen, color_inactive, input_box1, 2)


        txt_surface2 = myFont.render(text2, True, BLACK)
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        if box2:
            # Blit the input_box rect.
            draw.rect(screen, color_active, input_box2, 2)
        else:
            draw.rect(screen, color_inactive, input_box2, 2)


        draw_grid(screen, BLACK, RED, grid, blocked_points, coord_width)
        txt_surface3 = myFont.render(label1, True, BLACK) #render text
        screen.blit(txt_surface3, (coord_width, input_box1.y + 5))   #display it

        txt_surface4 = myFont.render(label2, True, BLACK) #render text
        screen.blit(txt_surface4, (coord_width, input_box2.y + 5))   #display it

        draw.rect(screen, BLACK, enter_box, 2)
        txt_surface5 = myFont.render(label3, True, BLACK) #render text
        screen.blit(txt_surface5, (enter_box.x + 5, enter_box.y + 5))   #display it




        x = Graph(m, n)
        path = x.BFS(coord1,coord2, blocked_points)
        for i in path:
            draw.rect(screen, BLACK, (i[0]*coord_width, i[1]*coord_width, coord_width, coord_width))

        clock.tick(30)
        display.update()   #update graphics on to window

main(20,20)


# x = Graph(5,5)
# print(x)
# print(x.BFS((0,4),(4,4)))


#NEXT STEPS: ACCOUNT FOR BLOCKED SECTIONS, SHOW BFS ON GRID
