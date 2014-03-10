def checkRows(data):
    for row in data:
        if row.count(row[0]) == len(row) and row[0] != '.':
            return row[0]
    return None

def checkCols(data):
    coldata = []
    for colindex, letter in enumerate(data[0]):
        column = ""
        for rowindex, row in enumerate(data):
            column += data[rowindex][colindex]
        coldata.append(column)
    return checkRows(coldata)

def checkDiags(data):
    diag1 = data[0][0] + data[1][1] + data[2][2]
    diag2 = data[0][2] + data[1][1] + data[2][0]
    return checkRows([diag1, diag2])
        
def checkio(game_result):
    winner = (checkRows(game_result) or checkCols(game_result) or
              checkDiags(game_result))
    if winner:
        return winner
    else:
        return 'D'

checkio(["XXO","XX.", "OOO"])
