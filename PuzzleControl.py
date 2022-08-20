import Pieces as p

import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui
import pyautogui
#import sounddevice as sd
from win32api import GetKeyState
import win32api
#from pydub import AudioSegment
from scipy.io.wavfile import write
import subprocess
import pyaudio
import sys
import wave
import os
import shutil
import keyboard 

win2find = 'Puzzle Pirates - Testdog on the Emerald ocean'

sys.setrecursionlimit(300000)

speed = 0.05

def puzzleLive():
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        x,y,w,h  = callback(whnd,False)
    found = False
    stars = []
    stars.append(imagesearcharea("Star.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarFul.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarTop.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarFull.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarEmpty.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    for star in stars:
        if star != [-1,-1]:
            return getPixels()
        else:
            pass
    return puzzleLive()

def puzzleLive2():
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        x,y,w,h  = callback(whnd,False)
    found = False
    stars = []
    stars.append(imagesearcharea("Star.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarFul.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarTop.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarFull.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    stars.append(imagesearcharea("StarEmpty.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None))
    for star in stars:
        if star != [-1,-1]:
            return True
        else:
            return False

def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))

def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

def getPixels():
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        x,y,w,h  = callback(whnd,False)
        #print("FOUND")
    screen = np.array(ImageGrab.grab(bbox=(x+2,y+26,x+w-356 + 2,y+h-29+26)))

    new_screen = process_img(screen)
    return new_screen

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    #print("Window %s:" % win32gui.GetWindowText(hwnd))
    #print("\tLocation: (%d, %d)" % (x, y))
    #print("\t    Size: (%d, %d)" % (w, h))
    return x,y,w,h

def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img,(coords[0],coords[1]) ,(coords[2],coords[3]) , [255,255,255] , 2 )
    except:
        pass

def process_img(original_image):
    RGB = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    
    process_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

    white = np.full((process_img.shape[0], process_img.shape[1], 3), 255, dtype=np.uint8)  # White image  

    RGB = np.where(RGB[:,:] == [0,0,0], white, RGB)   # This is where we replace black pixels


    toolbox = cv2.imread("toolbox.png")
    x = toolbox.shape[0]
    y = toolbox.shape[1]
    xoffset = 249
    yoffset = 61
    RGB[xoffset:x+xoffset,yoffset:yoffset+y] = RGB[xoffset:x+xoffset,yoffset:y+yoffset] - toolbox

    Grey = cv2.cvtColor(RGB,cv2.COLOR_RGB2GRAY)

    #process_img = cv2.Canny(Grey, threshold1=250, threshold2=150)
    
    return Grey


def moveToPuzzPos(xpos,ypos,delay):
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        windowx,windowy,w,h  = callback(whnd,False)
    windowx += 3 + 18
    windowy += 26 + 34
    puzzXmove = windowx + (xpos+1) * 18 - 9    #puzz is 414 x and 558 y
    puzzYmove = windowy + (ypos+1) * 18 - 9    #each node is 18 pix appart -9 gets center
    pyautogui.moveTo(puzzXmove, puzzYmove, delay)


def openPuzzle(speed):
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        x,y,w,h  = callback(whnd,False)
    dutyPos = imagesearcharea("CarpStation.PNG", x,y,x+w-375,y+h-20, precision=0.6, im=None)
    print(dutyPos)
    if dutyPos != [-1,-1]:
        pyautogui.moveTo(dutyPos[0]+x+76, dutyPos[1]+y+21, speed)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        return True
    return False

def closePuzzle(speed):
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        x,y,w,h  = callback(whnd,False)
    dutyPos = imagesearcharea("AbandonDuty.png", x,y,x+w,y+h, precision=0.7, im=None)
    if dutyPos != [-1,-1]:
        pyautogui.moveTo(dutyPos[0]+x+49, dutyPos[1]+y+12, speed)
        pyautogui.click(button='left')
        return True
    else:
        dutyPos = imagesearcharea("AbandonDuty2.PNG", x,y,x+w-375,y+h-20, precision=0.7, im=None)
        if dutyPos != [-1,-1]:
            pyautogui.moveTo(dutyPos[0]+x+46, dutyPos[1]+y+10, speed)
            pyautogui.click(button='left')
            return True
    return False


def selectPeiece(action):
    if action == 0:
        pyautogui.keyDown("1")
        pyautogui.keyUp("1")
    elif action == 1:
        pyautogui.keyDown("2")
        pyautogui.keyUp("2")
    else :
        pyautogui.keyDown("3")
        pyautogui.keyUp("3")

def rotatePeiece(action):
    if action == 0:
        pass
    elif action == 1:
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
    elif action == 2:
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
    elif action == 3:
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")

def flipPeiece(action):
    if action == 0:
        pass
    elif action == 1:
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")

def getBoardArrays(new_screen):
    # get holes
    
    board = []
    
    for y in range(31):
        line = [0]*23
        for x in range(23):
            val = new_screen[int(18*y)+int(18/2)+int(2)][int(18*x)+int(18/2)]
            if(val == 0 or val == 255):
                line[x] = 255
        board.append(line)
        
    
    board=np.asarray(board,dtype=int)
   
    
    #print(board[1:11,1:11])#hole TL
    #print(board[1:11,12:23])#hole TR
    #print(board[20:31,1:11])#hole TL
    #print(board[20:31,12:23])#hole TR
    #print(board[14:19,4:9])#peiece L
    #print(board[14:19,9:14])#peiece M
    #print(board[14:19,14:19])#peiece R

    return board[1:14,1:13],board[1:14,12:25],board[20:33,1:13],board[20:33,12:25],board[14:19,4:9],board[14:19,9:14],board[14:19,14:19]

def getHoleStats(hole):
    for y in range(11):
        if any(np.isin(hole[y],255)):
            break
    #yFirst = y
    yFirst = 0
    for y in range(11-yFirst):
        if not(any(np.isin(hole[y+yFirst],255))):
            break    
    for x in range(11):
        if any(np.isin(hole[:,x],255)):
            break
    #xFirst = x
    xFirst = 0
    for x in range(11-xFirst):
        if not(any(np.isin(hole[:,x+xFirst],255))):
            break

    #keptX = x
    #keptY = y

    keptX = 11
    keptY = 11
    
    #subArray = hole[yFirst:y+yFirst,xFirst:xFirst+x]
    subArray = hole[yFirst:11,xFirst:11]
    holes = []

    print(subArray)
    
    for y in range(keptY):
        for x in range(keptX):
            if 0 == subArray[y,x]:
                holes.append((x,y))

    print(keptX,xFirst)
    print(keptY,yFirst)

    return keptX,keptY,holes,xFirst,yFirst

def getPeieces(toolBox,pieces):
        pDict = {
                  0: "P",
                  1: "F",
                  2: "Y",
                  3: "L",
                  4: "N",
                  5: "T",
                  6: "U",
                  7: "V",
                  8: "W",
                  9: "Z",
                  10: "X",
                  11: "I"
                }
        
        actP = []

        for item in toolBox:
            added = False
            x=0
            for perm in pieces:
                y=0
                for piece in perm:
                    if (np.array_equal(piece,item)):
                        actP.append([x,y])
                        added = True
                    y+=1
                x+=1
            if added == False:
                actP.append([12,0])

        pDict = {
                  0: "P",
                  1: "F",
                  2: "Y",
                  3: "L",
                  4: "N",
                  5: "T",
                  6: "U",
                  7: "V",
                  8: "W",
                  9: "Z",
                  10: "X",
                  11: "I",
                  12: "PUTTY"
                }
        
        actPString = [pDict[actP[0][0]],pDict[actP[1][0]],pDict[actP[2][0]]]
        
        return actP, actPString

'''             
last_time = time.time()

#558,414
#31,23
np.set_printoptions(linewidth=400)
while(True):
    puzzleLive()
    new_screen = getPixels()
    new_screen = new_screen[35:593,19:433]

    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        windowx,windowy,w,h  = callback(whnd,False)
    
    cv2.imshow('window',new_screen)
    cv2.moveWindow('window', windowx-int(424),windowy+20)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destoryAllWindows()
        break
    
    TLB,TRB,BLB,BRB,LP,MP,RP = getBoardArrays(new_screen)
    print(TLB)
    
    x,y,holes = getHoleStats(TLB)
    

    input()            
                
    
    print("loop took {} seconds".format(time.time()-last_time))
    last_time = time.time()
'''




