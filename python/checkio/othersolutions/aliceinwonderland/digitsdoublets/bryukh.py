def count_diff(first, second):
    """
    Count how many digits are distinguished in the two numbers.
    """
    return len(str(first)) - sum(f == s for f, s in zip(str(first), str(second)))
 
 
def list_to_graph(numbers):
    """
    Convert a list of numbers in the dict graph representation,
    where each key is a node and values are "neighbour" numbers.
    """
    res = {}
    for node in numbers:
        res[node] = []
        for second_node in numbers:
            if count_diff(node, second_node) == 1:
                res[node].append(second_node)
    return res
 
 
def checkio(numbers):
    """
    I'm using "Breadth-first search" algorithm here.
    http://en.wikipedia.org/wiki/Breadth-first_search
    """
    graph = list_to_graph(numbers)
    goal = numbers[-1]
    # the queue contains positions and paths for they.
    queue = [(numbers[0], (numbers[0],))]
    # the visited numbers we store in the set, because it faster
    closed = set()
    while queue:
        current, path = queue.pop(0)
        if current in closed:
            continue
        closed.add(current)
        if current == goal:
            return list(path)
        for neigh in graph[current]:
            if neigh in closed:
                continue
            queue.append((neigh, path + (neigh,)))
    return []

checkio([123, 991, 323, 321, 329, 121, 921, 125, 999])
