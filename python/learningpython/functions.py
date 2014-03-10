# p. 475 functions can have attributes attached to them

def myfun():
    pass
myfun.name = "My function"
myfun.dbl = lambda x: x * 2

myfun.dbl(myfun.name)

def doubletail(lst):
    lst[-1] *= 2

mylist = [1,2,3]
doubletail(mylist)

mylist

f = lambda x: x + 10
f(7)

[attr for attr in dir(myfun) if attr[0] != "_"]

list(filter(lambda attr: attr[0] != "_", dir(myfun)))

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

intersect("SPAM", "SCAM")

# p. 483 quiz
# 1. reuse code and improve readability
# 2. when reaching def
# 3. None
# 4. when called
# 5. eliminates polymorphism and python does error checking on its own

# p. 555 recursion
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
mysum([1,2])
mysum([2])

L = [0]
L[1:]    # out of bounds slice returns []

def evenp(n):
    if n == 0:
        return True
    else:
        return oddp(n-1)

def oddp(n):
    if n == 0:
        return False
    else:
        return evenp(n-1)

evenp(9)

def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total

lst = [1, [2, [3, 4], 5], 6, [7, 8]]

# breadth-first
def sumtreebreadth(L):
    total = 0
    items = list(L)
    while items:
        print(items)
        front = items.pop(0)
        if not isinstance(front, list):
            total += front
        else:
            items.extend(front)
    return total

sumtree(lst)

# prepend to list
items = [1,2,3]
items[:0] = [0]
items

# depth-first
def sumtreedepth(L):
    total = 0
    items = list(L)
    while items:
        print(items)
        front = items.pop(0)
        if not isinstance(front,list):
            total += front
        else:
            items[:0] = front
    return total

sumtreedepth(lst)

def myfun2():
    myfun2.counter += 1

myfun2.counter = 0
myfun2()
myfun2.counter

f3 = lambda x: x*2
f3(9)

def echo(message):
    print("called echo: ", end="")
    print(message)

echo('direct call')
x = echo
x('indirect')

def func(a: 'something', b: (1, 10), c: float = 99) -> int:
    return a + b + c

func(1,2)
func.__annotations__

z = lambda x: x*2
z(9)

def callmewith2(f):
    print(f(2))

callmewith2(lambda x: 10+x)

(lambda x: "pos" if x > 0 else "not pos")(3)

# alterx = lambda k: n = k  # cannot assign in lambda

(lambda n: 10 + (lambda m: 100 + m)(n))(7)

def action(x):
    n = 1
    return lambda y: x + n + y

action(9)(9)

s = [1,2,3]
list(map(lambda x: x*2, s))
s

list(map(pow, [1,2,3], [2,3,4]))

def inc(x):
    return x + 10

g = (inc(x) for x in [1,2,3,4])
dir(g)
g.send(None)

import operator
operator.add(1,1)

# p. 578 quiz
# 1. both package code into named reusable parts
# 2. eliminate clutter
# 3. map applies function iteratively, filter compacts iterable, reduce
#    returns one value
# 4. a form of documentation, NOT. "syntactic embellishments" that are
#    packaged for potential use by other tools
# 5. functions that call themselves
# 6. not too long, well-defined purpose
# 7. return, modify mutable, and global variables


