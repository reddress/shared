class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

x = Number(5)
y = x - 2
y.data

class IndexSq:
    def __getitem__(self, index):
        if isinstance(index, slice):
            return [1,2,3,4,5][index]
        else:
            return index ** 2

x = IndexSq()
x[3]
x[0:5:2]

k = iter(x)
next(k)

class asIndex:
    def __index__(self):
        return 17

c = asIndex()
hex(c)

lst = list("abcdefghijklmnopqrstuvw")
lst[c]

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

si = StepperIndex()
si.data = "spam"

def testStepper():
    for letter in si:
        print(letter, end=" ")

# testStepper()

'p' in si
list(map(str.upper, si))

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
#for i in Squares(1, 5):
#    print(i)

# dirty way of supporting multiple scans is converting to a list
lst = list(Squares(1, 5))
tuple(lst), tuple(lst)

# p. 907

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end="")
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):
        print('contains: ', end="")
        return x in self.data

def testIters():
    x = Iters([1,2,3,4,5])
    print(3 in x)
    for i in x:
        print(i, end=" | ")

    print("PART II")

    print([i ** 2 for i in x])
    print("PART III")
    print(list(map(bin, x)))

    j = iter(x)
    while True:
        try:
            print(next(j), end=' @ ')
        except StopIteration:
            break

testIters()
y = Iters([1,2,3,4,5,6,7])
j = iter(y)
k = iter(y)
next(j)
next(k)

y[2]

class ItersYield:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):
        print('get[%s]:' % i, end="")
        return self.data[i]
    def __iter__(self):
        print('iter=> next:', end='')
        for x in self.data:
            yield x
            print('next:', end='')
    def __contains__(self, x):
        print('contains: ', end="")
        return x in self.data
        
m = ItersYield([1,2,3,4,5])
i = iter(m)
j = iter(m)
next(i)
next(j)

m[2]
[i ** 2 for i in m]
2 in m
m[1:3]

class Options:
    def __getitem__(self, choice):
        print(choice*2)

p = Options()
p['ok']
p[9]

class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

x = Empty()
x.age
# x.name

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # self.__dict__[attr] = value + 10
            object.__setattr__(self, attr, value + 20)
        else:
            raise AttributeError(attr + " not allowed")

x = Accesscontrol()
x.age = 40
x.age
# x.name = "bob"

# p. 913
class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other
x = adder()
print(x)

class addrepr(adder):
    def __repr__(self):
        return 'addrepr (%s)' % self.data

x = addrepr(2)
x + 1
print(x)

class hasrepr:
    name = "Has repr"
    def __repr__(self):
        return self.name

class norepr(hasrepr):
    name = "No repr"

n = norepr()
print(n)

class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return self.val + other
    def __repr__(self):
        return "[%s]" % self.val

x = Commuter1(88)
y = Commuter1(99)
x + 1
1 + y
x + y

# p. 919
class Commuter5:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print("calling comm5 add")
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)
    def __radd__(self, other):
        print("calling comm5 radd")
        return Commuter5(other + self.val)
    def __str__(self):
        return "[commuter5: %s]" % self.val

x = Commuter5(88)
y = Commuter5(99)
print(x + 10)
print(10 + y)
print(x + y)

class mynumber:
    def __init__(self, n):
        self.val = n
    def __add__(self, other):
        return self.val + other

a = mynumber(9)

class Number:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        self.val += other
        return self
    def __repr__(self):
        return "n.: %s" % self.val

n = Number(9)
n += 1
print(n)

class C:
    def __call__(self, *pargs, d=6, **kargs):
        print("called:", pargs, d, kargs)

x = C()
x(1, *(2,), **dict(d=4, e=9))

mycallback3 = lambda color="red": 'turn ' + color
print(mycallback3())

class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)

cb1 = Callback('green')
cb1()
