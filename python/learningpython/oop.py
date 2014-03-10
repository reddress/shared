# tag-delegate
# p. 942
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1,2,3])
#x.append(4)
x.wrapped

# tag-collision tag-privacy
# p. 945
class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)
    def method(self): print("C1 method")

class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)
    def __method(self): print("C2 method")

class C3(C2, C1):
    def actions(self): self.method()  # runs C1 method

I = C3()
I.meth1()
I.metha()
#I.meth2()
#I.methb()
#print(I.__dict__)

#I.actions()

# tag-method tag-bound
# unbound methods are function attributes of a class, do not have self.
# called by qualifying the class. must explicitly provide an instance
# object as the first argument.
# In python 3, unbound methods are simple functions
#
# bound methods are instance methods. the instance is packaged and passed
# as the first (self) argument of the method.

class Spam:
    def doit(self, message):
        print(message)

class Maps:
    def didit(self, massage):
        print(massage)

s = Spam()
m = Maps()
f = Spam.doit
#f(s, "the massage")

# tag-unbound
class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(arg1, arg2):
        return arg1 + arg2
    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2

x = Selfless(2)
x.normal(3,2)
Selfless.normal(x, 3, 4)
Selfless.selfless(3,4)

# tag-bound-method
class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

x = Number(2)
y = Number(3)
z = Number(4)
x.double()
acts = [x.double, y.double, y.triple, z.triple]
#for act in acts:
#    print(act())

# tag-method tag-bound
# can access instance and method function
bound = x.double
bound.__self__.triple()
bound.__func__(bound.__self__)

