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

# get a list of all attributes available to the argument
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
