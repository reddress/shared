def dividebyzero():
    try:
        a = 1 / 0
        
    finally:
        print("finally")

def fetcher(obj, index):
    try: 
        return obj[index]
    except IndexError:
        print("index out of range")
    except TypeError:
        print('enter an integer index')
    except:
        print('something else is wrong')
x = 'spam'
fetcher(x, 3)
fetcher(x, 'a')
fetcher(x, 9)
fetcher(3, 3)

class AlreadyGotOne(Exception): pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print("got exception")

class CustomMsgException(Exception):
    def __str__(self): return "custom exception message"

#raise CustomMsgException()

def simplefetch(obj, index):
    return obj[index]
    
def after():
    try:
        simplefetch("ab", 3)
    finally:
        print("after fetch")
    print("after try?")
after()

"""
p. 1090 quiz

1. avoid sending status codes, provide uninterrupted flow, add meaningful
error messages
2. is handled by default handler and terminates program
3. catch it (except)
4. raise, assert
5. finally or with/as
"""

try:
    a = 1/3
except IndexError:
    print("index error")
else:
    print("no error")

try:
    1/0
except Exception as X:
    print(X)
    saveit = X
X
saveit

try:
    1/0
except Exception as E:
    raise TypeError('bad') from E

try:
    try:
        9/0
    except:
        badname
except:
    open('none')

import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 3
    x = decimal.Decimal('1.3')/decimal.Decimal('3.00')
    print(x)

try:
    1/0
except Exception:
    import sys
    print(sys.exc_info())

try:
    'abc'[9]
except Exception as E:
    print(E.__class__)

class E(Exception): pass
try:
    raise E('spam', 39)
except E as Exc:
    print(repr(Exc))

class E(Exception):
    def __str__(self):
        return "called"
raise E('something else')

class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
def parser():
    raise FormatError(42, "spam.txt")
try:
    parser()
except FormatError as F:
    print("error at %s, line %s" % (F.file, F.line))

# exceptions can open log file and write to it
class FormatError(Exception):
    def logerror(self):
        print("open log file and write to it")
try:
    raise FormatError
except FormatError as FErr:
    print(sys.exc_info())
    FErr.logerror()

def raise1(): raise IndexError
def noraise(): print(" no raise")
def raise2(): raise SyntaxError
for func in (raise1, noraise, raise2, noraise):
    print("func: %s" % func.__name__)
    try:
        try:
            func()
        except IndexError:
            print("caught index error")
    finally:
        print("finally run")
    print("end")
