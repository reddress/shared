def copyDict(d):
    res = {}
    for k in d:
        res[k] = d[k]
    return res

d = {'a':1}
e = copyDict(d)
e
d['a'] = 2
d

def addDict(d1, d2):
    r = {}
    for k in d1:
        r[k] = d1[k]
    for k in d2:
        r[k] = d2[k]
    return r

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':100, 'd':400, 'e':500}

addDict(d1,d2)
