def myfun(x):
    return x*2

def someCond(y):
    if y > 0:
        return "Positive!"
    else:
        return "negative"

def thirdfun(z):
    return myfun(10+z)

# thirdfun(9) 
# someCond(9)
# someCond(-3)
# thirdfun(9)
# 3+3

9+8
2+2

#def somebuggyfunction(z):
#    if True:
#        print("True")

# somebuggyfunction(9)

list(range(9))
from random import randint
randint(1,2)

list(range(9))

def listOfRandom(a, b, n):
    result = []
    for i in range(n):
        result += [randint(a, b)]
    return result

listOfRandom(1,6,12)
[randint(1,6) for i in range(9)]

#for i in range(2):
#    print("ok")

1/3
3//4

def someotherfun(x):
    return 3

someotherfun(9)

from collections import namedtuple
constr = namedtuple('DisplayName', 'a')
cc = constr(99)
cc
cc.a
type(cc)

Pt = namedtuple('Point', 'x y')
pt1 = Pt(2.0, 3.0)
pt1

('name', 'joe', 'age', 3)[-1]
(1,2,)

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

ma = Worker('Alice Kay Moore', 90000)
ma.lastName()

import decimal
class mynum:
    def __init__(self, str):
        self.x = decimal.Decimal(str)

m = mynum("3.14")
m.x * -2
m.x.sqrt()


a = 3
a
b = a
b
a = 4

x = [1,2,3]
y = x
x[0] = 10
y
y[1] = 20
x

w = [1,2]
v = w

v = [3,4]
w

# dynamic typing quiz
# 1. no
# 2. yes
# 3. no

"{1} is {2}".format(2,3,4)

"{:3.2f}".format(9999.3)

"{:X}".format(199)

S=set("spam")
S.add('alot')
S.update(set('alot'))
S.update('xyz')
S

def odd(x):
    return x % 2 == 1
    
{odd(x) for x in range(1,5)}
[odd(x) for x in range(1,5)]
{i*j for i in range(1,4) for j in "john"}

fns = {'add': lambda x, y: x + y, 'sub': lambda x, y: x - y}
fns['add'](3, 3)

choice = 'sub'
#print(fns[choice](2,3))
(3+3)

def fn(x):
    return x*10
    
(fn(9))

# p. 205

repr(33)

import os
#os.chdir("/home/heitor/python")

#with open("hello.py") as add:
#    ctr = 1
#    for line in add:
#        print("{}: {}".format(ctr, line), end="")
#        ctr += 1

B = '111101'
B[1:]
ord('1')
ord('0')
int("1101",2)
"abcdef"[::2]
s = 'spamMMmMer'
s.find('pa')
#help(s.casefold)
s.casefold()
s.center(99)
s.count('M')
#help(s.maketrans)
#help(s.translate)
s.translate(s.maketrans("mM", "cC"))
s.translate({ord('s'): 'XssS'})
#help(s.replace)
2**8
",,,,a,,,b,,c".split(",")
import string
string.digits
n = 1
"%d %s%s" % (n, "dog", "s" if n > 1 else "")

import math
"%s" % math.pi
"%s %g" % ((2.0/3.0), math.pi)
"%c" % 23202
"%g" % 300.1234567
"%0*.*f" % (12, 3, 20000.294920)
"%(qty)d more %(food)s" % {'qty': 1, 'food': 'spam'}
 
reply = """
Hello %(name)s!
Your age is %(age)d
""" 
values = {'name': 'Joe', 'age': 35}
# print(reply % values)

food = "spam"
qty = 10

"%(qty)d more %(food)s" % vars()

template = "{0}, {j} {1}, And {2}"
template.format("spam", "eggs", "gravy", j="ham")

"%(han solo)s is da man" % {'han solo': 'harrison ford'}
"{wesley_gibson} is da man".format(wesley_gibson = "james")

import sys
"my {1[kind]} runs {0.platform}".format(sys, {'kind': 'laptop'})

somelist = list("SPAM")
somelist
'first={0}, last={1}'.format(somelist[0], somelist[-1])

'first {list[2]}'.format(list=somelist)

# p. 224
"{:,.3f}".format(9999.223344)
"{0:10} = {1:10}".format("spam", 123.4567)

dec = ".2f"
"{0:{1}}".format(3.226442, ".2f")
"{0[0]}".format("spam")

"1234567"

# out = []
# out += "123" is L.extend
# out + [1] is "concatenation"

movies = {'1975': 'holy grail',
          '1979': 'Brian',
          '1981': 'Brian',
          '1983': 'meaning'}

# for yr in movies:
#    print("{} \t {}".format(yr, movies[yr]))

# [year for (year, title) in movies.items() if title == 'Brian']
# movies.items()

[year for year in movies.keys() if movies[year] == 'Brian']

# shelve: alternative to pickle

# list/dictionary chapter quiz p. 272
#
# 1. [0]*5, [0,0,0,0,0]
# 2. dict(a=0, b=0), dict.fromkeys(['a','b'],0)
# 3. append, extend, del, assignment lst[0] = 0
# 4. assignment, del, addition, update
# 5. readability, sparse objects

from collections import namedtuple

Rec = namedtuple('Record', ['name', 'age', 'jobs'])
bob = Rec('bob', age=30, jobs=['dev', 'manager'])
bob

d = {'name': 'sarah', 'age': 33, 'jobs': ['teacher', 'parent']}
bob._asdict()
d.values()
job, name, age = d.values()
job
name

Rec(**d)

# comparisons, equality
s1 = "a longer string"
s2 = "a longer string"

s1 is s2
s1 == s2


class myclass:
    a = 3

class myint(int):
    a = 30

T = (4,5,6)
(1,) + T[1:]
# tuples quiz p. 311

# 1. len(), because it is generic
# 2. (1,) + T[1:]
# 3. read text
# 4. shelve or pickle
# 5. copy.deepcopy
# 6. length > 1, nonempty
# 7. ????
# 8. profit!

data = {'name': {'first': 'joe', 'last': 'hou'}, 'age': 31, 'phone': '555-1242'}
data['name']

#filename = '/home/heitor/python/myfile.txt'
#f = open(filename, 'w')
#f.write("Hello file world")
#f.close()

#f = open(filename)
#f.readline()
#f.close()

#a = 0
#while a < 10:
##    print(a)
#    a += 1
#else:
#    print("the else clause {}".format(a))
    
# nested whiles

"""
ctr = 0
while ctr < 10:
    w = ""
    while w != "q":
        w = input("enter a word: ")
        print("not the right word.")
        if w == "please":
            print("OK")
            break
    print(ctr)
    ctr += 1
"""

def fn(x):
    return 10*x

#print(fn(
#    999))

if (1 == 1 and
  2 == 2 and
  3 == 4):
    print("something")
    
# p. 339
# p. 343
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    # print(a + b + c)
    pass

for (a, b, c) in [[1, 2, 3], [4, 5, 6]]:
    # print(a + b + c)
    pass

j, *k = 't man'
j
k

start, *middle, end = [1,2,3,4,5,6,7]
start, middle, end

d = {'a': 1, 'b': 2, 'c': 3}
s, *b = sorted(d.keys())
b
s

"abc"[0:1]

a, *b = [1]
a
b
a,b = [1,2,3,4], [5, 6, 7, 8]
a

seq = [1,[20,30],4]
*a, = seq
a
seq
seq[1][0]=20000
a
seq[1:-1]

x = ['a','b']
y = 'cde'

x += y

x

f = open("pyout.txt", 'w')
f.write(str([1,2,3]))
f.close()

class FileFaker:
    def write(self, string):
        out = string*2
        print(".>." + out + ".<.")
        sys.__stdout__.write(out)

#import sys
#sys.stdout = FileFaker()
#print("abc")
#print([1,2])

# print("abc", file = FileFaker(), end="")

# p. 370 quiz
# 1. a = b = c = 9,
# 2. change in one affects other
# 3. in-place updates return None
# 4. print("...", file=f)

"""
if 1:
    print(1)
else:
    print(0)

a = 1
a
"""


# change in ernesto repo, wait for change in real repo

## change in real repo, commit then pull in side repo

def a(x):
    ...

# p. 391

# use 'break' to exit interactive loops (REPLs)

"""
while True:
    userin = input("Enter a letter: ")
    if userin == 'q':
        print("Bye.")
        break
    try:
        print(ord(userin))
    except:
        pass
"""

# while and else

"""
y = 999
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
"""

# use else instead of flags

"""
x = [1,3,5,7,1]
while x:
    if x[0] > 10:
        print("Found greater than 10")
        break
    x = x[1:]
else:
    print("all < 10")
"""

fns = {'add': lambda x, y: x + y, 'sub': lambda x, y: x - y}
fns['add'](3, 3)

choice = 'sub'
#print(fns[choice](2,3))
#(3+3)

def fn(x):
    return x*10
    
#(fn(9))

# import utility

# group([2,3,4,5,6,7,8,9],3)

"ab" "cd"

def isAnagram(x, y):
    def countLetters(s):
        return {c.lower(): s.count(c) for c in s.replace(' ', '')}
    return countLetters(x) == countLetters(y)

def somefun(a):
    print(a)

# somefun(a='abc'
#        'def')

# "abc" "def"

import adder as a
a.addmany(1,2,3)

from adder import adddict as ad
ad(good=2)


def rot13(source):
    def movechar(c):
        if ord(c) > 96:
            return chr(96+(ord(c)-96+13) % 26)
        else:
            return c
    return "".join([movechar(c) for c in source])

def getLength():
    desiredLength = 0
    while desiredLength < 1 or desiredLength > 9:
        try:
            desiredLength = int(input("enter a integer from 1 to 9: "))
        except:
            print("Please enter an integer from 1 to 9")
    return desiredLength
    
def generate(val):
    class S:
        c = val * 2
    return S
generate(9)().c

def f():
    pass


class Negativator:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args):
        return -self.fn(*args)
@Negativator
def f(x, y):
    return x + y
# is same as
# f = Negativator(f)
f(1, 2)
@Negativator
def g(x, y):
    return x - y
g(9, 1)

class Upperificator:
    def getwrapper(self, attrname):
        print("wrapper: ", attrname)
        # print(object.__getattribute__(self.instance, attrname))
        attrvalue = object.__getattribute__(self.instance, attrname)
        print(attrvalue, type(attrvalue))
        if isinstance(attrvalue, str):
            return attrvalue.upper()
        else:
            return object.__getattribute__(self.instance, attrname)()
    def __init__(self, cls):
        self.cls = cls
        self.cls.__getattribute__ = self.getwrapper
    def __call__(self, *args, **kwargs):
        self.instance = self.cls(*args, **kwargs)
        return self.instance
@Upperificator
class Robot:
    def __init__(self, name):
        self.name = name
    def getname(self):
        return self.name
# same as
# Robot = Upperificator(Robot)
n = Robot("Nick")
n.getname
n.getname()
n.__getattribute__('name')

class MyClass:
    data = 1
MyClass.__bases__
type(MyClass)
m = MyClass()
m.__class__
MyClass.__class__

def passed():
    print("passed")
def c():
    pass
def b():
    print("B")

def MyDecorator(y):
    y.a = 2
    return lambda: y
@MyDecorator
class A:
    a = 1
a = A
k = a()
k.a

import fractions
vars(fractions)

from collections import namedtuple
pt = namedtuple("Point", "x_pos y_pos")
a = pt(9.0, 10.0)
a.x_pos
