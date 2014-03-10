from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s,%s)" % (round(self.x, 2), round(self.y, 2))

class Line:
    # y = mx + b
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def __str__(self):
        return "y = %sx + %s" % (self.m, self.b)

def fromstring(str):
    nums = str.replace("(", "").replace(")", "").split(",")
    return Point(int(nums[0]), int(nums[1]))

def intersection(line1, line2):
    x = (line1.b - line2.b) / (line2.m - line1.m)
    y = line1.m * x + line1.b
    return Point(x, y)

def connect(point1, point2):
    # prevent division by zero
    if point2.x == point1.x:
        dx = 1e-9
    else:
        dx = point2.x - point1.x
    m = (point2.y - point1.y) / dx

    # b = point1.x * m  # submitted solution incorrect
    # corrected in rowsofcakes.py
    b = point1.y - m * point1.x
    return Line(m, b)

def midpoint(p1, p2):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    
def perpendicular(line, point):
    if line.m == 0:
        line.m = 1e-6
    return Line(-(1/line.m), point.y + point.x * (1/line.m))

def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def stripzero(float):
    s = str(float)
    if s[-2:] == ".0":
        return s[:-2]
    else:
        return s
        
def circlefrompoints(p1, p2, p3):
    segment1 = connect(p1, p2)
    segment2 = connect(p2, p3)
    pline1 = perpendicular(segment1, midpoint(p1, p2))
    pline2 = perpendicular(segment2, midpoint(p2, p3))
    center = intersection(pline1, pline2)
    return "(x-%s)^2+(y-%s)^2=%s^2" % (stripzero(round(center.x, 2)),
                                       stripzero(round(center.y, 2)),
                                       stripzero(round(distance(center, p1), 2)))

def checkio(s):
    s = s.replace("),(", ");(")
    return circlefrompoints(*map(fromstring, s.split(";")))


p1 = Point(2,2)
p2 = Point(2,6)
p3 = Point(6,2)

q1 = Point(3,7)
q2 = Point(6,9)
q3 = Point(9,7)



checkio("(3,7),(6,9),(9,7)")
checkio("(2,2),(4,2),(2,4)")
