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





















