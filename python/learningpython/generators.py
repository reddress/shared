def gensquares(n):
    for i in range(n):
        yield i ** 2

#for i in gensquares(5):
#    print(i, end=" : ")

x = gensquares(3)

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

tuple(ups('aaa,b,c'))

def gen():
    for i in range(10):
        x = yield i
        print(x)

g = gen()
next(g)
# g.send(99)

list(x ** 2 for x in range(3))

import math
list(map(math.sqrt, (x ** 2 for x in range(4))))

list(abs(x) for x in (-1,0,1))

list(filter(lambda n: True, [1,2,3]))

line = 'aa bbb c'

def gensub(line):
    for x in line.split():
        if len(x) > 1:
            yield x.upper()

# print(''.join(gensub(line)))

def timesfour(s):
    for c in s:
        yield c * 4

g = timesfour('spam')
next(g)
h = timesfour('spam')
next(h)

def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

list(both(7))
j = both(4)
next(j)

#import os
#print(list(os.walk('.')))
#help(os.popen)

def f(a,b,c): print('%s %s and %s' % (a,b,c))
D = dict(a='bob', b='dev', c=50.4); D
# f(**D)

# for x in 'spam': print(x.upper(), end=' ')

S = "spam"
for i in range(len(S)):
    X = S[i:] + S[:i]
#    print(X, end=" ")

def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

scramble('spam')

def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq

list(scramble("abc"))

def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

list(scramble("spam"))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
list(F("spam"))

# p. 617 my map
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

def mymapcomp(func, *seqs):
    return [func(*args) for args in zip(*seqs)]
    
mymap(lambda x, y: x + y, [1,2,3], [10, 20, 30, 40])
mymapcomp(pow, [1,2,3], [2,3,4,5])

def mymapgen(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

g = mymapgen(pow, [1,2,3], [2,3,4,5])
next(g)

def mymapgenexpr(func, *seqs):
    return (func(*args) for args in zip(*seqs))

g = mymapgenexpr(pow, [1,2,3], [4,5,6,7])
next(g)

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

myzip('abc', 'xyze3')

def myzipgen(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

g = myzipgen('abc','12345')
next(g)

def myzipgenexpr(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

g = myzipgenexpr('abc','1234')
next(g)

def minandprint(*args):
    # print("minarg")
    return min(*args)
minandprint(1,2,3)

def myzipgenexprandprint(*seqs):
    minlen = minandprint(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

g = myzipgenexprandprint("abc", '1234')
next(g)

def myzip621(*args):
    iters = map(iter, args)
    # print(list(iters))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

g = myzip621("abcdef","123456")
next(g)

m = map(lambda x: 2*x, [1,2,3])
next(m)
n = iter(m)
next(n)

from random import randint
def genfun(x):
    if x == 0:
        for i in range(9):
            yield randint(0,9)
    if x == 1:
        return 100
#g = genfun(0)
#next(g)
#next(genfun(1))

def fortest():
    Y = 99
    for Y in range(51):
        pass
    # print(Y)
    [Y for Y in range(99)]
    # print(Y)

fortest()

[(x, y) for x in [1,2,3] for y in [4,5,6]]

# p. 626 quiz
# 1. parentheses return generator
# 2. both respond to next()
# 3. look for yield
# 4. returns a value, but saves function variables' states
# 5. map returns a one-shot iterator

def getsend():
    ct = 0
    while True:
        ct += 1
        s = yield ct
        if s:
            print(s+ct)
        else:
            print("got nothing")

g = getsend()
next(g)
g.send(20)

def neveryield(n):
    if n > 9:
        return n*2
    if 0 == 1:
        yield 0
neveryield(20)
next(neveryield(99))

