# p. 527
def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y
x = 1
L = [1, 2]
x, L = multiple(x, L)
x, L

a, *b, c = [1,2,3,4,5]
b
(*a,) = multiple(x, L)
a

# p. 528 explicit assignment
def f(T):
    (a, (b, c)) = T
    return a + b + c

f((1, (2, 3)))
f([10, [20, 30]])

def getname(*, name):  # zero positional arguments
    print(name)

getname(name="bob")

def func(*other, name):
    print(other)

func(1,2, name="joe")

def fxy(x, y, *, name):
    print(name, x + y)

fxy(10, 7, name='mary')

def adder(*args):
    print(type(args))
    return sum(x for x in args)

adder(100,92,3)
t = (1,2,3)
adder(*t)
lst = [1,2,3]
adder(*lst)

def multaddlabel(multiplier, *add_n, label):
    print(label, multiplier * sum(n for n in add_n))

multaddlabel(9, 10, 2, label="times nine")

def f_argannot(name:"the annotation"="the default"):
    print(name)

f_argannot(name="kate")

def f(a, b, c):
    print(f.__name__, ":", a,b,c)

f(c=3, a=1, b=2)

# p. 534
def f2(*args): print(args)
f2(1)

def echo(*args, **kwargs):
    print(args, kwargs)

pargs = (1,2)
kargs = {'a': 3, 'b': 4}

echo(9, c=5, *pargs, **kargs)

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

min1("az", "aa", "bc", "3")

def inters(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

inters("SPAM", "SCAM", "SMIRK")

def f3(n):
    output = ('' if n == 0 else "*") + str(n)
    print(output)

f3(0)

# p. 551 quiz
# 1. 1,2,5
# 2. 1,2,3
# 3. 1, (2,3)
# 4. 1, {'b': 2, 'c': 3}
# 5. 1, 5, 6, 4
# 6. 1, ['x'], {'a': 'y'}
