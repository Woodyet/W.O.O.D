###create board class####

import random
import numpy as np
import copy
from PIL import Image
import cv2
from range_key_dict import RangeKeyDict
from skimage import measure
import time

class Game:
    ######Peieces####

    P = np.array([[False,False,False,False,False],
                  [False,True,True,False,False],
                  [False,True,True,True,False],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    F = np.array([[False,False,False,False,False],
                  [False,False,True,True,False],
                  [False,True,True,False,False],
                  [False,False,True,False,False],
                  [False,False,False,False,False]])

    Y = np.array([[False,False,False,False,False],
                  [False,False,False,False,False],
                  [False,True,True,True,True],
                  [False,False,True,False,False],
                  [False,False,False,False,False]])

    L = np.array([[False,False,False,False,False],
                  [False,False,False,False,False],
                  [False,True,True,True,True],
                  [False,True,False,False,False],
                  [False,False,False,False,False]])

    N = np.array([[False,False,False,False,False],
                  [False,True,True,False,False],
                  [False,False,True,True,True],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    I = np.array([[False,False,False,False,False],
                  [False,False,False,False,False],
                  [True,True,True,True,True],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    T = np.array([[False,False,True,False,False],
                  [False,False,True,False,False],
                  [False,True,True,True,False],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    W = np.array([[False,False,False,False,False],
                  [False,True,False,False,False],
                  [False,True,True,False,False],
                  [False,False,True,True,False],
                  [False,False,False,False,False]])

    U = np.array([[False,False,False,False,False],
                  [False,True,False,True,False],
                  [False,True,True,True,False],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    V = np.array([[False,False,True,False,False],
                  [False,False,True,False,False],
                  [False,False,True,True,True],
                  [False,False,False,False,False],
                  [False,False,False,False,False]])

    Z = np.array([[False,False,False,False,False],
                  [False,True,True,False,False],
                  [False,False,True,False,False],
                  [False,False,True,True,False],
                  [False,False,False,False,False]])

    X = np.array([[False,False,False,False,False],
                  [False,False,True,False,False],
                  [False,True,True,True,False],
                  [False,False,True,False,False],
                  [False,False,False,False,False]])

    
    PUT =np.array([[True,True,True,True,True],
                  [True,False,False,False,True],
                  [True,False,False,False,True],
                  [True,False,False,False,True],
                  [True,True,True,True,True]])
                  
    difficulty = 2
    holesGenerated = 0
    holesPerDifficulty = [None,None,4,6,8,10,12,15,17,None]
    moves = 0
    ACTION_SPACE_SIZE = 35
    OBSERVATION_SPACE_VALUES = 519
    
    def __init__(self):
        self.holes = [Hole(1,Game.difficulty),Hole(2,Game.difficulty),Hole(3,Game.difficulty),Hole(4,Game.difficulty)]
        self.holes[0].genHole()
        self.holes[1].genHole()
        self.holes[2].genHole()
        self.holes[3].genHole()
        self.pieceDict = RangeKeyDict({
                                (0,22):self.randomZKey(self.randomXKey(Game.P)),
                                (22,36):self.randomZKey(self.randomXKey(Game.F)),
                                (36,50):self.randomZKey(self.randomUDFlip(Game.Y)),
                                (50,58):self.randomZKey(self.randomUDFlip(Game.L)),
                                (58,66):self.randomZKey(self.randomUDFlip(Game.N)),
                                (66,73):self.randomXKey(Game.T),
                                (73,77):self.randomXKey(Game.U),
                                (77,81):self.randomXKey(Game.V),
                                (81,85):self.randomZKey(self.randomXKey(Game.W)),
                                (85,89):self.randomZKey(self.randomXKey(Game.Z)),
                                (89,92):Game.X,
                                (92,94):Game.I,
                                (94,95):Game.PUT,})
        
        self.chestPieces = [[None],[None],[None]]
        self.initChest()
        self.done = False
        Game.holesGenerated=4
        self.scoreFromAction = 0
        self.scoreFromTimers = 0
        Game.moves = 0
        

    def randomXKey(self,peiece):
        for x in range(random.randrange(0,4)):
            peiece = np.rot90(peiece)
        return peiece

    def randomZKey(self,peiece):
        for x in range(random.randrange(0,2)):
            peiece = np.fliplr(peiece)
        return peiece

    def randomUDFlip(self,peiece):
        for x in range(random.randrange(0,2)):
            np.flipud(peiece)
        return peiece
        
    def board(self):
        pass
        
    def moveHoles(self,holes):
        self.holes
        
    def initChest(self):
        temp = 0
        for element in self.chestPieces:
            if not(all(element)) == None:
                self.chestPieces[temp]=self.getRandPeiece()
            temp+=1

    def getRandPeiece(self):
        return self.pieceDict[random.randrange(0,95)]

    def putPeiece(self,hole,peieceSelect,x,y,xRots,zTrue):
        peiece = self.chestPieces[peieceSelect]
        peiece = self.rotPiece(peiece,xRots)
        if (zTrue == 1):
            peiece = self.ZKey(peiece)
            #print("Flipped")
        return self.holes[hole].placePeiece(peiece,x,y)

    def rotPiece(self,peiece,rots):
        for x in range(0,rots):
            peiece = np.rot90(peiece)
        return peiece

    def ZKey(self,peiece):
        peiece = np.fliplr(peiece)
        return peiece

    def showChest(self):
        forShow = []
        tit = 1
        every = []
        #print(self.chestPieces[0])
        #print(self.chestPieces[1])
        #print(self.chestPieces[2])
        for item in self.chestPieces:
            for x in range(len(item)):
                for y in range(len(item[x])):
                    if item[x][y] == False:
                        forShow.append("X")
                    else :
                        forShow.append("O")
            y , x = item.shape
            temp = 0
            show = []
            row = []
            for element in forShow:
                row.append(element)
                temp += 1
                if temp == x:
                    show.append(row)
                    row = []
                    temp = 0
            for element in show:
                #print(element)
                #print()
                pass
            my_array = item.reshape((y, x)).astype('uint8')*255
            res = cv2.resize(my_array,(x*20,y*20),fx=0, fy=0, interpolation = cv2.INTER_NEAREST)
            xs,ys=res.shape
            for y in range(ys):
                for x in range(xs):
                    if ( ((x%20) == 0) or  ((y%20) == 0)):
                        if (res[x][y] == 255):
                            res[x][y]=0
                        else :
                            res[x][y]=255
            #im = Image.fromarray(res)
            im = res
            tit+=1
            #im.show()
            every.append(im)
        return every
            
        
    def stepViz(self,action):
        cv2.imshow('Hole0',self.holes[0].showHole())
        cv2.imshow('Hole1',self.holes[1].showHole())
        cv2.imshow('Hole2',self.holes[2].showHole())
        cv2.imshow('Hole3',self.holes[3].showHole())
        
        temp = self.showChest()

        cv2.imshow('P0',temp[0])
        cv2.imshow('P1',temp[1])
        cv2.imshow('P2',temp[2])

        cv2.moveWindow('Hole0', 100,50)
        cv2.moveWindow('Hole1', 500,50)
        cv2.moveWindow('Hole2', 100,500)
        cv2.moveWindow('Hole3', 500,500)
        cv2.moveWindow('P0', 150,800)
        cv2.moveWindow('P1', 300,800)
        cv2.moveWindow('P2', 450,800)
        '''
        cv2.imshow('Hole0',self.holes[0].showHole())
        cv2.imshow('Hole1',self.holes[1].showHole())
        cv2.imshow('Hole2',self.holes[2].showHole())
        cv2.imshow('Hole3',self.holes[3].showHole())

        cv2.imshow('P0',temp[0])
        cv2.imshow('P1',temp[1])
        cv2.imshow('P2',temp[2])
        '''
        
        

        [hole,peiecePick,x,y,xRots,zTrue]=action
        
        temp = self.putPeiece(hole,peiecePick,x,y,xRots,zTrue)
        self.scoreFromAction = temp
        
        if (not(temp == -400.34)):
            self.chestPieces[peiecePick]=self.getRandPeiece()
            for x in range(3):
                if x == hole:
                    continue
                self.scoreFromTimers = self.holes[x].upCounterForWiggle()

        self.checkHoles()
        '''
        try:
            if (self.moves == 5000):
                self.done = True
                #print("Game")
            else:
                self.moves+=1
        except:
            self.moves = 0
        '''
        Game.moves+=1
        if (Game.difficulty == 8 or Game.moves == 3):
            self.done = True
            print("Game")

        #print("Score For Move " + str(self.scoreFromAction+self.scoreFromTimers))

        holes = [y for x in(self.holes[0].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[1].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[2].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[3].origEmpty).tolist()for y in x]
        
        peieces = [y for x in(self.chestPieces[0]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[1]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[2]).tolist()for y in x]
        

        #holes = (self.holes[0].origEmpty).tolist()+(self.holes[1].origEmpty).tolist()+(self.holes[2].origEmpty).tolist()+(self.holes[3].origEmpty).tolist()
        #peieces = (self.chestPieces[0]).tolist()+(self.chestPieces[1]).tolist()+(self.chestPieces[2]).tolist()
        counters = [self.holes[0].counterForWiggle,self.holes[1].counterForWiggle,self.holes[2].counterForWiggle,self.holes[3].counterForWiggle]
        self.observation = holes+peieces+counters

        cv2.imshow('Hole0-A',self.holes[0].showHole())
        cv2.imshow('Hole1-A',self.holes[1].showHole())
        cv2.imshow('Hole2-A',self.holes[2].showHole())
        cv2.imshow('Hole3-A',self.holes[3].showHole())
        
        temp = self.showChest()

        cv2.imshow('P0-A',temp[0])
        cv2.imshow('P1-A',temp[1])
        cv2.imshow('P2-A',temp[2])

        cv2.moveWindow('Hole0-A', 100+800,50)
        cv2.moveWindow('Hole1-A', 500+800,50)
        cv2.moveWindow('Hole2-A', 100+800,500)
        cv2.moveWindow('Hole3-A', 500+800,500)
        cv2.moveWindow('P0-A', 150+800,800)
        cv2.moveWindow('P1-A', 300+800,800)
        cv2.moveWindow('P2-A', 450+800,800)

        print(self.scoreFromAction+self.scoreFromTimers)
        print(action)
        cv2.waitKey(0)
        
        
        return np.array([int(i) for i in self.observation]), self.scoreFromAction+self.scoreFromTimers, self.done,False


    #Hole(1,Game.difficulty)
    #self.holes[0].genHole()

    def checkHoles(self):
        holesLeft = Game.holesPerDifficulty[Game.difficulty] - Game.holesGenerated
        if (Game.holesPerDifficulty[Game.difficulty] - Game.holesGenerated > -1):
            if (((self.holes[1].solved and self.holes[2].solved and self.holes[3].solved) and (holesLeft>2)) == True):
                #move 0 to 3
                self.holes[3] = copy.deepcopy(self.holes[0])
                #genNewHoles
                self.holes[0].genHole()
                self.holes[1].genHole()
                self.holes[2].genHole()
                Game.holesGenerated += 3
            elif (((self.holes[0].solved and self.holes[2].solved and self.holes[3].solved) and (holesLeft>2)) == True):
                #move 1 to 2
                self.holes[2] = copy.deepcopy(self.holes[1])
                #genNewHoles
                self.holes[0].genHole()
                self.holes[1].genHole()
                self.holes[3].genHole()
                Game.holesGenerated += 3
            elif (((self.holes[0].solved and self.holes[1].solved and self.holes[3].solved) and (holesLeft>2)) == True):
                #move 2 to 1
                self.holes[1] = copy.deepcopy(self.holes[2])
                #genNewHoles
                self.holes[0].genHole()
                self.holes[3].genHole()
                self.holes[2].genHole()
                Game.holesGenerated += 3
            elif (((self.holes[0].solved and self.holes[1].solved and self.holes[2].solved) and (holesLeft>2)) == True):
                #move 3 to 0
                self.holes[0] = copy.deepcopy(self.holes[3])
                #genNewHoles
                self.holes[3].genHole()
                self.holes[1].genHole()
                self.holes[2].genHole()
                Game.holesGenerated += 3
            elif (((self.holes[0].solved and self.holes[1].solved) and (holesLeft>1)) == True):
                #move 2/3 to 0/1
                self.holes[0] = copy.deepcopy(self.holes[2])
                self.holes[1] = copy.deepcopy(self.holes[3])
                #genNewHoles
                self.holes[2].genHole()
                self.holes[3].genHole()
                Game.holesGenerated += 2
            elif (((self.holes[2].solved and self.holes[3].solved) and (holesLeft>1)) == True):
                #move 2/3 to 0/1
                self.holes[2] = copy.deepcopy(self.holes[0])
                self.holes[3] = copy.deepcopy(self.holes[1])
                #genNewHoles
                self.holes[0].genHole()
                self.holes[1].genHole()
                Game.holesGenerated += 2
            elif (((self.holes[0].solved and self.holes[2].solved) and (holesLeft>1)) == True):
                #move 0/2 to 1/3
                self.holes[0] = copy.deepcopy(self.holes[1])
                self.holes[2] = copy.deepcopy(self.holes[3])
                #genNewHoles
                self.holes[0].genHole()
                self.holes[2].genHole()
                Game.holesGenerated += 2
            elif (((self.holes[1].solved and self.holes[3].solved) and (holesLeft>1)) == True):
                #move 1/3 to 0/2
                self.holes[1] = copy.deepcopy(self.holes[0])
                self.holes[3] = copy.deepcopy(self.holes[2])
                #genNewHoles
                self.holes[1].genHole()
                self.holes[3].genHole()
                Game.holesGenerated += 2
            elif ((self.holes[0].solved and self.holes[1].solved) == True):
                self.holes[0] = copy.deepcopy(self.holes[2])
                self.holes[1] = copy.deepcopy(self.holes[3])
                #genNewHole
                self.holes[2].genHole()
                Game.holesGenerated += 1
            elif ((self.holes[2].solved and self.holes[3].solved) == True):
                self.holes[2] = copy.deepcopy(self.holes[0])
                self.holes[3] = copy.deepcopy(self.holes[1])
                #genNewHole
                self.holes[0].genHole()
                Game.holesGenerated += 1
            elif ((self.holes[0].solved and self.holes[2].solved) == True):
                #move 0/2 to 1/3
                self.holes[0] = copy.deepcopy(self.holes[1])
                self.holes[2] = copy.deepcopy(self.holes[3])
                #genNewHole
                self.holes[0].genHole()
                Game.holesGenerated += 1
            elif ((self.holes[1].solved and self.holes[3].solved) == True):
                #move 1/3 to 0/2
                self.holes[1] = copy.deepcopy(self.holes[0])
                self.holes[3] = copy.deepcopy(self.holes[2])
                #genNewHoles
                self.holes[1].genHole()
                Game.holesGenerated += 1
        else:
            Game.difficulty+=1
            Game.holesGenerated=0
            self.__init__()

            
    def step(self,action):

        [hole,peiecePick,x,y,xRots,zTrue]=action
        
        temp = self.putPeiece(hole,peiecePick,x,y,xRots,zTrue)
        self.scoreFromAction = temp
        
        if (not(temp == -400.34)):
            self.chestPieces[peiecePick]=self.getRandPeiece()
            for x in range(3):
                if x == hole:
                    continue
                self.scoreFromTimers = self.holes[x].upCounterForWiggle()

        self.checkHoles()
        '''
        try:
            if (self.moves == 5000):
                self.done = True
                #print("Game")
            else:
                self.moves+=1
        except:
            self.moves = 0
        '''
        Game.moves+=1
        if (Game.difficulty == 8 or Game.moves == 2):
            self.done = True
            #print("Game")

        #print("Score For Move " + str(self.scoreFromAction+self.scoreFromTimers))

        holes = [y for x in(self.holes[0].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[1].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[2].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[3].origEmpty).tolist()for y in x]
        
        peieces = [y for x in(self.chestPieces[0]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[1]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[2]).tolist()for y in x]
        

        #holes = (self.holes[0].origEmpty).tolist()+(self.holes[1].origEmpty).tolist()+(self.holes[2].origEmpty).tolist()+(self.holes[3].origEmpty).tolist()
        #peieces = (self.chestPieces[0]).tolist()+(self.chestPieces[1]).tolist()+(self.chestPieces[2]).tolist()
        counters = [self.holes[0].counterForWiggle,self.holes[1].counterForWiggle,self.holes[2].counterForWiggle,self.holes[3].counterForWiggle]
        self.observation = holes+peieces+counters
        
        return np.array([int(i) for i in self.observation]), self.scoreFromAction+self.scoreFromTimers, self.done,False

    def render(self,holes,chestPieces):
        print("Board/Cheststate")
    
    def reset(self):
        Game.difficulty = 2
        self.__init__()
        holes = [y for x in(self.holes[0].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[1].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[2].origEmpty).tolist()for y in x]
        holes = holes+[y for x in(self.holes[3].origEmpty).tolist()for y in x]
        
        peieces = [y for x in(self.chestPieces[0]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[1]).tolist()for y in x]
        peieces = peieces+[y for x in(self.chestPieces[2]).tolist()for y in x]
        

        #holes = (self.holes[0].origEmpty).tolist()+(self.holes[1].origEmpty).tolist()+(self.holes[2].origEmpty).tolist()+(self.holes[3].origEmpty).tolist()
        #peieces = (self.chestPieces[0]).tolist()+(self.chestPieces[1]).tolist()+(self.chestPieces[2]).tolist()
        counters = [self.holes[0].counterForWiggle,self.holes[1].counterForWiggle,self.holes[2].counterForWiggle,self.holes[3].counterForWiggle]
        self.observation = holes+peieces+counters
        
        return np.array([int(i) for i in self.observation])

        


class Hole:
    EmptyCompare = np.array([ [False,False,False,False,False],
                              [False,False,False,False,False],
                              [False,False,False,False,False],
                              [False,False,False,False,False],
                              [False,False,False,False,False]])

    ###

    PutForCompare =np.array([[True,True,True,True,True],
                  [True,False,False,False,True],
                  [True,False,False,False,True],
                  [True,False,False,False,True],
                  [True,True,True,True,True]])
    
    ### puzzz vars
    MINSIZE = 4
    STARTSIZE = 6
    MAXSIZE = 14
    MAXWIDTH = 10
    MAXHEIGHT = 10
    MAXHOLENEGLECT = 8
    MAXPUTTYFILL = 5
    MAXKNOCKOUTS = 3
    KNOCKOUTPENALTY = 2
    MINROWS = [ -1, -1, -1, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7 ]
    MAXROWS = [ -1, -1, -1, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 10, 10 ]

    ###SCORES###
    perfectPlace = 800
    fudgedPlace = -200
    couldNotPlace = -400.34
    hole_masterpiece = 300
    hole_craftsmanship = 250
    hole_fair_job = 200
    hole_sloppy_work = 150
    hole_pigs_breakfast = 100
    flyOff = -200
    
    
    def __init__(self,holeId,difficulty):
        self.holeId = holeId
        self.difficulty = difficulty
        self.holesGenerated = 0
        self.counterForWiggle = 0
        self.peiecesUsed=0

    def placePeiece(self,peiece,xPlaced,yPlaced):
        #tester = copy.deepcopy(self.origEmpty)
        
        if (self.solved == True):
            #print("SOLVED")
            return Hole.couldNotPlace
        #check for putty here
        putty=False
        if np.array_equal(peiece,Hole.PutForCompare):
            #print("PUTTY PEIECE")#@
            putty=True
            if (self.origEmpty[xPlaced-1][yPlaced-1] == False):
                #print("PUTTY BAD")
                return Hole.couldNotPlace
            boardArea = []
            for x in range(5):
                for y in range(5):
                    try:
                        boardArea.append((self.origEmpty[yPlaced+x-2][xPlaced+y-2]))
                    except:
                        boardArea.append(False)
            boardAreaNp = np.array(boardArea)
            boardAreaNp = boardAreaNp.reshape(5,5)
            img_labeled = measure.label(boardAreaNp, connectivity=1)
            middle = img_labeled[2][2]
            tempy=0
            tempx=0
            count = 0
            for row in img_labeled:
                for el in row:
                    if el == 2:
                        img_labeled[tempy][tempx]=True
                    else:
                        img_labeled[tempy][tempx]=False
                    tempx += 1
                tempy += 1
                tempx = 0


            if (count>5):
                #print("PUTTY BAD 2")
                return Hole.couldNotPlace
            peiece = img_labeled.astype(bool)

        #check if piece falls off more than 1 square
        yMax,xMax = self.origEmpty.shape
        if (putty == False):
            for y in range(5):
                if any(peiece[:,y]):
                    west = 1-y
                    break
            for y in reversed(range(5)):
                if any(peiece[:,y]):
                    east = y-2
                    break
                
            if (xPlaced+east>xMax):
                #print("OutOfBoundsEast")#@
                return Hole.couldNotPlace
            elif(xPlaced-west<0):
                #print("OutOfBoundsWest")#@
                return Hole.couldNotPlace

        #check if all peieces are undneath

        placeable = []
        for x in range(5):
            for y in range(5):
                if (peiece[x][y] == True):
                    try:
                        placeable.append(self.origEmpty[yPlaced+x-2][xPlaced+y-2])
                    except:
                        placeable.append(False)
                    '''
                    #print("LookingAT",str(xPlaced+y-2),str(yPlaced+x-2))
                    if (((xPlaced+y-2) < 0) or ((yPlaced+x-2) < 0)):
                        pass
                    else:
                        try:
                            placeable.append((self.origEmpty[yPlaced+x-2][xPlaced+y-2]))
                        except:
                            pass
                    '''


        if (any(placeable) == False):
            #print("TryinaPlaceOverBoards")#@
            #print(Hole.couldNotPlace)
            return Hole.couldNotPlace

        #add final detect for surronding peieces #flip board @
        #make compare matrix...

        compare = copy.deepcopy(Hole.EmptyCompare)

        for x in range(5):
            for y in range(5):
                if (peiece[x][y] == True):
                    try:
                        compare[x+1][y] = True
                    except:
                        pass
                    try:
                        compare[x-1][y] = True
                    except:
                        pass
                    try:
                        compare[x][y+1] = True
                    except:
                        pass
                    try:
                        compare[x][y-1] = True
                    except:
                        pass

        for x in range(5):
            for y in range(5):
                if (peiece[x][y] == True):
                    compare[x][y] = False

        placeable2 = []
        for x in range(5):
            for y in range(5):
                if (compare[x][y] == True):
                    #print("LookingAT",str(xPlaced+y-2),str(yPlaced+x-2))
                    if (((xPlaced+y-2) < 0) or ((yPlaced+x-2) < 0)):
                        placeable2.append(False)
                    else:
                        try:
                            placeable2.append((self.origEmpty[yPlaced+x-2][xPlaced+y-2]))
                        except:
                            placeable2.append(False)

        
        if(all(placeable2)==True):
            #print("No Peiece Around")#@
            return Hole.couldNotPlace
                    
        #print("PLACED")#@

        
        self.counterForWiggle = 0
        self.peiecesUsed += 1
        self.lastPlaced = copy.deepcopy(peiece)
        self.lastx = xPlaced
        self.lasty = yPlaced
        self.lastBoard = copy.deepcopy(self.origEmpty)

        for x in range(5):
            for y in range(5):
                if (peiece[x][y] == True):
                    try:
                        self.origEmpty[yPlaced+x-2][xPlaced+y-2] = False
                    except:
                        pass
        temp = []

        '''
        if np.array_equal(tester,self.origEmpty) :
            print(self.origEmpty)
            print(peiece)
            print(xPlaced,yPlaced)
            print("Small Prob")
            input()
        '''
        
        for y in range(yMax):
            for x in range(xMax):
                temp.append(self.origEmpty[y][x])
        
        if any(temp) == False:
            #print("Hole " + str(self.holeId) + " complete")#@
            nominalPeieces = self.holeSquares/5
            if (nominalPeieces - self.peiecesUsed == 0):
                other = Hole.hole_masterpiece
            elif (nominalPeieces - self.peiecesUsed == -1):
                other = Hole.hole_craftsmanship
            elif (nominalPeieces - self.peiecesUsed == -2):
                other = Hole.hole_fair_job
            elif (nominalPeieces - self.peiecesUsed == -3):
                other = Hole.hole_sloppy_work
            else:
                other = Hole.hole_pigs_breakfast
            self.solved = True
                
        else:
            other = 0
        
        if len(placeable) == 5:
            if (all(placeable)or putty) == True:
                #work out possible adjacent sides
                forCompare = np.zeros((7,7))

                for y in range(5):
                    for x in range(5):
                        if (peiece[x][y] == True):
                            forCompare[x][y+1] = True
                            forCompare[x+2][y+1] = True
                            forCompare[x+1][y] = True
                            forCompare[x+1][y+2] = True       
                                
                for x in range(5):
                    for y in range(5):
                        if (peiece[x][y] == True):
                            forCompare[x+1][y+1] = False
                            

                nextTo = []
                for x in range(7):
                    for y in range(7):
                        if (forCompare[x][y] == True):
                            try:
                                nextTo.append(not(self.origEmpty[yPlaced+x-3][xPlaced+y-3]))
                            except:
                                nextTo.append(True)
                count = 0
                
                for x in nextTo:
                    if x == True:
                        count +=1
                
                return Hole.perfectPlace * (count/(len(nextTo))) + other

        forscore = 0
        for test in placeable:
            if test == True:
                forscore+=1

        forscore= (5-forscore)/5
        
        return forscore * Hole.fudgedPlace + other

    def removePeiece(self):
        self.origEmpty = copy.deepcopy(self.lastBoard)

    def punchEdge(self):
        countx = 0
        county = 0
        try:
            for x in self.empty:
                for y in x:
                    if (self.empty[county][countx] == False):
                        if(self.empty[county+1][countx] == True):
                           self.empty[county][countx] = True
                           self.origEmpty = copy.deepcopy(self.empty)
                           return
                    countx +=1
                countx = 0
                county += 1
        except:
            pass

    def upCounterForWiggle(self):
        if (self.solved == False):
            self.counterForWiggle += 1/8
            if (self.counterForWiggle == 1):
                self.counterForWiggle = 0
                try:
                    self.removePeiece()
                except:
                    self.punchEdge()
                return Hole.flyOff
            return 0
        return 0

    def genHole(self):
        self.solved = False
        maximum = max(4, 6 - self.difficulty)
        i = random.randrange(0,min(14, 6 + self.difficulty) - maximum + 1) + maximum
        j = self.holesGenerated
        self.piecesUsed = 0
        self.countdown = 8
        self.size = i
        self.origHoleSquares = i * 5
        self.height = Hole.MINROWS[i]

        i = Hole.MAXROWS[i] - self.height

        if (i != 0):
            self.height += random.randrange(0,i + 1)

        while(True):
            self.width = int(4 + self.origHoleSquares/self.height - random.randrange(0,2))
            if (self.width > 10):
                self.height += 1
            if(not(self.width > 10)):
                break
            
        if (self.height > 10):
            self.width = 10
            self.height = 10


        self.origEmpty = np.zeros([self.width, self.height], dtype=bool)
        self.empty  = np.zeros([self.width, self.height], dtype=bool)

        for i in range(self.height):
            for j in range(2,self.width - 2):
                self.origEmpty[j][i] = True
        
        self.knockOut(self.origHoleSquares - self.height * (self.width - 4), False)
        self.recreateEmpty()

    def knockOut(self,i,b):
        while(i > 0):
            nextInt = random.randrange(0,self.height);
            if( random.randrange(0,2) == 0 ):
                x = 1
            else:
                x = (self.width - 2)
            
            if(self.origEmpty[x][nextInt]):
                if(x == 1):
                    x -= 1
                else:
                    x += 1
                if(self.origEmpty[x][nextInt]):
                    continue
            if(b):
                pass
            else:
                self.origEmpty[x][nextInt] = True
            i-=1

    def recreateEmpty(self):
        self.holeSquares = self.origHoleSquares         
        self.origEmpty = np.rot90(self.origEmpty)
        self.padHole()
        self.empty = copy.deepcopy(self.origEmpty)

    def showHole(self):
        forShow = []
        for x in range(len(self.origEmpty)):
            for y in range(len(self.origEmpty[x])):
                if self.origEmpty[x][y] == False:
                    forShow.append("X")
                else :
                    forShow.append("O")
        y , x = self.origEmpty.shape
        temp = 0
        show = []
        row = []
        for element in forShow:
            row.append(element)
            temp += 1
            if temp == x:
                show.append(row)
                row = []
                temp = 0
        for element in show:
            #print(element)
            pass
        my_array = self.origEmpty.reshape((y, x)).astype('uint8')*255
        res = cv2.resize(my_array,(x*20,y*20),fx=0, fy=0, interpolation = cv2.INTER_NEAREST)
        xs,ys=res.shape
        for y in range(ys):
            for x in range(xs):
                if ( ((x%20) == 0) or  ((y%20) == 0)):
                    if (res[x][y] == 255):
                        res[x][y]=0
                    else :
                        res[x][y]=255
        #im = Image.fromarray(res)
        im = res            
        #im.show()
        return im

    def padHole(self):
        y,x = self.origEmpty.shape

        def pad_with(vector, pad_width, iaxis, kwargs):
            pad_value = kwargs.get('padder', 10)
            vector[:pad_width[0]] = pad_value
            vector[-pad_width[1]:] = pad_value

        self.origEmpty = np.pad(self.origEmpty, int(x/2), pad_with, padder=False)

        y,x = self.origEmpty.shape

        xToRemove = int((x - 10)/2)
        yToRemove = int((y - 11)/2)

        xUpRange = range(x-xToRemove,x)
        xDownRange = range(0,xToRemove)

        yUpRange = range(y-yToRemove,y)
        yDownRange = range(0,yToRemove)

        self.origEmpty = np.delete(self.origEmpty,xUpRange, axis=1)
        self.origEmpty = np.delete(self.origEmpty,xDownRange, axis=1)

        self.origEmpty = np.delete(self.origEmpty,yUpRange, axis=0)
        self.origEmpty = np.delete(self.origEmpty,yDownRange, axis=0)

        y,x = self.origEmpty.shape

        if x == 11:
            if (random.randrange(0,2)==1):
                self.origEmpty = np.delete(self.origEmpty,-1, axis=1)
            else:
                self.origEmpty = np.delete(self.origEmpty,0, axis=1)

        if y == 12:
            if (random.randrange(0,2)==1):
                self.origEmpty = np.delete(self.origEmpty,-1, axis=0)
            else:
                self.origEmpty = np.delete(self.origEmpty,0, axis=0)
        




PP = Game()
temp = PP.showChest()

cv2.imshow('P0',temp[0])
cv2.imshow('P1',temp[1])
cv2.imshow('P2',temp[2])

cv2.imshow('Hole0',PP.holes[0].showHole())

cv2.waitKey(1)

pick= int(input("Peiece"))
x= int(input("X"))
y= int(input("Y"))
xRots= int(input("xRots"))
zTrue= int(input("zRot"))
peiece = PP.chestPieces[pick]
print("Score " + str(PP.putPeiece(0,pick,x,y,xRots,zTrue)))
cv2.imshow('HoleTest',PP.holes[0].showHole())
cv2.waitKey(1)

input()

'''       
PP.holes[0].showHole()
'''
