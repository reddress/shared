# current standings 18/06/14
# BRA 4
# MEX 4
# CAM 0
# CRO 0

class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def __str__(self):
        return "%s %s" % (self.name, self.points)

def matchup(left, right, winner):
    # left wins: -1, tie: 0, right wins: 1
    if winner == -1:
        left.points += 3
        print("%s def. %s" % (left.name, right.name))
    elif winner == 0:
        left.points += 1
        right.points += 1
        print("%s ties %s" % (left.name, right.name))
    elif winner == 1:
        right.points += 3
        print("%s def. %s" % (right.name, left.name))
    else:
        print("UNKNOWN RESULT")

def setup():
    print("=================================")
    print("begin simulation")
    BRA = Team('BRA', 4)
    MEX = Team('MEX', 4)
    CAM = Team('CAM', 0)
    CRO = Team('CRO', 0)
    def resetpoints():
        BRA.points = 4
        MEX.points = 4
        CAM.points = 0
        CRO.points = 0
    outcomes = [(i, j, k) for i in range(-1,2) \
                for j in range(-1,2) for k in range(-1,2)]
    for outcome in outcomes:
        matchup(CAM, CRO, outcome[0])
        matchup(CAM, BRA, outcome[1])
        matchup(CRO, MEX, outcome[2])
        print(BRA)
        print(MEX)
        print(CAM)
        print(CRO)
        print()
        resetpoints()

setup()
BRA

"""
begin simulation
CAM def. CRO
CAM def. BRA
CRO def. MEX
BRA 4
MEX 4 
CAM 6
CRO 3 MAYBE 1

CAM def. CRO
CAM def. BRA
CRO ties MEX
BRA 4
MEX 5
CAM 6
CRO 1 NO 1

CAM def. CRO
CAM def. BRA
MEX def. CRO
BRA 4
MEX 7
CAM 6
CRO 0 NO 2

CAM def. CRO
CAM ties BRA
CRO def. MEX
BRA 5
MEX 4
CAM 4
CRO 3 YES 1

CAM def. CRO
CAM ties BRA
CRO ties MEX
BRA 5
MEX 5
CAM 4
CRO 1 YES 2

CAM def. CRO
CAM ties BRA
MEX def. CRO
BRA 5
MEX 7
CAM 4 
CRO 0 YES 3

CAM def. CRO
BRA def. CAM
CRO def. MEX
BRA 7
MEX 4
CAM 3
CRO 3 YES 4
 
CAM def. CRO
BRA def. CAM
CRO ties MEX
BRA 7
MEX 5
CAM 3
CRO 1 YES 5

CAM def. CRO
BRA def. CAM
MEX def. CRO
BRA 7
MEX 7
CAM 3
CRO 0 YES 6

CAM ties CRO
CAM def. BRA
CRO def. MEX
BRA 4
MEX 4
CAM 4
CRO 4 MAYBE 2

CAM ties CRO
CAM def. BRA
CRO ties MEX
BRA 4
MEX 5
CAM 4
CRO 2 MAYBE 3

CAM ties CRO
CAM def. BRA
MEX def. CRO
BRA 4
MEX 7
CAM 4
CRO 1 MAYBE 4

CAM ties CRO
CAM ties BRA
CRO def. MEX
BRA 5
MEX 4
CAM 2
CRO 4 YES 7

CAM ties CRO
CAM ties BRA
CRO ties MEX
BRA 5
MEX 5
CAM 2
CRO 2 YES 8

CAM ties CRO
CAM ties BRA
MEX def. CRO
BRA 5
MEX 7
CAM 2
CRO 1 YES 9

CAM ties CRO
BRA def. CAM
CRO def. MEX
BRA 7
MEX 4
CAM 1
CRO 4 YES 10

CAM ties CRO
BRA def. CAM
CRO ties MEX
BRA 7
MEX 5
CAM 1
CRO 2 YES 11

CAM ties CRO
BRA def. CAM
MEX def. CRO
BRA 7
MEX 7
CAM 1
CRO 1 YES 12
 
CRO def. CAM
CAM def. BRA
CRO def. MEX
BRA 4
MEX 4
CAM 3
CRO 6 MAYBE 5

CRO def. CAM
CAM def. BRA
CRO ties MEX
BRA 4
MEX 5
CAM 3
CRO 4 MAYBE 6

CRO def. CAM
CAM def. BRA
MEX def. CRO
BRA 4
MEX 7
CAM 3
CRO 3 YES 13

CRO def. CAM
CAM ties BRA
CRO def. MEX
BRA 5
MEX 4
CAM 1
CRO 6 YES 14

CRO def. CAM
CAM ties BRA
CRO ties MEX
BRA 5
MEX 5
CAM 1
CRO 4 YES 15

CRO def. CAM
CAM ties BRA
MEX def. CRO
BRA 5
MEX 7
CAM 1
CRO 3 YES 16

CRO def. CAM
BRA def. CAM
CRO def. MEX
BRA 7
MEX 4
CAM 0
CRO 6 YES 17

CRO def. CAM
BRA def. CAM
CRO ties MEX
BRA 7
MEX 5
CAM 0
CRO 4 YES 18

CRO def. CAM
BRA def. CAM
MEX def. CRO
BRA 7
MEX 7
CAM 0
CRO 3 YES 19

TOTAL YES 19
MAYBE 6
NO 2
"""
