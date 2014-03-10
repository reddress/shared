def add(x, y):
    return x + y

print(add(2,3))
print(add("ab", "ra"))
print(add(1.2, 2))

def addmany(*args):
    res = args[0]
    # for i in range(len(args)-1):
    for next in args[1:]:
        # res += args[i+1]
        res += next
    return res

addmany(2,3,4)
addmany("a", "b", "c")

def adddict(good=1, bad=2, ugly=3, **rest):
    res = good + bad + ugly
    for k in rest:
        res += rest[k]
    return res

adddict(ugly=1, good=2, something=100)

from math import sqrt
nums = [2, 4, 9, 16, 25]

roots = []
for n in nums:
    roots.append(sqrt(n))

roots2 = map(sqrt, nums)
list(roots2)

[sqrt(n) for n in nums]

g = (sqrt(n) for n in nums)
next(g)

def genroot(lst):
    for n in lst:
        yield sqrt(n)

gg = genroot(nums)
next(gg)

def countdown(start):
    if start <= 0:
        print("stop")
    else:
        print(start, end=" ")
        countdown(start-1)

countdown(5)

def countgen(n):
    if n == 0:
        yield 'stop'
    else:
        yield n
        yield from countgen(n-1)

g = countgen(5)
list(g)

list(range(1,9))
