counter = 99

def makecounter():
    counter = 0
    def increasecounter():
        def evendeeper():
            nonlocal counter
            counter += 1
            print(counter)
        evendeeper()
    return increasecounter

f = makecounter()
f()
g = makecounter()
g()

# http://stackoverflow.com/questions/4020419/closures-in-python
def make_printer(msg):
    def printer():
        print(msg)
    return printer

printspam = make_printer('spam')
printspam()

somestr = 'some'
L = [1,2,3]
def useL():
    L.append(4)
    print(L)
    print(somestr)
    anotherstr = 'another'
    def printanother():
        nonlocal anotherstr
        anotherstr += 'yes'
        print(anotherstr)
    printanother()
L
useL()

def first():
    str = "first"
    def second():
        str = "second"
        def third():
            nonlocal str
            print(str)
        third()
    second()

first()

topstr = "top"
def top1():
    topstr = "top 1"
    def top2():
        # nonlocal topstr
        global topstr
        print(topstr)
    top2()

top1()

X = 99

def func(Y):
    Z = X + Y
    return Z

func(1)

# http://stackoverflow.com/questions/233673/lexical-closures-in-python?rq=1
flist = []
def outer():
    for i in range(3):
        def inner(x, i=i):
            return x * i
        flist.append(inner)
outer()
flist
for f in flist:
    print(f(3))

def f(x):
    f.a = x
    return f.a

f(9)

y, z = 1, 2
def all_global():
    global allglobalx
    allglobalx = y + z

all_global()
allglobalx

import python.functions
python.functions.intersect("spam", "sam")

import python.myvars

python.myvars.printmyvar()
python.myvars.myvar = 99

# p. 499-500
var = 99

def global2():
    var = 0
    import python.scoping
    python.scoping.var += 1

def test():
    print(var)
    global2()
    print("new var", var)

test()
global2()

# p. 501
def f1():
    x = 88
    def f2():
        print(x)
    return f2

action = f1()
action()

def maker(N):
    def action(X):
        return X ** N
    return action

squarer = maker(2)
squarer

squarer(9)

def func():
    x = 4
    action = lambda n: x ** n
    return action

g = func()
print(g(2))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = makeActions()
acts[2](2)
acts[3](2)

def counter():
    c = [0]
    def addtoctr():
        c[0] += 1
        print(c[0])
    return addtoctr

g = counter()
g()

""" does not work
def counter_regular():
    c = 0
    def addtoctr():
        c += 1
        print(c)
    return addtoctr

h = counter_regular()
h()
"""

# p. 515
def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

f = tester(18)
f("abc")

def tester517(start):
    state = [start]
    def nested(label):
        print(label, state[0])
        state[0] += 1
    return nested

f = tester517(10)
f("hi")
f("bye")

# p. 519 quiz
# 1. Spam, lookup rule
# 2. Spam, Ni disappears after function call
# 3. Ni\nSpam ...
# 4. Ni, global accesses and modifies module level X
# 5. Ni Spam
# 6. Spam
# 7. global, closure, nonlocal, attributes
