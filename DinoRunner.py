# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:36:46 2018

@author: shabs
"""
import time
from PIL import ImageGrab, ImageOps
import pyautogui as pg
import numpy as np

xR = 1                  #Ratio for x-cordinate
yR = 1                  #Ratio for y-cordinate
 
#function for calculating the screen resolution ratio
def inp():
    print("Enter your screen resolution")
    x = int(input())
    y = int(input())
    xRatio = x/1366
    yRatio = y/768
    return(xRatio,yRatio)

#setting the position of dino and replay button    
class position:
    replay = (330*xR,380*yR)
    dino = (190*xR,395*yR)

#function to make dino jump
def jump():
    pg.press('up')
    time.sleep(0.0001)
    
#function to make dino duck    
def duck():
    pg.keyDown('down')
    time.sleep(0.4)
    pg.keyUp('down')
    time.sleep(0.0001)
    
#Starting or restarting the game
def gameStart():
    pg.click(position.replay)
    
#forming a rectangle in which if any obstacle comes, dino jumps    
def jumpingBox():
    box = ((position.dino[0]+46)*xR,(position.dino[1]+25)*yR,(position.dino[0]+100)*xR,(position.dino[1]+30)*yR)
    img = ImageGrab.grab(box)
    Gray = ImageOps.grayscale(img)
    a = np.array(Gray.getcolors())    
    return a.sum()

#forming the rectangle in which if any obstacle comes, dino ducks
def duckingBox():
    box = ((position.dino[0]+30)*xR,(position.dino[1]-25)*yR,(position.dino[0]+110)*xR,(position.dino[1]+5)*yR)
    img = ImageGrab.grab(box)
    Gray = ImageOps.grayscale(img)
    a = np.array(Gray.getcolors())  
    return a.sum()
    
#main function
if __name__ == "__main__" :
    xR,yR = inp()
    gameStart()
    while(True):
        if(jumpingBox()>=520):              #thresholding the box, for dino jumping
            pg.press('up')
            time.sleep(0.0001)
        elif(duckingBox()>=11000):          #thresholding the box, for dino ducking
            pg.keyDown('down')
            time.sleep(0.4)
            pg.keyUp('down')
            time.sleep(0.0001)
        else:                               #none to do, but to pass a thousandth of a second, LOL :D
            time.sleep(0.0001)
