grid = [
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]]

gridv = [
    [1, 2, 3, 4],
    [1, 2, 3, 3],
    [9, 2, 8, 7],
    [3, 2, 3, 9]]

def transpose(m):
    return list(zip(*m))

def checkindirection(m, row, col, drow, dcol, count):
    try:
        value = m[row][col]
        return (m[row+drow][col+dcol] == value and
                m[row+2*drow][col+2*dcol] == value and
                m[row+3*drow][col+3*dcol] == value)
    except:
        print("out of bounds")
        return False

def checkhorizontally(m):
    for row in range(len(m)):
        for col in range(len(m) - 3):
            if checkindirection(m, row, col, 0, 1, 1):
                return True
    return False

def checkvertically(m):
    return checkhorizontally(transpose(m))

def checkbackslash(m):
    for row in range(len(m) - 3):
        for col in range(len(m) - 3):
            if checkindirection(m, row, col, 1, 1, 1):
                return True
    return False

def checkslash(m):
    for row in range(len(m) - 3):
        for col in range(2, len(m)):
            if checkindirection(m, row, col, 1, -1, 1):
                return True
    return False

def checkio(m):
    return (checkhorizontally(m) or checkvertically(m) or
            checkbackslash(m) or checkslash(m))
