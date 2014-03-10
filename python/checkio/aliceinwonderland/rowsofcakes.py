from fractions import Fraction

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)
        
class Line:
    """
    Line satisfying equation: y = mx + b
    In the special case of vertical lines, m is None and
    b is the x-intercept (normally, m = slope and b = y-intercept)
    """
    def __init__(self, m, b):
        self.m = m
        self.b = b
        
    def contains(self, pt):
        """
        Check if given point lies on this Line
        """
        if self.m == None:
            return pt.x == self.b
        else:
            return self.m * pt.x + self.b == pt.y

    def __eq__(self, other):
        return self.b == other.b and self.m == other.m

    def __hash__(self):
        return hash((self.m, self.b))

    def __repr__(self):
        if self.m == None:
            return "Vertical, x=%s" % self.b
        else:
            return "y = %sx + %s" % (self.m, self.b)

def connect(point1, point2):
    """
    Return a Line connecting point1 and point2
    """
    assert not (point1.x == point2.x and point1.y == point2.y)
    
    if point1.x == point2.x:
        return Line(None, point1.x)
    else:
        dx = point2.x - point1.x
        m = Fraction(point2.y - point1.y, dx)
        b = point1.y - m * point1.x
        return Line(m, b)

def checkio(cakes):
    """
    Define a set to hold valid rows (lines with 3 or more cakes).
    Pick a start point.
    For other points, draw a line containing the start point and the other pt.
    Using this line, check how many cakes it contains.
    If there are three or more, add to the valid rows set.
    Repeat this procedure for all points as the base point.

    It is awfully inefficient because it is checking all combinations of
    segments and no checks are done to skip segments already added.
    """
    validrows = set()
    cakepoints = set([Point(*cake) for cake in cakes])
    for startpoint in cakepoints:
        otherpoints = cakepoints.difference(set([startpoint]))
        for endpoint in otherpoints:
            if startpoint != endpoint:
                cakeline = connect(startpoint, endpoint)
                if sum(cakeline.contains(other) for other in otherpoints) > 1:
                    validrows.add(cakeline)
    return len(validrows)

checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]])
checkio([[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]])
