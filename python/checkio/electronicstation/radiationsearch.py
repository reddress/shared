partm = [
 [1,2,3,4,5],
 [1,1,1,2,3],
 [1,1,1,2,2],
 [1,2,2,2,1],
 [1,1,1,1,1]]

# current method breaks on row (1,2,2,2,1) because the 2s are assigned a new
# group, when they should match the 2s above. To reassign correctly, I would
# need to backtrack

from collections import namedtuple

Part = namedtuple('Spare_part', ['row', 'col', 'id'])

def isadjacentpart(a, b):
    return (a.id == b.id and
            ((b.col == a.col - 1 and b.row == a.row) or
             (b.col == a.col + 1 and b.row == a.row) or
             (b.col == a.col and b.row == a.row - 1) or
             (b.col == a.col and b.row == a.row + 1)))

def checkio(matrix):
    n = len(matrix)
    currentgroup = 0
    groups = {}
    # initialize groups
    for i in range(100):
        groups[i] = []
        
    groupmatrix = [[-1 for i in range(n)] for j in range(n)]
    partmatrix = matrix[:]
    
    # set up Parts matrix
    for row in range(n):
        for col in range(n):
            partmatrix[row][col] = Part(row=row, col=col, id=matrix[row][col])
            
    for row in range(n):
        for col in range(n):
            if groupmatrix[row][col] == -1:
                # assign to group
                groupmatrix[row][col] = currentgroup
                groups[currentgroup].append(partmatrix[row][col])
                currentgroup += 1
            # check cell to right, add to group if part matches
            try:
                if isadjacentpart(partmatrix[row][col], partmatrix[row][col+1]):
                    groupmatrix[row][col+1] = groupmatrix[row][col]
                else:
                    if groupmatrix[row][col+1] == -1:
                        groupmatrix[row][col+1] = currentgroup
                        groups[currentgroup].append(partmatrix[row][col+1])
                        currentgroup += 1
            except:
                # out of bounds
                pass

            # check cell below
            try:
                if isadjacentpart(partmatrix[row][col], partmatrix[row+1][col]):
                    groupmatrix[row+1][col] = groupmatrix[row][col]
                else:
                    if groupmatrix[row+1][col] == -1:
                        groupmatrix[row+1][col] = currentgroup
                        groups[currentgroup].append(partmatrix[row+1][col])
                        currentgroup += 1
            except:
                # out of bounds
                pass
#    print(groups)
    print(groupmatrix)

checkio(partm)

