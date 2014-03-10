bar_test = {'gold-tin': Fraction(1, 2),
            'gold-iron': Fraction(1, 3),
            'gold-copper': Fraction(1, 4)}

bar = {'gold-tin': 0.5,
       'gold-iron': 0.333333,
       'gold-copper': 0.25}
bar2 = {'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2)}

from fractions import Fraction

def addrows(a, b):
    return [sum(x) for x in zip(a, b)]

def scalerow(row, a):
    return [a * x for x in row]
    
def keytorow(dict, key):
    metals = ['copper', 'iron', 'tin', 'gold']

    row = [0 for i in range(5)]
    for metal in key.split("-"):
        row[metals.index(metal)] = 1
    row[-1] = dict[key]
    return row

def bartomatrix(bar):
    m = [keytorow(bar, k) for k in bar]
    m.append([1, 1, 1, 1, 1])
    return m

def eliminate(matrix, col):
    selected = []
    selectedindex = 0
    # find row with zeros up to col
    for i in range(len(matrix)):
        row = matrix[i]
        if all(x == 0 for x in row[:col]) and abs(row[col]) > 0:
            selected = row
            selectedindex = i
    print("selected: ", selected)

    for i in range(len(matrix)):
        if i != selectedindex:
            row = matrix[i]
            # convert to Fraction later
            # factor = -1 * row[col] / selected[col]
            factor = Fraction(-1 * row[col], selected[col])
            print(i)
            matrix[i] = addrows(row, scalerow(selected, factor))
    return matrix

def findgold(matrix):
    goldrow = []
    for row in matrix:
        if all(x == 0 for x in row[:3]):
            factor = row[3]
            return row[4] / factor

def checkio(bar):
    matrix = bartomatrix(bar)
    for i in range(3):
        eliminate(matrix, i)
    return findgold(matrix)

checkio(bar_test)
