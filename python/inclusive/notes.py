# Notes for Learning Python, 5th ed.

# p. 96 Built-in objects
########################################################################

# Everything is a kind of object

# Contained in an outer list are the built-in objects:

# Numbers
from decimal import Decimal
from fractions import Fraction

[ 1, 2, 3+4j, Decimal(), Fraction() ]

# Strings
[ 'abc', "Bob's", r"raw\new", b'a\x01c_bytes', u'sp\xc4m' ]

# Tuples
from collections import namedtuple

[ (1, 'spam', 4, 'U'), tuple('abc') ] # is ('a', 'b', 'c')
TupleName = namedtuple('DisplayName', ['x', 'y'])
TupleName(1, 2)

# Lists
[ [1, [2, 'three'], 5.6], list(range(10))]

# Dictionaries
[ {'food': 'spam', 'name': 'Joe'}, dict(hours=10) ]

# Sets
[ set('abc'), {'a', 'c', 'b'} ]

# Files: open('eggs.txt'), open(r'C:\ham.bin', 'wb')

# Booleans
[ True, False ]

# Types
[ type(type), type(7) ]

# None
None

# Functions
def f(x):
    return x
g = lambda x: x * x

# Modules

# Classes

class MyClass:
    pass
    
# p. 97 Numbers
########################################################################

# Exponentiation is **
2 ** 3  # 8

# p. 99 Strings
########################################################################

s = 'The lazy dog'

# String length
len(s)

# Instead of a character type, s[n] returns another string
# Substrings are s[m:n], called slices. m and n are optional
# Last character is s[-1]
s[4:-4]  # lazy
s[4:]    # lazy dog

# concatenate strings with +
s + ' barks loudly'

# repeat strings with *
s * 3

# p. 101
# Strings are immutable. As an alternative, convert to list then ''.join(lst)
# or use bytearray(b'mystr')

# find substring in a string (returns -1 if not found)
s.find('dog')

# replace returns a new string
s.replace(' ', '-')

# other string methods
"1,2,3,Go".split(',')
'fred'.upper()
'bob'.isalpha()
'123'.isdigit()
" abc ".lstrip()  # remove whitespace
" abc ".rstrip()
' abc  '.strip()

# string formatting can be done in two ways
"%s, eggs, and %s" % ('Spam', 'Tomatoes')  # values are in a tuple
'{0}, eggs, and {1}'.format('spam', 'tomatoes')
'{}, eggs, and {}'.format('spam', 'tomatoes')  # numbers are optional

# p. 103
# generic operations spanning multiple types are usually built-in functions or
# expressions, but type-specific operations are method calls

# p. 104 Getting help
########################################################################

# get a list of all attributes, methods available to the argument
dir(s)

# get documentation for the argument
help(s.upper)

# p. 105
s = 'A\nB\tC'  # newline and tab
ord('A')       # get ASCII/Unicode
s = 'a\0b'     # zero byte

multiline = """The story of a boy
His name is Joe
He is a 1337 hacker
"""

unicode_spam = 'sp\xc4m'

id(s)  # get object's memory address

# p. 108 Pattern matching (regular expressions, regexes)
########################################################################

# considered too advanced for Learning Python

# a simple example
import re
match = re.match("Hello[ \t]*(.*) world", "Hello   Python world")
match.group(1)

# p. 109 Lists
########################################################################

lst = [123, 'spam', 1.23]
len(lst)  # 3

lst[0]
lst[:-1]         # slicing returns a new list
lst + [4, 5, 6]  # concatenation returns a new list
lst * 2          # repetition returns a new list

lst.index('spam')  # locate item
lst.index('nope')  # ValueError if nonexistent

lst.count(123)     # count occurrences of object

# type-specific operations (methods) alters the list in place
lst.append('zy') # adds to end of list, alters original list
lst

lst.pop(2)       # removes and returns item at given index
                 # default is last item

del(lst[2])      # same effect but returns nothing
lst

lst
lst.insert(2, 'eggs')  # inserts before given index
lst                    # object stays at given index.
# if index is greater than length, object is simply added to the end

# in-place sort and reverse
lst = [3, 9, 2, 5, -2, -4]
lst.sort()
lst.reverse()
lst

# p. 110 Lists may be nested in any manner, and include any objects

# p. 111 List comprehensions
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
mat
col2 = [row[1] for row in mat]  # does not alter mat
col2

[row[1] for row in mat if row[1] % 2 == 0]  # get even numbers

[c * 2 for c in 'spam']

list(range(-6, 6, 2))  # end value excluded in range, here step = 2

# comprehension in parentheses is used to create generator
gen = (sum(row) for row in mat)
gen  # generator object
next(gen)

# map objects does similar work
list(map(sum, mat))

# can also create sets and dictionaries
{sum(row) for row in mat}
{i: sum(mat[i]) for i in range(3)}

# p. 113 Dictionaries
########################################################################

# literal
d = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
d['food']

# changed in place
d['quantity'] += 1
d

# make dictionaries with dict
bob = dict(name="Bob", job="dev", age=40)
bob

# check if a key is in a dictionary
'lastname' in bob

# return a default value if key is not found
value = d.get('x', 'not found')
value

d['x'] if 'x' in d else 'not found'

# iterate through sorted keys of a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
d

for key in sorted(d):
    print(key, ': ', d[key])

# p. 121 Tuples
########################################################################

# tuples are immutable
t = (1, 2, 3, 4)

t + (5, 6)  # concatenation
t[-1]       # indexing

t.index(3)  # locate object
t.count(3)

t = (1,)    # one-element tuple must have trailing comma

# p. 122 Files
########################################################################

f = open('out.txt', 'w')  # 'w' indicates write mode, default 'r' read
f.write("Hello\n")
f.write("World\n")
f.close()

f = open('out.txt')
text = f.read()
text

# p. 128 testing for type
lst = [1, 2, 3]

if type(lst) == type([]):
    print('yes')

if type(lst) == list:
    print('yes')

if isinstance(lst, list):
    print('yes')

# p. 182 shared references
lst1 = [2, 3, 4]
lst2 = lst1

lst1[0] = 99  # affects lst2
lst2

# list in list
lst1 = [1, 2, [10, 20]]
lst2 = lst1[:]  # shallow copy

lst1[1] = 19
lst1[2][0] = 99
lst2

lst3 = lst1.copy()  # still shallow
lst1[2][0] = 999
lst3

import copy
lst4 = copy.deepcopy(lst1)  # deep copy
lst1[2][0] = 99
lst4

d1 = {'a': 1}
d2 = d1.copy()
d2

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst1 == lst2  # values are the same
lst1 is lst2  # arguments are the same object

# p. 206
# character codes and back
ord('s')
chr(65)

lst = ['m', 'ss', 'ss', 'pp']
'i'.join(lst)

s = 'a,man,a,plan'
s.split(',')

# string formatting
"I want %d %s" % (2, 'pies')

# p. 219
# %[(keyname)][flags][width][.precision]typecode
d = {'name': 'Joe'}
"His name is %(name)s" % (d)

# p. 255
# merge keys (overwrites old values)
d = {'a': 1, 'b': 2, 'c': 3}
d.update({'b': 20, 'd': 40})
d

# create dictionary from zip
dict(zip(['a', 'b'], [1, 2]))

dict.fromkeys(['a', 'b'], 10)  # create with default value

d.items()

# p. 410
# generate both offsets and items
s = "spam"
list(enumerate(s))
for (offset, character) in enumerate(s):
    print("%c appears in %d poaition" % (character, offset))

# p. 419
# manually iterate with next()
f = open("out.txt")
next(f)
f.close()

iter(f)  # obtains iterator object from iterable

# p. 591 Generator functions and expressions
########################################################################
def gensquares(n):
    for i in range(n):
        yield i ** 2

g = gensquares(9)
next(g)

def gensquaresinf():
    n = 0
    while True:
        yield n ** 2
        n += 1

g_inf = gensquaresinf()

import itertools
first5 = itertools.islice(g_inf, 5)
list(first5)

# p. 596
def gen():
    c = 10
    a = 1
    while True:
        a = (yield c) + 1000
        print("a: " + str(a))
        c = c + a
        print("c: " + str(c))

g = gen()
next(g)        # 10, result of yield c
g.send(3000)   # a depends only on value sent

# p. 596 send can be used to pass a termination code to the generator

def genloop():
    msg = "begin"
    while True:
        m = yield msg
        if m == 'break':
            break
        print(m.upper())

g = genloop()
next(g)
g.send(None)
g.send("hello")
g.send("break")

