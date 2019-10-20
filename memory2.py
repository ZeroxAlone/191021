# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:12:17 2019

@author: lisa_
"""

import random
import numpy as np
Grid =  [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

Copy =  [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

def SetUpEmptyGrid():
    global Grid
    for i in range(8):
        for j in range(8):
            Grid[i][j] = 0
    
    
def GetEmptyGridPosition():
    global x, y
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if Grid[x][y] == 0:
            break
    

def RandomlyDistributrCards():
    for Number in range(1, 33):
        GetEmptyGridPosition()
        Grid[x][y] = Number
        GetEmptyGridPosition()
        Grid[x][y] = Number

def SetUpPlayers():
    global Points, ThisPlayer
    Points[0] = 0
    Points[1] = 0
    ThisPlayer = 1
    
def GetPlayersCoordinates():
    global x1, y1, x2, y2
    global Copy
    for i in range(8):
        for j in range(8):
            Copy[i][j] = Grid[i][j]
        print(Copy[i])
#    for i in Grid:
#        print(i)
    while True:
        x1 = int(input('x1: ')) - 1
        y1 = int(input('y1: ')) - 1
        if Grid[x1][y1] > 0:
            break
        DisplayGrid()
    while True:
        x2 = int(input('x2: ')) - 1
        y2 = int(input('y2: ')) - 1
        if Grid[x2][y2] > 0 and x1 != x2 or y1 != y2:
            break
        
def DisplayGrid():
    for i in range(8):
        for j in range(8):
            if i == x1 and j == y1:
                print(Copy[i][j])
                Copy[i][j] = 0
            if i == x2 and j == y2:
                print(Copy[i][j])
                Copy[i][j] = 0
    for i in range(8):
        for j in range(8):        
            if Copy[i][j] == 0:
                Grid[i][j] = " "
            else:
                Grid[i][j] = "?"

def TestForMatch():
    if Copy[x1][y1] == Copy[x2][y2]:
        Copy[x1][y1] = 0
        Copy[x2][y2] = 0
        Points[ThisPlayer]+=1
    else:
        SwapPlayers()

def SwapPlayers():
    global ThisPlayer
    if ThisPlayer == 1:
        ThisPlayer = 2
    else:
        ThisPlayer = 1
        
def TestForEndGame():
    global Points
    global GameEnd
    if Points[0] + Points[1] == 32:
        GameEnd = True

def OutPutResults():
    print(Points[1])
    print(Points[2])

def main():
    SetUpEmptyGrid()
    RandomlyDistributrCards()
    SetUpPlayers()
    GameEnd = False
    while GameEnd == False:
        GetPlayersCoordinates()
        DisplayGrid()
        TestForMatch()
        TestForEndGame
    OutPutResults()

main()
'''

'''