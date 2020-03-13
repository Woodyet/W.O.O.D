#make holes
import random

random.randint(1,5)

SET = None

MIN_ROWS = SET
MAX_ROWS = SET
hole = []
difficulty = 2
lowerBound = max(4,6-difficulty)
higherBound = min(14,6+difficulty)

lowerBound += random.randint(0,higherBound-lowerBound+1)

def Hole (size,random?,holeID):
    origHoleSquares = size*5
    height = MIN_ROWS[size]
    if ( (size = MAX_ROWS[size] - height) != 0 ):
        height += random.randint(0, size + 1)
    while(True):
        width = 4 + origHoleSquares / height - random.randint(0,2)
        if (width > 10):
            height += 1
        if (width > 10):
            pass
        else:
            break
    if (height > 10):
        width = 10
        height = 10

    origEmpty = numpy.ones((width, height), dtype=bool)
    empty = numpy.ones((width, height), dtype=bool)

    for x in range(height):
        for y in range(width-2):
            origEmpty[y,x] = True

    knockOut(origHoleSquares - height * (width - 4), Randint, false)

def knockOut(A,B,C):
    pass
