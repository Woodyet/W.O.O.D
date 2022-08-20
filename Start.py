
import random

def reset(positions):
    """

    This is used for setup before starting the search
    Moves the shape's position so that the top left square is at (0, 0)

    """

    min_x, min_y = min(positions, key=lambda x:x[::-1])

    return tuple(sorted((x-min_x, y-min_y) for x, y in positions))

def variation(positions):
    """
  
    This is used for setup before starting the search
    Returns unique rotations and reflections of the shape

    """

    return list({reset(var) for var in (
        positions,

        [(-y,  x) for x, y in positions], # Anti-clockwise 90
        [(-x, -y) for x, y in positions], # 180
        [( y, -x) for x, y in positions], # Clockwise 90

        #[(-x,  y) for x, y in positions], # Mirror vertical
        #[(-y, -x) for x, y in positions], # Mirror diagonal
        [( x, -y) for x, y in positions], # Mirror horizontal
        [(y,  x) for x, y in positions], # Mirror Anti-clockwise 90
        [(-x, y) for x, y in positions], # Mirror 180
        [( -y, -x) for x, y in positions], # Mirror Clockwise 90
        
        
    )})
'''
shapes = [
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P1"),#"P"),
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P2"),#"P"),
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P3"),#"P"),
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P4"),#"P"),
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P5"),#"P"),
    (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P6"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P7"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P8"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P9"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P10"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P11"),#"P"),
    #(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P12"),#"P"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F1"),#"F"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F2"),#"F"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F3"),#"F"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F4"),#"F"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F5"),#"F"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F6"),#"F"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F7"),#"F"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y1"),#"Y"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y2"),#"Y"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y3"),#"Y"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y4"),#"Y"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y5"),#"Y"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y6"),#"Y"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y7"),#"Y"),
    (((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), "L1"),#"L"),
    (((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), "L2"),#"L"),
    (((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), "L3"),#"L"),
    #(((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), "L4"),#"L"),
    (((0, 2), (0, 3), (1, 0), (1, 1), (1, 2)), "N1"),#"N"),
    (((0, 2), (0, 3), (1, 0), (1, 1), (1, 2)), "N2"),#"N"),
    #(((0, 2), (0, 3), (1, 0), (1, 1), (1, 2)), "N3"),#"N"),
    (((0, 0), (1, 0), (1, 1), (1, 2), (2, 0)), "T1"),#"T"),
    (((0, 0), (1, 0), (1, 1), (1, 2), (2, 0)), "T2"),#"T"),
    #(((0, 0), (1, 0), (1, 1), (1, 2), (2, 0)), "T3"),#"T"),
    #(((0, 0), (1, 0), (1, 1), (1, 2), (2, 0)), "T4"),#"T"),
    (((0, 0), (0, 1), (1, 1), (2, 0), (2, 1)), "U1"),#"U"),
    #(((0, 0), (0, 1), (1, 1), (2, 0), (2, 1)), "U2"),#"U"),
    (((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)), "V1"),#"V"),
    #(((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)), "V2"),#"V"),
    (((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)), "W1"),#"W"),
    #(((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)), "W2"),#"W"),
    (((0, 0), (1, 0), (1, 1), (1, 2), (2, 2)), "Z1"),#"Z"),
    #(((0, 0), (1, 0), (1, 1), (1, 2), (2, 2)), "Z2"),#"Z"),
    (((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)), "X1"),#"X"),
    #(((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)), "X2"),#"X"),
    (((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)), "I1")#"I")
]

random.shuffle(shapes)

'''
BASESHAPES1 = [(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P1")]
    
BASESHAPES2 = [(((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F1"),#18
               (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y1")]#25

BASESHAPES3 = [(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P2")]
    
BASESHAPES4 = [(((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), "L1"),#29
               (((0, 2), (0, 3), (1, 0), (1, 1), (1, 2)), "N1"),#35
               (((0, 0), (1, 0), (1, 1), (1, 2), (2, 0)), "T1")]#39

BASESHAPES5 = [(((0, 1), (1, 0), (1, 1), (1, 2), (2, 0)), "F2"),
               (((0, 1), (1, 0), (1, 1), (1, 2), (1, 3)), "Y2"),
               (((0, 0), (0, 1), (1, 1), (2, 0), (2, 1)), "U1"),#41
               (((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)), "V1"),#43
               (((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)), "W1"),#45
               (((0, 0), (1, 0), (1, 1), (1, 2), (2, 2)), "Z1")]#47

BASESHAPES6 = [(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1)), "P3")]
                                                 
BASESHAPES7 = [(((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)), "X1"),#49
               (((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)), "I1")]#50

random.shuffle(BASESHAPES2)
random.shuffle(BASESHAPES4)
random.shuffle(BASESHAPES5)
random.shuffle(BASESHAPES7)

shapes = BASESHAPES1 + BASESHAPES2 + BASESHAPES3 + BASESHAPES4 + BASESHAPES5 + BASESHAPES6 + BASESHAPES7


from range_key_dict import RangeKeyDict
pieceDict = RangeKeyDict({
                                (0,22):"P",
                                (22,36):"F",
                                (36,50):"Y",
                                (50,58):"L",
                                (58,66):"N",
                                (66,73):"T",
                                (73,77):"U",
                                (77,81):"V",
                                (81,85):"W",
                                (85,89):"Z",
                                (89,92):"X",
                                (92,94):"I",
                                })


shape_variations = {shape: variation(shape) for shape, name in shapes}

def pprintn(grid, size, transpose=False):
    """

    Function to print the grid in a nice format

    """

    width, height = size

    for x in range(width):
        for y in range(height):
            if grid[(x, y)] == " ":
                grid[(x, y)] = "  "
            if grid[(x, y)] == "M":
                grid[(x, y)] = "MM"
        
    
    if transpose:
        for x in range(width):
            print("".join([grid[(x, y)] for y in range(height)]))
    else:
        for y in range(height):
            print("".join([grid[(x, y)] for x in range(width)]))

def pprint(grid, size, transpose=False):
    """

    Function to print the grid in a nice format

    """

    width, height = size
    if transpose:
        for x in range(width):
            print("".join([grid[(x, y)] for y in range(height)]))
    else:
        for y in range(height):
            print("".join([grid[(x, y)] for x in range(width)]))

def solveSpecShapes(grid, size, available_shapes, spec_shapes, start=0):
    """

    Recursive function that yields completed/solved grids
    Max recursion depth is width*height//5+1

    """

    width, height = size

    # Traverse the grid left to right, then top to bottom like reading a book
    # Look for next open space (".")
    for i in range(start, width*height):
        y, x = divmod(i, width)
        if grid[(x, y)] == ".":
            for shape, name in available_shapes:
                # Check each rotation and reflection of shape
                for shape_var in spec_shapes[shape]:
                    if all(grid.get((x+xs, y+ys)) == "." for xs, ys in shape_var):
                        temp_grid = grid.copy()
                        temp_shapes = available_shapes.copy()
                        for xs, ys in shape_var:
                            temp_grid[(x+xs, y+ys)] = name
                        temp_shapes.remove((shape, name))

                        yield from solveSpecShapes(temp_grid, size, temp_shapes, spec_shapes, i+1)
            
            return # No more shapes are found, let previous recursion continue
    # yield final grid when all grid values have been checked
    yield grid

def solve(grid, size, available_shapes, start=0):
    """

    Recursive function that yields completed/solved grids
    Max recursion depth is width*height//5+1

    """

    width, height = size

    random.shuffle(BASESHAPES2)
    random.shuffle(BASESHAPES4)
    random.shuffle(BASESHAPES5)
    random.shuffle(BASESHAPES7)

    shapes = BASESHAPES1 + BASESHAPES2 + BASESHAPES3 + BASESHAPES4 + BASESHAPES5 + BASESHAPES6 + BASESHAPES7
    shape_variations = {shape: variation(shape) for shape, name in shapes}

    # Traverse the grid left to right, then top to bottom like reading a book
    # Look for next open space (".")
    for i in range(start, width*height):
        y, x = divmod(i, width)
        if grid[(x, y)] == ".":
            for shape, name in available_shapes:
                # Check each rotation and reflection of shape
                for shape_var in shape_variations[shape]:
                    if all(grid.get((x+xs, y+ys)) == "." for xs, ys in shape_var):
                        temp_grid = grid.copy()
                        temp_shapes = available_shapes.copy()
                        for xs, ys in shape_var:
                            temp_grid[(x+xs, y+ys)] = name
                        temp_shapes.remove((shape, name))

                        yield from solve(temp_grid, size, temp_shapes, i+1)
            return # No more shapes are found, let previous recursion continue
    # yield final grid when all grid values have been checked
    yield grid 

from time import time
import copy
from operator import itemgetter

def find(width, height, holes=[], gimmieSol=0):
    """

    Program is faster when width is less than height
    if width is greater than height, swap them around

    Iterate over solve() for more solutions

    """
    t = time()
    #print(width, height, *holes)

    grid = {(x, y):"." for x in range(width) for y in range(height)}    
    for hole in holes:
        for x, y in holes:
            grid[(x, y)] = " "
    #pprint(grid, (width, height))

    #print()

    newgrid = copy.deepcopy(grid)

    trim = 1
    trimAmount = 2*trim
    heightTrimmed = height-trimAmount
    widthTrimmed = width-trimAmount
    '''
    #removes middle (better for stratgy) but can leave blocks
    #alone resulting in an unsolved puzzle
    for y in range(heightTrimmed):
        for x in range(widthTrimmed):
            if(x == 0 or x == widthTrimmed-1):
                pass
            elif(y == 0 or y == heightTrimmed-1):
                pass
            else:
                if(grid[(x-1, y-1)] == " " or grid[(x+1, y-1)] == " " or grid[(x-1, y+1)] == " " or grid[(x+1, y+1)] == " " or grid[(x, y)] == " "):
                    pass
                else:
                    newgrid[(x+trim, y+trim)] = "T"
                
    #pprint(newgrid, (width, height))
    
    #make sure mutiple of 5 have been removed
    count = 0
    for y in range(heightTrimmed):
        for x in range(widthTrimmed):
            if newgrid[(x, y)] == "T":
                count +=1

    count = count%5

    #print(count)

    holeCountOnT = []

    for y in range(heightTrimmed):
        for x in range(widthTrimmed):
            if newgrid[(x, y)] == "T":
                _count = 0
                for i in range(-trimAmount,trimAmount+1):
                    for j in range(-trimAmount,trimAmount+1):
                        if (newgrid[(x+i, y+j)]== " "):
                            _count += 1
                if _count > 0:
                    holeCountOnT.append([x,y,_count])

    holeCountOnT = sorted(holeCountOnT, key=itemgetter(2))[::-1]

    for item in holeCountOnT:
        count -= 1
        if count < 0:
            break
        x, y, _ = item
        newgrid[(x, y)] = "."

    x = trimAmount
    y = trimAmount
    while count > 0 :
        if newgrid[(x, y)] == "T":
            newgrid[(x, y)] = "."
            count -= 1
        x+=1
        if (x == widthTrimmed):
            x = trimAmount
            y+=1

    for y in range(heightTrimmed):
        for x in range(widthTrimmed):
            if newgrid[(x, y)] == "T":
                newgrid[(x, y)] = " "
                    
    
    #pprint(newgrid, (width, height))
    '''
    grid = copy.deepcopy(newgrid)
    
    #print("DONE2")
    #print("DONE5")
    temp = 0
    for solution in solve(grid, (width, height), shapes):
        if gimmieSol != temp:
            temp += 1
            continue
        #pprintn(solution, (width, height))
        #print("DONE6")
        remove=[]
        for y in range(height):
            for x in range(width):
                temp=""
                try:
                    temp+=solution[(x+1, y)]
                    temp+=solution[(x-1, y)]
                    temp+=solution[(x, y+1)]
                    temp+=solution[(x, y-1)]
                    if(temp.find(" ") != -1):
                        pass
                    else:
                        remove.append(solution[(x, y)])
                except:
                    pass
        VALUETOCOUNT = list( dict.fromkeys(remove) )
        actRem = []
        for item in VALUETOCOUNT:
            if (remove.count(item) == 5):
                actRem.append(item)

        for y in range(height):
            for x in range(width):
                for item in actRem:
                    if(solution[(x, y)] == item):
                        solution[(x, y)] = " "
        pprintn(solution, (width, height))
        print(f"{time()-t:.3f}s\n")
        return solution
    else:
        pprint(grid, (width, height))
        print("No solution")
        print(f"{time()-t:.3f}s\n")
        return False


def findSpecShapes(width, height, spec_shapes, findWith, holes=[]):
    """

    Program is faster when width is less than height
    if width is greater than height, swap them around

    Iterate over solve() for more solutions

    """
    t = time()
    #print(width, height, *holes)

    grid = {(x, y):"." for x in range(width) for y in range(height)}    
    for hole in holes:
        for x, y in holes:
            grid[(x, y)] = " "
    #pprint(grid, (width, height))

    #print()

    newgrid = copy.deepcopy(grid)

    trim = 1
    trimAmount = 2*trim
    heightTrimmed = height-trimAmount
    widthTrimmed = width-trimAmount
    
    grid = copy.deepcopy(newgrid)
    
    
    for solution in solveSpecShapes(grid, (width, height), shapes, spec_shapes):
        found = [False,False,False]
        for key in solution:
            temp = 0
            for contains in findWith:
                if solution[key][0] == contains:
                    found[temp] = True
                    temp += 1

        if any(found) != True:
            continue
                            
        remove=[]
        for y in range(height):
            for x in range(width):
                temp=""
                try:
                    temp+=solution[(x+1, y)]
                    temp+=solution[(x-1, y)]
                    temp+=solution[(x, y+1)]
                    temp+=solution[(x, y-1)]
                    if(temp.find(" ") != -1):
                        pass
                    else:
                        remove.append(solution[(x, y)])
                except:
                    pass
        VALUETOCOUNT = list( dict.fromkeys(remove) )
        actRem = []
        for item in VALUETOCOUNT:
            if (remove.count(item) == 5):
                actRem.append(item)

        for y in range(height):
            for x in range(width):
                for item in actRem:
                    if(solution[(x, y)] == item):
                        solution[(x, y)] = " "
        pprintn(solution, (width, height))
        print(f"{time()-t:.3f}s\n")
        return solution
    else:
        pprint(grid, (width, height))
        print("No solution")
        print(f"{time()-t:.3f}s\n")
        return False


