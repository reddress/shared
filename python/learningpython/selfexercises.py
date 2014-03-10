# 1.
# implement zip
#
# zip(*zip(x, y)) returns same thing

def f(*args):
    print("...".join(map(str, args)))
    return 0

# f(1,2,3)

def myzip(*input):
    lastIndex = (min(map(len, input)))
    output = []
    for i in range(lastIndex):
        values = []
        for row in input:
            values.append(row[i])
        output.append(tuple(values))
    return output

list(zip([1,2,3],[4,5,5,6,8],[9,91,991])) == myzip([1,2,3],[4,5,5,6,8],[9,91,991])

myzip([1,2,3],[4,5,5,6,8],[9,91,991])

list(zip("spam", "eggs")) == myzip("spam", "eggs")
myzip([1,2,3])

