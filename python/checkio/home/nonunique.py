def checkio(data):
    return [n for n in data if count(n, data) > 1]

def count(n, lst):
    return len([m for m in lst if m == n])

count(1, [1,2,3,1,1])
checkio([1,2,3,1,3])
checkio([5,5,5,5,5])
