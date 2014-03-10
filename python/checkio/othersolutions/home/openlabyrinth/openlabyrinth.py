#dictionary with keys is available symbols, values - (dx, dy).
DIRECTIONS = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
 
from heapq import heappop, heappush, heapify
from collections import namedtuple
 
State = namedtuple('State', ('priority', 'position', 'path', 'cost'))
 
 
def heuristic(position, goal):
    """
    Calculate heuristic value for position.
    Using manhattan distance from position to goal.
    position - tuple(x:int, y:int) - coordinate of position.
    goal - tuple(x:int, y:int) - coordinate of goal.
    Return heuristic value - int..
    """
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])
 
 
def successor(position, maze):
    """
    Return neighbours coordinates with cost (always 1) and used direction.
    position - tuple(int, int) - coordinate of position.
    maze - matrix with maze map.
    return list of tuples with neighbours data - (coordinate:(int, int), direct:str)
    """
    neighs = []
    for direct, (dx, dy) in DIRECTIONS.items():
        x = position[0] + dx
        y = position[1] + dy
        #check wall
        if not maze[x][y]:
            neighs.append(((x, y), direct))
    return neighs
 
 
def checkio(labyrinth):
    """
    Using A-star graph search algorithm.
    labyrinth - square matrix with 0 or 1 - list[][].
    return route from (1,1) to (10, 10) - string.
    """
    start = (1, 1)
    goal = (10, 10)
    #priority=cost+heuristic, position, path, cost
    queue = [State(0, start, '', 0)]
    heapify(queue)
    #visited cells
    closed = set()
    while queue:
        #select node with min heuristic + cost
        current = heappop(queue)
        if current.position == goal:
            return current.path
            #check in closed nodes
        if current.position in closed:
            continue
        neighbours = successor(current.position, labyrinth)
        for new_position, direction in neighbours:
            if new_position in closed:
                continue
            priority = current.cost + 1 + heuristic(new_position, goal)
            heappush(queue, State(priority, new_position, current.path + direction, current.cost + 1))
        closed.add(current.position)
        #No route - Suicide
    return "N"
