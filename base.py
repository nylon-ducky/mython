#from imutils import paths
#import numpy as np
#import imutils
#import cv2
#import matplotlib.pyplot as plt

from colorama import init, Fore
init()

cell = 'c'
wall = 'w'


def init_maze(width, height):
    maze = []
    for i in range (0, width):
        line = []
        for j in range (0, height):
            line.append('u')
        maze.append(line)
    
    import random
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)

    if starting_height == 0:
        starting_height += 1
    if starting_width == 0: 
        starting_width += 1
    
    if starting_height == -1:
        starting_height -= 1
    if starting_width == -1:
        starting_width -= 1

    maze [starting_height] [starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])


    maze [starting_height - 1] [starting_width] = wall
    maze [starting_height] [starting_width - 1] = wall
    maze [starting_height] [starting_width + 1] = wall
    maze [starting_height + 1] [starting_width] = wall

    while walls:
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        if rand_wall[1] != 0:
            
            if maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c':
            
                if rand_wall[0] != 0:   
                    
                    if maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]+1] == 'c':
    
                        if rand_wall[0] != height-1:
                            
                            if maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c':
                                
                                if rand_wall[1] != width-1:
                                    
                                    if maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c':


                                        def surroundingCells(rand_wall):
                                            s_cells = 0
                                            if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
                                                s_cells += 1
                                            if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
                                                s_cells += 1
                                            if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
                                                s_cells +=1
                                            if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                                                s_cells += 1
                                            return s_cells

                                        return maze





def print_maze(maze):
    for i in range (0, len(maze)):
        for j in range (0, len(maze[0])):
            if maze [i] [j] == 'u':
                print (Fore.WHITE, f'{maze [i] [j]}', end = '')
            elif maze [i] [j] == 'c':
                print(Fore.GREEN, f'{maze [i] [j]}', end = '')
            else:
                print(Fore.RED, f'{maze [i] [j]}', end = '')
        print('\n')




#    https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

#    https://www.online-python.com/














