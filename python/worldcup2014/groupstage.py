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
...
CRO 4 - 0 CAM

CAM def. BRA
CRO def. MEX
BRA 4
MEX 4
CAM 3
CRO 6 MAYBE 5

CAM def. BRA
CRO ties MEX
BRA 4
MEX 5
CAM 3
CRO 4 MAYBE 6

CAM def. BRA
MEX def. CRO
BRA 4
MEX 7
CAM 3
CRO 3 YES 13

TOTAL YES 19
MAYBE 6
NO 2
"""
