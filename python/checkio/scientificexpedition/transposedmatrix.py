def checkio(data):
    result = [[] for i in range(len(data[0]))]
    for row in data:
        for trow, val in enumerate(row):
            result[trow].append(val)
    return result

checkio([[1,3], [4,9], [6,2]])
