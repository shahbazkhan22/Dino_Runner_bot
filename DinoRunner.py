# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:36:46 2018

@author: shahb
"""
import time
from PIL import ImageGrab, ImageOps
import pyautogui as pg
import numpy as np

xR = 1
yR = 1
 
def inp():
    print("Enter your screen resolution")
    x = int(input())
    y = int(input())
    xRatio = x/1366
    yRatio = y/768
    return(xRatio,yRatio)
    
class position:
    replay = (330*xR,380*yR)
    dino = (190*xR,395*yR)

def jump():
    pg.press('up')
    time.sleep(0.0001)
    
def duck():
    pg.keyDown('down')
    time.sleep(0.4)
    pg.keyUp('down')
    time.sleep(0.0001)
    
def gameStart():
    pg.click(position.replay)
    
def jumpingBox():
    box = ((position.dino[0]+46)*xR,(position.dino[1]+25)*yR,(position.dino[0]+100)*xR,(position.dino[1]+30)*yR)
    img = ImageGrab.grab(box)
    Gray = ImageOps.grayscale(img)
    a = np.array(Gray.getcolors())    
    return a.sum()

def duckingBox():
    box = (220*xR,370*yR,300*xR,400*yR)
    img = ImageGrab.grab(box)
    Gray = ImageOps.grayscale(img)
    a = np.array(Gray.getcolors())  
    return a.sum()
    
if __name__ == "__main__" :
    xR,yR = inp()
    gameStart()
    while(True):
        if(jumpingBox()>=520):
            pg.press('up')
            time.sleep(0.0001)
        elif(duckingBox()>=11000):
            pg.keyDown('down')
            time.sleep(0.4)
            pg.keyUp('down')
            print('Down')
            time.sleep(0.0001)
        else:
            time.sleep(0.0001)