import Start as solve
import PuzzleControl as Control
import Pieces as p

import pyautogui
import copy
import time
import cv2
import win32gui
import random
import numpy as np

from collections import Counter

win2find = 'Puzzle Pirates - XXXXX on the Emerald ocean'
MOUSESPEED = 0.2

print("START")
'''
solve.find(7,4,[(0, 0),(0, 1),(0, 3),(5, 1),(5, 2),(6, 1),(6, 2),(6, 3)])

solve.find(6,10)

solve.find(8,8,[(0, 0),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(7, 2),(7, 4),(7, 5)])

solve.find(10,7,[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,3),(8,0),(8,1),(8,3),(9,0),(9,1),(9,3),(9,4),(9,6)])

solve.find(8,10,[(0,3),(0,7),(0,3),(0,9),(7,1),(7,2),(7,4),(7,5),(7,6),(7,7),(7,9)])
'''
solve.find(9,9,[(0,2),(0,3),(0,4),(0,5),(0,6),(7,0),(7,4),(7,5),(7,7),(8,0),(8,1),(8,2),(8,4),(8,5),(8,7),(8,8)])
#(xsize,ysize,(xcord#start@0,ycord#start@0))


test = solve.find(6,10,[],5)

print("TESTS COMPLETE")

def getMiddle(newTarget):
        count = 0
        y=0
        for row in newTarget:
                for x in range(5):
                        if row[x] == 0:
                                if (x == 2 and y == 2):return count
                                count += 1
                y+=1

def canPlace(actPString,xS,yS,sols):
        finPString = []
        for item in actPString:
            finPString.append(item+"1")
            finPString.append(item+"2")
            finPString.append(item+"3")
            finPString.append(item+"4")
            finPString.append(item+"5")
            finPString.append(item+"6")
        canPlace = False
        board=0
        for sol in sols:
            for x in range(xS[board]):
                for y in range(yS[board]):
                    for p in finPString:
                        try:
                            if sol[(x, y)] == p:
                                return True , board ,sol[(x, y)]
                        except:
                            pass
            board+=1
        return False , False , False


def canPlaceAll(actPString,xS,yS,sols):
        editActPString = copy.deepcopy(actPString)
        finPString = []
        for item in actPString:
            finPString.append(item+"1")
            finPString.append(item+"2")
            finPString.append(item+"3")
            finPString.append(item+"4")
            finPString.append(item+"5")
            finPString.append(item+"6")
        canPlace = False
        board=0
        bnp = []
        for sol in sols:
            for x in range(xS[board]):
                for y in range(yS[board]):
                    for p in finPString:
                        try:
                            if sol[(x, y)] == p:
                                canPlace = True
                                bnp.append([board,sol[(x, y)]])
                        except:
                            pass
            board+=1
                 
        print(bnp)

        x = 0

        bnpNC = []

        for x in range(len(bnp)):
                if not(bnp[x] in bnpNC):
                        bnpNC.append(bnp[x])

        bnpK = []

        for item in editActPString:
                for other in bnpNC:
                        if other[1][0] == item:
                                bnpK.append(other)
                                bnpNC.remove(other)
                                break
        boardKeep = []
        peieceKeep = []
        
        for item in bnpK:
                boardKeep.append(item[0])
                peieceKeep.append(item[1])
                

        return canPlace , boardKeep , peieceKeep

def canPlaceAllSingle(actPString,xS,yS,sols):
        editActPString = copy.deepcopy(actPString)
        finPString = []
        for item in actPString:
            finPString.append(item+"1")
            finPString.append(item+"2")
            finPString.append(item+"3")
            finPString.append(item+"4")
            finPString.append(item+"5")
            finPString.append(item+"6")
        canPlace = False
        board=0
        bnp = []
        for sol in sols:
            for x in range(xS[board]):
                for y in range(yS[board]):
                    for p in finPString:
                        try:
                            if sol[(x, y)] == p:
                                canPlace = True
                                bnp.append([board,sol[(x, y)]])
                        except:
                            pass
            if canPlace == True:
                    break
            board+=1
                 
        print(bnp)

        x = 0

        bnpNC = []

        for x in range(len(bnp)):
                if not(bnp[x] in bnpNC):
                        bnpNC.append(bnp[x])

        bnpK = []

        for item in editActPString:
                for other in bnpNC:
                        if other[1][0] == item:
                                bnpK.append(other)
                                bnpNC.remove(other)
                                break
        boardKeep = []
        peieceKeep = []
        
        for item in bnpK:
                boardKeep.append(item[0])
                peieceKeep.append(item[1])
                

        return canPlace , boardKeep , peieceKeep

last_time = time.time()

def completePeiece(pieces,tofind):
    x = 5 - len(tofind[0])
    y = 5 - len(tofind)
    for perm in pieces:
        for piece in perm:
            for i in range(x+1):
                for j in range(y+1):
                    if (np.array_equal(piece[0+j:5-y+j:,0+i:5-x+i],tofind)):
                        return piece

def PlaceDatPeiece(whnd,selectTool,z,x,xPlace,yPlace,MOUSESPEED):
        Control.puzzleLive()   
        win32gui.SetForegroundWindow(whnd)
        Control.selectPeiece(selectTool)
        Control.flipPeiece(z)
        Control.rotatePeiece(x)
        Control.moveToPuzzPos(xPlace,yPlace,MOUSESPEED)
        

def bringToFront(inlist,pos): 
    inlist.insert(0, inlist.pop(pos))
    return inlist

timers = [0,3,2,1]
PLACESPECHOLE = False
DOONE = False
while(True):
    Control.puzzleLive()
    new_screen = Control.getPixels()
    new_screen = new_screen[35:593,19:433]

    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        windowx,windowy,w,h  = Control.callback(whnd,False)
    
    cv2.imshow('window',new_screen)
    cv2.moveWindow('window', windowx-int(424),windowy+20)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destoryAllWindows()
        break
    
    TLB,TRB,BLB,BRB,LP,MP,RP = Control.getBoardArrays(new_screen)

    toolBox = [LP,MP,RP]
    
    xS,yS,sols,xOff,yOff = [],[],[],[],[]
    
    print("DOING SOL")

    count = 1
        
    for hole in [TLB,TRB,BLB,BRB]:
        x,y,holes,xOffset,yOffset = Control.getHoleStats(hole)
        sol = solve.find(x,y,holes)
        
        xS.append(x)
        yS.append(y)
        xOff.append(xOffset)
        yOff.append(yOffset)
        
        sols.append(sol)
        print("Done"+str(count))
        count+=1
    
    print("DONE SOL")

    print(toolBox) 

    actP, actPString = Control.getPeieces(toolBox,p.allRots)

    #havePeiece,hole,target = canPlace(actPString,xS,yS,sols)

    havePeiece,hole,target = canPlaceAll(actPString,xS,yS,sols)

    print(havePeiece,hole,target)
    
    print(actPString)
    
    if havePeiece == False or PLACESPECHOLE == True:
        #random.shuffle(p.BASESHAPES2)
        #random.shuffle(p.BASESHAPES4)
        #random.shuffle(p.BASESHAPES5)
        #random.shuffle(p.BASESHAPES7)
        for item in actPString:
                pos = 0
                random.shuffle(solve.shapes)
                BASESHAPES = copy.deepcopy(solve.shapes)
                random.shuffle(BASESHAPES)
                for stuff1,stuff2 in BASESHAPES:
                        if (stuff2[0] == item):                  #for items in toolsbox #break on find
                                BASESHAPES = bringToFront(BASESHAPES,pos)
                                break
                        pos+=1

        actP, actPString = Control.getPeieces(toolBox,p.allRots)
        
        base_shape_variations = {shape: solve.variation(shape) for shape, name in BASESHAPES}
        if PLACESPECHOLE == False:  #used when peieces aren't available but a single hole isn't about to crack
                print("DOING EDITED SOL")

                xS,yS,sols,xOff,yOff = [],[],[],[],[]

                count = 4

                #chnage to exit on found sol
                                
                for hole in [TLB,TRB,BLB,BRB]:
                        x,y,holes,xOffset,yOffset = Control.getHoleStats(hole)
                        sol = solve.findSpecShapes(x,y,base_shape_variations,actPString,holes)
                                
                        xS.append(x)
                        yS.append(y)
                        xOff.append(xOffset)
                        yOff.append(yOffset)
                                
                        sols.append(sol)
                        print("Done"+str(count))
                        count-=1
                            
                print("DONE EDITED SOL")

                #havePeiece,hole,target = canPlace(actPString,xS,yS,sols)

                havePeiece,hole,target = canPlaceAllSingle(actPString,xS,yS,sols)

                if havePeiece == False:
                        print("PEICES CAN'T SOLVE THESE BOARDS")
                        break
                
        else: #used when peieces aren't available and a single hole is about to crack
                print("DOING EDITED SPEC SOL FOR HOLE " + str(SPECHOLE))
        
                xS,yS,sols,xOff,yOff = [],[],[],[],[]

                count = 1

                temp = copy.deepcopy([TLB,TRB,BLB,BRB])
                temp2 = 0
                for hole in temp:
                        if temp2 == SPECHOLE:
                                temp2 += 1
                                continue
                        for x in range(len(hole)):
                                for y in range(len(hole[x])):
                                        temp[temp2][x][y] = 0
                        temp2 += 1
                
                for hole in temp:
                        x,y,holes,xOffset,yOffset = Control.getHoleStats(hole)
                        sol = solve.findSpecShapes(x,y,base_shape_variations,actPString,holes)
                                
                        xS.append(x)
                        yS.append(y)
                        xOff.append(xOffset)
                        yOff.append(yOffset)
                                
                        sols.append(sol)
                        print("Done"+str(count))
                        count+=1
                            
                print("DONE EDITED SPEC SOL")

                #havePeiece,hole,target = canPlace(actPString,xS,yS,sols)

                havePeiece,hole,target = canPlaceAllSingle(actPString,xS,yS,sols)

                if havePeiece == False:
                        print("PEICES CAN'T SOLVE SPEC SOL")
                        break

                PLACESPECHOLE = False
                DOONE = True
                
    
    
    while havePeiece:
        print("Wait 4 2")
        for NUM in range(len(hole)):
                print(timers)   
                
                holee = hole[NUM]
                targete = target[NUM]
                
                #time.sleep(2)
                newTarget = np.zeros((13,13),dtype=int)
                newTarget.fill(255)
                lookat = sols[holee]
                targetXY = []
                shape = []
                for y in range(yS[holee]):
                    for x in range(xS[holee]):
                        if lookat[(x, y)] == targete:
                            targetXY.append([x,y])
                            shape.append([y,x])
                           
                print(shape)
                for coords in shape:
                    x,y = coords
                    newTarget[x,y]=0
                        
                            
                print(newTarget)
                
                newTarget = newTarget[~np.all(newTarget == 255, axis=1)][:, ~np.all(newTarget == 255, axis=0)]

                print(newTarget)

                newTarget = completePeiece(p.allRots,newTarget)
                
                print(newTarget)
                
                cord = getMiddle(newTarget)

                xPlace,yPlace = targetXY[cord]
                
                print(holee)
                print(targete)
                selectTool = 0
                for tool in actPString:
                        if(targete[0] == tool):
                                break
                        selectTool += 1

                tool = toolBox[selectTool]

                holeADD = [0,0],[11,0],[0,19],[11,19]
                
                print(xPlace+xOff[holee]+1+holeADD[holee][0],yPlace+yOff[holee]+1+holeADD[holee][1])

                xPlace = xPlace+xOff[holee]+1+holeADD[holee][0]
                yPlace = yPlace+yOff[holee]+1+holeADD[holee][1]
                
                #find rotation of toolbox p _actP_

                #tool
                #newTarget
                x = 0
                z = 0
                if(np.array_equal(np.rot90(tool),newTarget)):
                   z = 0
                   x = 1
                elif (np.array_equal(np.rot90(np.rot90(tool)),newTarget)):
                   z = 0
                   x = 2
                elif (np.array_equal(np.rot90(np.rot90(np.rot90(tool))),newTarget)):
                   z = 0
                   x = 3
                elif (np.array_equal(np.fliplr(tool),newTarget)):
                   z = 1
                   x = 0
                elif (np.array_equal(np.rot90(np.fliplr(tool)),newTarget)):
                   z = 1
                   x = 1
                elif (np.array_equal(np.rot90(np.rot90(np.fliplr(tool))),newTarget)):
                   z = 1
                   x = 2
                elif (np.array_equal(np.rot90(np.rot90(np.rot90(np.fliplr(tool)))),newTarget)):
                   z = 1
                   x = 3
                                
                PlaceDatPeiece(whnd,selectTool,z,x,xPlace,yPlace,MOUSESPEED)
                pyautogui.click(button='left')
                #(ADDCLICK)

                #check if placement went through

                for y in range(yS[holee]):
                    for x in range(xS[holee]):
                        if lookat[(x, y)] == targete:
                                lookat[(x, y)] = " "

                for x in range(len(timers)):
                        timers[x] += 1

                timers[holee] = 0
                
                #input("AFTERPLACE")

                
                win32gui.SetForegroundWindow(whnd)
                Control.puzzleLive()
                new_screen = Control.getPixels()
                new_screen = new_screen[35:593,19:433]

                TLB,TRB,BLB,BRB,LP,MP,RP = Control.getBoardArrays(new_screen)

                toolBox = [LP,MP,RP]
                actP, actPString = Control.getPeieces(toolBox,p.allRots)
                
                for SPECHOLE in range(len(timers)):
                        all_zeros = not np.any([TLB,TRB,BLB,BRB][SPECHOLE])
                        if all_zeros == True:
                                timers[SPECHOLE] = 0
                        if timers[SPECHOLE] == 7:
                                PLACESPECHOLE = True
                                break

                if PLACESPECHOLE == True or DOONE == True:
                        break
               # break #

        havePeiece,hole,target = canPlaceAll(actPString,xS,yS,sols)

        if (havePeiece == False or PLACESPECHOLE == True or DOONE == True):
            print("USE TOOLBOX P's for next P or PLACESPECHOLE")
            DOONE = False
            break
       # break #

    print("loop took {} seconds".format(time.time()-last_time))
    last_time = time.time()
