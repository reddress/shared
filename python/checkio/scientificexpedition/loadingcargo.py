
# check all combinations
def num2bin(n, width):
    return "{0:b}".format(n).zfill(width)

def diff(left, right):
    return abs(sum(left) - sum(right))

def checkio(data):
    min_diff = sum(data)
        
    for i in range(2 ** len(data)):
        weights = data[:]
        left = []
        right = []
        
        arrangement = num2bin(i, len(data))
        for c in arrangement:
            if c == "0":
                left.append(weights.pop())
            else:
                right.append(weights.pop())

        d = diff(left, right)
        if d < min_diff:
            min_diff = d
    return min_diff

checkio([12, 30, 30, 32, 42, 49])
