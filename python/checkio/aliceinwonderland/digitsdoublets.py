class Node:
    """
    Holds the integer as a string (to compare digit-by-digit)
    Might be repeating myself using ids here and in the dictionary below,
    but
    """
    
    def __init__(self, value, id):
        self.value = str(value)
        self.id = id
    def __repr__(self):
        return "%s [%s]" % (self.value, self.id)

def isneighbor(m, n):
    assert len(m.value) == len(n.value)
    differences = 0
    for i in range(len(m.value)):
        if m.value[i] != n.value[i]:
            differences += 1
    return differences == 1

class Map:
    def __init__(self, list):
        self.nodes = {id: Node(n, id) for id, n in enumerate(list)}
        self.start = self.nodes[0]
        self.end = self.nodes[len(self.nodes) - 1]
        self.valid_paths = []
        
        self.neighbors = {}

        for id in self.nodes:
            self.neighbors[id] = []
            
        for id in self.nodes:
            for other_id in self.nodes:
                if isneighbor(self.nodes[id], self.nodes[other_id]):
                    self.neighbors[id].append(other_id)

    def printNeighbors(self):
        for id in sorted(self.nodes):
            print(self.nodes[id], end=": ")
            for neighbor_id in self.neighbors[id]:
                print(self.nodes[neighbor_id], end=",")
            print()

    def step(self, begin_id, visited, path):
        for next_id in self.neighbors[begin_id]:
            if next_id == self.end.id:
                path.append(self.end.id)
                self.valid_paths.append(path)
            elif next_id not in visited:
                self.step(next_id, visited+[next_id], path+[next_id])

    def solve(self):
        self.step(0, [0], [0])
        self.valid_paths.sort(key=len)
        shortest_path = self.valid_paths[0]
        return list(map(lambda n: int(self.nodes[n].value), shortest_path))
            
"""
idea:
from start, go to
def step(start, path):


"""



m = Map([123, 991, 323, 321, 329, 121, 921, 125, 999])
n = Map([111, 222, 333, 444, 555, 666, 121, 727, 127, 777])

m.solve()
n.solve()
m.valid_paths.sort(key=len)
m.valid_paths
