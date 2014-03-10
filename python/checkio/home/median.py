def checkio(lst):
    slst = sorted(lst)
    count = len(slst)
    if count % 2 == 1:
        return slst[count//2]
    else:
        return (slst[count//2 - 1] + slst[count//2]) / 2

checkio([1,300,2,200,1])
checkio([3,6,20,99,10,15])
