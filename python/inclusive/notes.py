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
[ 'abc', "Bob's", r"raw\now", b'a\x01c', u'sp\xc4m' ]

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

