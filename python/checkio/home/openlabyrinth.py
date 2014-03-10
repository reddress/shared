maze = ([[1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,1,1,1],
         [1,0,0,0,1],
         [1,1,1,1,1]])


class MazeSolver:
    def __init__(self, start, goal, map):
        self.goal = goal
        self.map = map
        self.moves = {}
        self.moves[start] = ""
        self.visited = {}
        self.start = start

    def newpos(self, curpos, dir):
        def addcoords(t, u):
            return (t[0] + u[0], t[1] + u[1])
        if dir == "N":
            return addcoords(curpos, (-1, 0))
        elif dir == "S":
            return addcoords(curpos, (1, 0))
        elif dir == "E":
            return addcoords(curpos, (0, 1))
        elif dir == "W":
            return addcoords(curpos, (0, -1))
            
    def getvalue(self, pos):
        return self.map[pos[0]][pos[1]]

    def possiblemoves(self, pos):
        movelist = []
        for dir in "NSEW":
            if self.getvalue(self.newpos(pos, dir)) == 0:
                movelist.append(dir)
        return movelist

    def walker(self, curpos):
        for dir in self.possiblemoves(curpos):
            newposition = self.newpos(curpos, dir)
            if not newposition in self.moves:
                self.moves[newposition] = self.moves[curpos] + dir
                self.walker(newposition)

ms = MazeSolver((1,1), (3,3), maze)
ms.walker(ms.start)
print(ms.moves[ms.goal])
