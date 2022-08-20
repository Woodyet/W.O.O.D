import numpy as np
import Start as solve
import random

P1 = np.array([[255,255,255,255,255],
              [255,0,0,255,255],
              [255,0,0,0,255],
              [255,255,255,255,255],
              [255,255,255,255,255]])
P2 = np.rot90(P1)
P3 = np.rot90(P2)
P4 = np.rot90(P3)
P5 = np.fliplr(P1)
P6 = np.rot90(P5)
P7 = np.rot90(P6)
P8 = np.rot90(P7)

P = [P1,P2,P3,P4,P5,P6,P7,P8]

F1 = np.array([[255,255,255,255,255],
              [255,255,0,0,255],
              [255,0,0,255,255],
              [255,255,0,255,255],
              [255,255,255,255,255]])
F2 = np.rot90(F1)
F3 = np.rot90(F2)
F4 = np.rot90(F3)
F5 = np.fliplr(F1)
F6 = np.rot90(F5)
F7 = np.rot90(F6)
F8 = np.rot90(F7)

F = [F1,F2,F3,F4,F5,F6,F7,F8]

Y1 = np.array([[255,255,255,255,255],
              [255,255,255,255,255],
              [255,0,0,0,0],
              [255,255,0,255,255],
              [255,255,255,255,255]])
Y2 = np.rot90(Y1)
Y3 = np.rot90(Y2)
Y4 = np.rot90(Y3)
Y5 = np.fliplr(Y1)
Y6 = np.rot90(Y5)
Y7 = np.rot90(Y6)
Y8 = np.rot90(Y7)

Y = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8]

L1 = np.array([[255,255,255,255,255],
              [255,255,255,255,255],
              [255,0,0,0,0],
              [255,0,255,255,255],
              [255,255,255,255,255]])
L2 = np.rot90(L1)
L3 = np.rot90(L2)
L4 = np.rot90(L3)
L5 = np.fliplr(L1)
L6 = np.rot90(L5)
L7 = np.rot90(L6)
L8 = np.rot90(L7)

L = [L1,L2,L3,L4,L5,L6,L7,L8]

N1 = np.array([[255,255,255,255,255],
              [255,0,0,255,255],
              [255,255,0,0,0],
              [255,255,255,255,255],
              [255,255,255,255,255]])
N2 = np.rot90(N1)
N3 = np.rot90(N2)
N4 = np.rot90(N3)
N5 = np.fliplr(N1)
N6 = np.rot90(N5)
N7 = np.rot90(N6)
N8 = np.rot90(N7)

N = [N1,N2,N3,N4,N5,N6,N7,N8]

I1 = np.array([[255,255,255,255,255],
              [255,255,255,255,255],
              [0,0,0,0,0],
              [255,255,255,255,255],
              [255,255,255,255,255]])
I2 = np.rot90(I1)

I = [I1,I2]

T1 = np.array([[255,255,0,255,255],
              [255,255,0,255,255],
              [255,0,0,0,255],
              [255,255,255,255,255],
              [255,255,255,255,255]])
T2 = np.rot90(T1)
T3 = np.rot90(T2)
T4 = np.rot90(T3)

T = [T1,T2,T3,T4]

W1 = np.array([[255,255,255,255,255],
              [255,0,255,255,255],
              [255,0,0,255,255],
              [255,255,0,0,255],
              [255,255,255,255,255]])
W2 = np.rot90(W1)
W3 = np.rot90(W2)
W4 = np.rot90(W3)

W = [W1,W2,W3,W4]

U1 = np.array([[255,255,255,255,255],
              [255,0,255,0,255],
              [255,0,0,0,255],
              [255,255,255,255,255],
              [255,255,255,255,255]])
U2 = np.rot90(U1)
U3 = np.rot90(U2)
U4 = np.rot90(U3)

U = [U1,U2,U3,U4]

V1 = np.array([[255,255,0,255,255],
              [255,255,0,255,255],
              [255,255,0,0,0],
              [255,255,255,255,255],
              [255,255,255,255,255]])
V2 = np.rot90(V1)
V3 = np.rot90(V2)
V4 = np.rot90(V3)

V = [V1,V2,V3,V4]

Z1 = np.array([[255,255,255,255,255],
              [255,0,0,255,255],
              [255,255,0,255,255],
              [255,255,0,0,255],
              [255,255,255,255,255]])
Z2 = np.rot90(Z1)
Z3 = np.rot90(Z2)
Z4 = np.rot90(Z3)
Z5 = np.fliplr(Z1)
Z6 = np.rot90(Z5)
Z7 = np.rot90(Z6)
Z8 = np.rot90(Z7)

Z = [Z1,Z2,Z5,Z6]

X = [np.array([[255,255,255,255,255],
              [255,255,0,255,255],
              [255,0,0,0,255],
              [255,255,0,255,255],
              [255,255,255,255,255]])]


PUT = [np.array([[255,0,0,255,255],
               [255,0,0,255,255],
               [255,0,0,255,255],
               [255,0,0,255,255],
               [255,0,0,255,255]])]

allRots = [P,F,Y,L,N,T,U,V,W,Z,X,I]

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

BASESHAPES = BASESHAPES1 + BASESHAPES2 + BASESHAPES3 + BASESHAPES4 + BASESHAPES5 + BASESHAPES6 + BASESHAPES7

'''
#base_shape_variations = {shape: solve.variation(shape) for shape, name in BASESHAPES}

def bringToFront(inlist,pos): 
    inlist.insert(0, inlist.pop(pos))
    return inlist

for item in BASESHAPES:
    print(item)

pos = 0
for stuff1,stuff2 in BASESHAPES:
    if (stuff2[0] == "W"):                  #for items in toolsbox #break on find 
        BASESHAPES = bringToFront(BASESHAPES,pos)
    pos+=1

print()

for item in BASESHAPES:
    print(item)
'''
