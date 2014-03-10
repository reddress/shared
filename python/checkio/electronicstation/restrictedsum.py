def checkio(data):
    def accum(lst, total):
        if lst:
            return accum(lst[1:], total + lst[0])
        return total
    return accum(data, 0)

checkio([1,2,3,4,5])
