def isneighbor(m, n):
    differences = 0
    for i in range(len(m)):
        if m[i] != n[i]:
            differences += 1
    return differences == 1

class Puzzle:
    def __init__(self, list):
        self.nodes = {id: str(n) for id, n in enumerate(list)}
        self.end_id = len(self.nodes) - 1
        self.neighbors = {}
        self.complete_paths = []

        for id in self.nodes:
            self.neighbors[id] = []
            
        for id in self.nodes:
            for other_id in self.nodes:
                if isneighbor(self.nodes[id], self.nodes[other_id]):
                    self.neighbors[id].append(other_id)

    def step(self, begin_id, visited, path):
        for next_id in self.neighbors[begin_id]:
            if next_id == self.end_id:
                path.append(self.end_id)
                self.complete_paths.append(path)
            elif next_id not in visited:
                self.step(next_id, visited+[next_id], path+[next_id])

    def solve(self):
        self.step(0, [0], [0])
        self.complete_paths.sort(key=len)
        shortest_path = self.complete_paths[0]
        return list(map(lambda n: int(self.nodes[n]), shortest_path))

def checkio(numbers):
    p = Puzzle(numbers)
    return p.solve()

    
m = Puzzle([123, 991, 323, 321, 329, 121, 921, 125, 999])
n = Puzzle([111, 222, 333, 444, 555, 666, 121, 727, 127, 777])

m.solve()
n.solve()
m.complete_paths.sort(key=len)
m.complete_paths

o = Puzzle([456, 455, 454, 356, 656, 654])
o.solve()
