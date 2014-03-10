import operator, functools, math

def digitsproduct(n):
    return functools.reduce(operator.mul, [int(c) for c in str(n)])

def checkio(n):
    # check numbers up to 999...999 whose number of digits is
    # one more than n
    for i in range(1, 10 ** (round(math.log(n) / math.log(10)) + 2)):
        if digitsproduct(i) == n:
            return i
    return 0

checkio(17)
