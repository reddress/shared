# tagged tag-topic

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
class Base:
    a = 1
    b = 2
b = Base()
w = Wrapper(b)
c = w.b
c

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

# tag-callable
def square(arg):
    return arg * arg
    
class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg

s = Sum(2)
p = Product(3)
actions = [square, s, p.method] # , CallToCompute]
#for act in actions:
#    print(act(5))

class CallToCompute:
    def __init__(self, x):
        print(x * 10)
    def __repr__(self):
        return "call to compute"

#c = CallToCompute(9)

table = {act(5): act for act in actions}
#for (key, value) in table.items():
#    print('{0:2} => {1}'.format(key, value))

table

# tag-factory tag-class-factory
# p. 954
def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)

class Solo:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job="Bum"):
        self.name = name
        self.job = job

obj1 = factory(Spam)
obj2 = factory(Person, "Arthur", "King")
obj3 = factory(Person, name="Brian")

obj3.name

# tag-attributes tag-getattr

class Character:
    def __init__(self, name, age, hp):
        self.name = name
        self.age = age
        self.hp = hp

joe = Character("Joe", 30, 120)
getattr(joe, "age")
joe.__dict__['hp']

# p. 988
# tag-getattr tag-attribute-interception
class C:
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)
    def __getitem__(self, i):
        return self.data[i]

x = C()
# x[0] # indexing fails in 3.x, because __getitem__ is not fetched
x.__getitem__(0)  # explicitly naming method works
x[1]
type(x).__getitem__(x, 2)

class G(type("a")):
    pass

g = G()
type(g)
G.__bases__

# p. 994
# tag-type-testing
class C: pass
class D: pass

c, d = C(), D()
type(c), type(d)
c.__class__, d.__class__
type(c) == c.__class__
c1, c2 = C(), C()
type(c1) == type(c2)
isinstance(c1, C)

type(object)
type(c1)
type(C)

type(type)
isinstance(type, object)
isinstance(object, object)
isinstance(9, object)
type("abc")

# tag-diamond
class A: attr = 'a'
class B(A): pass
class C(A): attr = 'c'
# class D(B, C): pass  # will get C.attr
class D(B, C): attr = B.attr  # prefer A.attr
x = D()
x.attr

class A:
    def meth(self): print('A.meth')

class C(A):
    def meth(): print("C.meth")

class B(C): pass

b = B()
#B.meth()

# tag-diamond tag-mro
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass
D.__mro__
A.__bases__
C.__bases__
D.__bases__
D.mro()

# tag-slots
class limiter:
    __slots__ = ['age', 'name', 'job']

x = limiter()
x.age = 30
# x.color = "blue"  # not in __slots__ , so is not allowed

class C:
    __slots__ = ['a', 'b']
    z = 3
    # a = 5  # conflicts with slot

c = C()
c.a = 9
c.a

# p. 1013 tag-slots
class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 3  # class attributes work normally
    def __init__(self):
        self.d = 4  # gets stored in __dict__

x = D()
x.d

getattr(x, '__slots__', [])

class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data

i = Slotful(3)
i.a, i.b = 1, 2
# i.a, i.b, i.c

# for a in (x for x in dir(i) if not x.startswith('__')):
#     print(a, getattr(i, a))

j = Slotful(90)
j.a = 'abc'
j.a

class A: __slots__ = ['a']
class B(A): __slots__ = ['b']

i = B()
i.a = 'a'
i.b = 'bb'
i.b
A.__dict__

# tag-getattr

class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = operators()
x.age

# tag-properties
class properties(object):
    def getage(self):
        return 42
    age = property(getage, None, None, None)  # get, set, del, docs
    # or age = property(getage)

x = properties()
x.age

# tag-descriptor
# p. 1023
class AgeDesc(object):
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance._age = value

class descriptors(object):
    age = AgeDesc()

x = descriptors()
x.age
x.age = 42
x._age

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of inst. created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(self):
        print("Num. instances. %s" % Spam.numInstances)

# a = Spam()
# a.printNumInstances()
# Spam().printNumInstances()
# Spam.printNumInstances(a)

# tag-static tag-classmethod
# p. 1029
# static requires no instance
# class method requires a class argument

class Methods:
    def imeth(self, x):
        print([self, x])
    def smeth(x):
        print([x])
    def cmeth(cls, x):
        print([cls, x])
    def py3staticmeth(y):
        print([y, y])
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

# Methods.smeth(3)
# Methods.cmeth(3)
# m = Methods()
# m.imeth(3)
# m.smeth(9)
# m.cmeth(4)
# m.py3staticmeth(9)  # does not work
# Methods.py3staticmeth(9)  # works

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("num. of inst. %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

a = Spam()
b = Spam()
#Spam.printNumInstances()

class Sub(Spam):
    def printNumInstances():
        print("extra stuff")
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

a = Sub()
b = Sub()
#a.printNumInstances()
c = Sub()
d = Spam()

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("num. instances (cls): %s %s" % (cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass 
    
x = Sub()
y = Spam()
# x.printNumInstances()
# y.printNumInstances()
# Sub.printNumInstances()
b = Spam()
z  = Other()
# z.printNumInstances()

class Spam:
    numInstances = 0
    def count(cls):
        cls.numInstances += 1
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numinst = 0
    # attribute numInstances gets created

x = Spam()
y1 = Sub()
x.numInstances
z = Other()
z.numinst
y1.numInstances
z.numInstances

# tag-decorator tag-staticmethod
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("inst: ", Spam.numInstances)

a = Spam()
# a.printNumInstances()

class Methods(object):
    @classmethod
    def cmeth(cls, x):
        print([cls, x])
        
    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__

obj = Methods()
# obj.cmeth("x")
obj.name

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call #%s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

@tracer
def spam(a, b, c):
    return a + b + c

# print(spam(1,2,3))
# print(spam('a','b','c'))

# tag-decorator tag-function-decorator
# p. 1038
def funtracer(func):
    def oncall(*args):
        oncall.calls += 1
        print("funtracer: call #%s to %s" % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @funtracer
    def spam(self, a, b, c): return a + b + c

@funtracer
def dbl(x):
    return x * 2

x = C()
#print(x.spam(1,2,3))
#print(dbl(12))

def hijack(f):
    return lambda x: print("all your logics are belong to us")

@hijack
def triple(x):
    return x * 3

#print(triple(9))
#triple(3)

def addfive(f):
    return lambda *args: f(*args) + 5

@addfive
def mulbyten(x,y):
    return (x + y) * 10

mulbyten(2,9)

def count(aClass):
    aClass.numInstances = 0
    return aClass

@count
class Spam:
    @classmethod
    def count(cls):
        cls.numInstances += 1
    def __init__(self):
        # Spam.numInstances += 1
        self.count()
    def printNumInstances(self):
        print(self.numInstances)

@count
class Sub(Spam):
    pass
        
c = Spam()
#c.printNumInstances()

d = Sub()
#d.printNumInstances()

# p. 1039
def upperator(cls):
    class Proxy:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name).upper()
    return Proxy

@upperator
class Student:
    def __init__(self, name, master):
        self.name = name
        self.master = master

st = Student("Joe", "Mr. Miyagi")
st.master

# tag-superclass

class C:
    def mul(self, m):
        print(self.val * m)

class D:
    def __init__(self, val):
        self.val = val

    def act(self, x):
        C.mul(self, x)
        print("D.act")

#x = D(30)
#x.act(9)

class C:
    def mul(self, m):
        print(self.val * m)
    def act(self):
        print("C.act")
class D(C):
    def act(self, x):
        super().mul(x)
        print("D with super")
    def __init__(self, val):
        self.val = val
#x = D(9)
#x.act(2)

class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        
# E().method()

class Base:
    def __init__(self):
        self.baseval = 1
#class Child(Base):
class Child:
    def __init__(self):
        Base.__init__(self)
        self.childval = 2
    def __str__(self):
        return "%s %s" % (self.baseval, self.childval)
#ch = Child()
#print(ch)

class A:
    def act(self):
        print("A")
class B(A):
    def act(self):
        print("B")
class C(B):
    def act(self):
        super().act()
c = C()
#c.act()

# tag-superclass tag-dynamic
class C(A):
    def m(self):
        super().act()
k = C()
#k.m()
C.__bases__ = (B,)
#k.m()

# alternative to super()
class C(A):
    def m(self):
        C.__bases__[0].act(self)

# tag-cooperative-super
# p. 1052
class A:
    def __init__(self):
        print("A.init")
class B(A):
    def __init__(self):
        print("B.init")
        super().__init__()
class C(A):
    def __init__(self):
        print("C.init")
        super().__init__()
        # super call is propagated as long as all classes do the same
        # without super, C "anchors the chain"
class D(B, C):
    pass
x = D()
# so passing super call along is an all-or-nothing tool

class A:
    def method(self):
        print("A.method")
        super().method()
class B(A):
    def method(self):
        print("B.method")
        super().method()
class C:
    def method(self):
        print("C.method")
        # super().method()  # anchors chain
class D(B, C):
    def method(self):
        print("D.method")
        super().method()
x = D()
x.method()

# tag-mixin tag-coupling
class A:
    def other(self): print("A.other")
class Mixin(A):
    def other(self): print("Mixin.other"); super().other()
class B:
    def method(self): print("B.method")
#class C(Mixin, B):
class C(B, Mixin):
    def method(self): print("C.method"); super().other(); super().method()
C().method()

# p. 1059
class A:
    def method(self): print("A.method")
class Mixin(A):
    def method(self): print("Mixin.method"); super().method()
class B(A):
    def method(self): print("B.method")
class C(Mixin, B):
    def method(self): print("C.method"); super().method()
C().method()

# tag-class-attributes
class X:
    a = 1
i = X()
i.a
j = X()
i.a = 2
j.a
X.a = 3

def generate():
    class Spam:
        count = "a"
        def __init__(self):
            self.count = "c"
        def __str__(self):
            return self.count
    return Spam()
g = generate()
print(g)

def generate(label):
    count = 99
    class Spam:
    count = 1  # must be called Spam.count, methods cannot see enclosing class
        def method(self):
            print("%s=%s" % (label, count))
    return Spam
aclass = generate("O rly?")
i = aclass()
i.method()

# tag-with tag-context-manager
class TraceBlock:
    def message(self, arg):
        print("running " + arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally')
        else:
            print('raise an exc. ' + str(exc_type))
            return False
with TraceBlock() as action:
    action.message('test 1')
    #raise TypeError
    print('reached')

# tag-multiple-with tag-with
# with open('data') as in, open('res') as out:

import os
import itertools
os.chdir("/home/heitor/python/learningpython")
with open('script1.py') as s1, open('script2.py') as s2:
    for pair in itertools.zip_longest(s1, s2, fillvalue="---"):
        print(pair)

# tag-format
testscripts=[dict(script="a.py", args="a"), dict(script="b.py", args="b")]
for t in testscripts:
    print("%(script)sthe script %(args)s" % t)

# tag-bytearray
ba = bytearray(b'abc')
ba += b'def'
ba + b'g'
ba += b'9'
ba

# tag-properties
class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print("get...")
        return self._name
    def setName(self, value):
        print("set...")
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")
bob = Person('bob smith')
print(bob.name)
del bob.name
bob.name = 'bob'

# tag-descriptor
class MyDescr:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep="\n")
class Subj:
    attr = MyDescr()
class Subj2:
    attr2 = MyDescr()
x = Subj()
x.attr
y = Subj2()
y.attr2

# tag-descriptor-read-only
class D:
    def __get__(*args): print ('get')
    def __set__(*args): raise AttributeError('cannot set')
class C:
    a = D()
X = C()
X.a
X.a = 99

class Name:
    "name descriptor docstring"
    def __get__(self, instance, owner):
        print("name--get")
        print(owner)
        return instance._name
    def __set__(self, instance, value):
        print("name--set")
        instance._name = value
    def __delete__(self, instance):
        print("name--delete")
        del instance._name
class Person:
    #def __init__(self, name):
    #    self._name = name
    def __init__(self):
        pass
    name = Name()
bob = Person()
bob.name = "Bobby"
print(bob.name)
s = Person()
s.name = "Sue jones"
print(s.name)
print(Name.__doc__)

class Super:
    def __init__(self, name):
        self._name = name
    name = Name()
class Person(Super):
    pass
p = Person("pam")
print(p.name)

# can also nest descriptor inside client class
class Person:
    def __init__(self, name):
        self._name = name
    class Name:
        "nested name descriptor docs"
        def __get__(self, instance, owner):
            print("fetch...")
            return instance._name
        def __set__(self, instance, value):
            print("change...")
            instance._name = value
        def __delete__(self, instance):
            print("remove...")
            del instance._name
    name = Name()
m = Person("Mary")
print(m.name)
print(Person.Name.__doc__)

class DescSquare:
    def __init__(self, start):
        self.value = start
    def __get__(self, instance, owner):
        return self.value ** 2
    def __set__(self, instance, value):
        self.value = value
class Client1:
    x = DescSquare(3)
class Client2:
    x = DescSquare(32)
c1 = Client1()
c2 = Client2()
print(c1.x)
print(c2.x)
c2.x = 9

class DescrOwnerData:
    def __init__(self, val):
        self.value = val
    def __get__(self, instance, owner):
        return owner.value
    def __set__(self, instance, val):
        self.value = val
class ClientOwner:
    data = DescrOwnerData(9)
    value = "ClientOwner value"
c = ClientOwner()
print(c.value)

# tag-descriptor-state tag-shared
class DescState:
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):
        print("DescState set")
        self.value = value        
class CalcAttrs:
    X = DescState(2)
    Y = 3
    def __init__(self):
        self.Z = 4
obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
CalcAttrs.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)
obj2 = CalcAttrs()
print(obj2.X, obj2.Y, obj2.Z)

class InstState:
    def __get__(self, instance, owner):
        print("inststate get")
        return instance._x * 10
    def __set__(self, instance, value):
        print("inststate set")
        instance._x = value
class CalcAttrs:
    x = InstState()
    y = 3
    def __init__(self):
        self._x = 2
        self.z = 4
obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.y = 10
print(obj.y)
obj.x = 5
obj.z = 9
print(obj.x, obj.y, obj.z)
obj2 = CalcAttrs()
print("obj2:", obj2.x, obj2.y, obj2.z)

class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return "%s, %s" % (self.data, instance.data)
    def __set__(self, instance, value):
        instance.data = value

class DProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)
class Person:
    def getName(self):
        print("getname...")
        return self.__dict__['name']
    def setName(self, value):
        print("setname")
        self.__dict__['name'] = value
    name = DProperty(getName, setName)
x = Person()
x.name = "Bob"
print(x.name)
x.name = "Steve"
print(x.name)

class DelToSet:
    def __delattr__(self, name):
        self.thevalue = 9
        self.__dict__[name] = 3
d = DelToSet()
del d.x
print(d.thevalue)
print(d.x)

# tag-wrapper
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print("Trace", attrname)
        print(getattr(self.wrapped, attrname))
        return getattr(self.wrapped, attrname)
x = Wrapper([1,2,3])
x.append(4)
print(x.wrapped)

class WithGetAttribute:
    def __init__(self, val):
        self.value = val
    def __getattribute__(self, name):
        x = object.__getattribute__(self, "value")
        return x
w = WithGetAttribute(9)
print(w.value)

# tag-attribute-generic
class Person:
    def __init__(self, name):
        self._name = name  # doesn't work as shown unless setattr has _name
    def __getattr__(self, attr):
        print("Get:", attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):
        print("set:", attr)
        if attr == 'name' or attr == '_name':
            attr = '_name'
            self.__dict__[attr] = value
            #object.__setattr__(self, attr, value)
    def __delattr__(self, attr):
        print("Del:", attr)
        if attr == 'name':
            attr = "_name"
        del self.__dict__[attr]
b = Person("bob")
print(b.name)
b.name = "bob smith"
s = Person("sarah")
print(s.name)

# override built-ins
class GetAttr:
    e = 88
    def __init__(self):
        self.spam = 77
    def __getattribute__(self, attr):
        print("get attr")
        if attr == '__str__' or attr == "__repr__":
            return lambda *args: '[Getattr str]'
g = GetAttr()
print(g.__str__())
g.x
g.__str__
print(g)

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[person %s]' % self.name
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus = 0.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)
sue = Person("sue jones", job="dev", pay=10000)
print(sue.lastName())
tom = Manager("tom jones", 50000)
print(tom)

# tag-decorator
def doubler(f):
    # return lambda x, y: 2 * (x + y)
    def double(*args):
        return 2 * f(*args)
    return double
@doubler
def f(x, y):
    return x + y
f(7, 9)
@doubler
def g(x, y):
    return x - y
g(9, 1)
@doubler
def h(x, y, z):
    return sum([x, y, z])
h(1, 2, 3)

# tag-decorator that uses classes
class AddOneDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        args_plus_one = map(lambda x: x + 1, args)
        return self.func(*args_plus_one)
@AddOneDecorator
def f(x, y):
    return x * y
f(3, 4)

def classdecorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            print("wrapper get attr")
            return getattr(self.wrapped, name)
    return Wrapper
@classdecorator
class C:
    def __init__(self, x, y):
        self.attr = "spam"
x = C(6, 7)
print(x.attr)

# tag-nested-decorators
def doubler(fn):
    def double(*args):
        return 2 * fn(*args)
    return double
def addten(fn):
    def adder(*args):
        return 10 + fn(*args)
    return adder
@doubler
@addten
def f(x, y):  # adds ten then doubles
    return x + y
f(10, 20)
@addten
@doubler
def g(x, y):  # doubles then adds ten
    return x + y
g(10, 20)

# tag-decorator-arguments
def multiplier(a, b):
    def actualDecorator(f):
        return lambda n: f(n) * a * b
    return actualDecorator
@multiplier(10, 10)
def f(n):
    return n
f(2)

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args)
@tracer
def spam(a, b):
    print(a + b)
    return a - b
spam(2, 3)

def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("wrapper call %s to %s" % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
@tracer
def spam(a, b, c):
    print(a + b + c)
spam(1, 2, 3)
@tracer
def eggs(a):
    print(a)
eggs(9)

# tag-decorator-descriptor
class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        return wrapper(self, instance)
class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)
@tracer
def spam(a, b):
    return a + b
spam(1, 2)
class Person:
    def __init__(self, pay):
        self.pay = pay
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1 + percent)
p = Person(100)
p.giveRaise(.10)
print(p.pay)
q = Person(200)
q.giveRaise(.20)  # call count is per class, not instance
print(q.pay)

import time
force = list
class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print("%s: %.5f %.5f" % (self.func.__name__, elapsed, self.alltime))
        return result
@timer
def listcomp(N):
    return [x * 2 for x in range(N)]
@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))
result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime)
print("")
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)

# tag-decorator-arguments p.1298
def timer(label="", times=1):
    def decorator(func):
        def onCall(*args):
            print(label * times)
            return func(*args)
        return onCall
    return decorator
@timer("==> ", 3)
def f(x):
    return x*2
print(f(9))

def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.clock()
            result = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = "%s %s: %.5f, %.5f"
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
@timer(label="[ccc]===>", trace=True)
def listcomp(N):
    return [x * 2 for x in range(N)]
listcomp(43)

# tag-class-decorator p. 1302
instances = {}
def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall
@singleton
class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        print(self.name)
@singleton
class Spam:
    def __init__(self, val):
        self.attr = val
bob = Person("Bob")
bob.getName()
sue = Person("Sue")
sue.getName()

class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance
@singleton
class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name.upper()
p = Person("Paul")
print(p.getName())
g = Person("Guy")
p

# tag-delegation p. 1304
class JustWrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print("Trace:", attrname)
        return getattr(self.wrapped, attrname)
x = JustWrapper([1,3,4])
x.append(4)
dir([1,2])
class MyObj:
    def __init__(self, v):
        self.v = v
y = JustWrapper(MyObj(9))
print(y.v)

def Tracer(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = cls(*args, **kwargs)
        def __getattr__(self, attrname):
            print("Trace:", attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper
@Tracer
class Spam:
    def display(self):
        print("spam")
@Tracer
class Person:
    def __init__(self, name):
        self.name = name
    def getname(self):
        return self.name.upper()
food = Spam()
food.display()
print([food.fetches])

# tag-manager-function
class Person:
    def __init__(self, name):
        self.name = name
instances = {}
def getInstance(aClass, *args, **kwargs):
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)
    return instances[aClass]
bob = getInstance(Person, "Bob")
bob.name
sarah = getInstance(Person, "Sarah")
sarah.name

# tag-decorator-register p. 1312
registry = {}
def register(obj):
    registry[obj.__name__] = obj
    return obj
@register
def spam(x):
    return x ** 2
@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 3
    def __str__(self):
        return str(self.data)
print("Registry")
for name in registry:
    print(name, ">>", registry[name], type(registry[name]))
print("manual calls")
print(spam(2))
x = Eggs(2)
print(x)
y = Eggs(20)
print(y)
print("registry calls")
for name in registry:
    print(name, '=>', registry[name](2))
Eggs.__name__

# tag-decorator-argument p. 1314
def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate
@annotate("spam data")
def spam(a, b):
    return a + b
spam(1, 2), spam.label

# tag-decorator tag-privacy p. 1315
traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')
def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attr fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attr. change. ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorator
traceMe = True
@Private('data', 'size')
class Doubler:
    def __init__(self, label, start):
        self.label = label
        self.data = start
    def size(self):
        return len(self.data)
    def double(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * 2
    def mult(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * self.size()
    def display(self):
        print("%s => %s" % (self.label, self.data))
x = Doubler('x is', [1,2,3])
y = Doubler('y is', [-2,-3,-4])
print(x.label)
x.display()
y.display()
x.mult()
x.display()

traceMe = True
def trace(*args):
    if traceMe: print('[' + " ".join(map(str, args)) + ']')
def accessControl(failif):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get', attr)
                if failif(attr):
                    raise TypeError("private attr. fetch " + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failif(attr):
                    raise TypeError("private attr change " + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator
def Private(*attributes):
    return accessControl(failif=lambda attr: attr in attributes)
def Public(*attributes):
    return accessControl(failif=lambda attr: attr not in attributes)
@Public('age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
f = Person('Fred', 20)
f.age
f.name

# p. 1331
def rangetest(*argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = "arg %s not in %s..%s" % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
@rangetest((1, 0, 120))
def persinfo(name, age):
    print(name, "is", age, "years old")
persinfo('joe', 90)

# tag-introspection
def f(*args):
    return args[0]
code = f.__code__
code.co_varnames

class Meta(type):
    def __new__(meta, classname, supers, classdict):
        return type.__new__(meta, classname, supers, classdict)

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print("In MetaOne.new:", meta, classname, supers, classdict, sep="\n...")
        return type.__new__(meta, classname, supers, classdict)
class Eggs:
    pass
print('making class')
class Spam(Eggs, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg
print('making instance')
x = Spam()
print('data:', x.data, x.meth(2))

class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print("in metatwo.new: ", classname, supers, classdict, sep="\n...")
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print("in metatwo init: ", classname, supers, classdict, sep="\n...")
        print("...init class obj.", list(Class.__dict__.keys()))
class Eggs:
    pass
print('making class')
class Spam(Eggs, metaclass=MetaTwo):
    data = 1
    def meth(self, arg):
        return self.data + arg
print("making instance")
x = Spam()
print("data:", x.data, x.meth(2))

def MetaFunc(classname, supers, classdict):
    print("in metafunc:", classname, supers, classdict, sep="\n...")
    return type(classname, supers, classdict)
class Eggs:
    pass
print("making class")
class Spam(Eggs, metaclass=MetaFunc):
    data = 1
    def meth(self, arg):
        return self.data + arg
print("making instance")
x = Spam()
print("data:", x.data, x.meth(2))

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print("in metaobj call")
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class
    def __New__(self, classname, supers, classdict):
        print("in metaobj New:")
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print("in metaobj.init")
        print("... init class obj", list(Class.__dict__.keys()))
class Eggs:
    pass
print("making class")
class Spam(Eggs, metaclass=MetaObj()):
    data = 1
    def meth(self, arg):
        return self.data + arg
print("making instance")
x = Spam()
print("data", x.data, x.meth(2))

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print("in Supermetaobj call", classname, supers, classdict, sep="\n...")
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class
class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print("in submetaobj.new", classname, supers, classdict, sep="\n...")
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print('in submetaobj init')
        print("init class obj.", list(Class.__dict__.keys()))
class Eggs:
    pass
class Spam(Eggs, metaclass=SubMetaObj()):
    data = 1
    def meth(self, arg):
        return self.data + arg
x = Spam()
x.meth(9)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print("in super meta call", classname)
        return type.__call__(meta, classname, supers, classdict)
class SubMeta(SuperMeta):
    def __init__(Class, classname, supers, classdict):
        print("in submeta init", classname)
print(SubMeta.__class__)
print(SubMeta.__call__)
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})

# p. 1379 # tag-meta-instance
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print("in metaone new", classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        return 'toast'
class Super(metaclass=MetaOne):
    def spam(self):
        return 'spam'
class Sub(Super):
    def eggs(self):
        return 'eggs'
x = Sub()
x.eggs()
x.toast()
x.spam()
Sub.toast()
Super.toast()
dir(Super)

class M(type): attr = 1
class N(M): pass
class A: attr = 2
class B(A): pass
class C(B, metaclass=N): pass
class D(C): pass
I = C()
I.__class__
C.__bases__
C.__class__
B.__class__
D.__class__
M.__class__
N.__class__
N.__bases__

class M1(type): attr1 = 1
class M2(M1): attr2 = 2
class C1: attr3 = 3
class C2(C1, metaclass=M2): attr4 = 4
I = C2()
I.attr3, I.attr4
C2.attr4, C2.attr1
M2.__class__
M1.__class__
I.__class__.attr1

class P:
    a = 1
x = P()
P.__bases__
# x.__bases__  # does not have them

# tag-descriptor p. 1385
class D:
    def __get__(self, instance, owner): print('get')
    def __set__(self, instance, value): print('set')
    # removing __set__ makes 'd' hide this name in its class
class C:
    d = D()
I = C()
I.d
I.__dict__['d'] = "spam"
I.__dict__['d']
I.d

# tag-built-in
class C:
    attr = 1
    def __str__(self):
        return("class C")
I = C()
I.__str__(), str(I)
I.__str__ = lambda: "instance"
I.__str__(), str(I)
I.__str__

class D(type):
    def __str__(self): return("D class")
class C(metaclass=D):
    pass
C.__str__

class A(type):
    def a(cls):
        cls.x = cls.y + cls.z
class B(metaclass=A):
    y, z = 11, 22
    @classmethod
    def b(cls):
        return cls.x
B.a() 
B.x

class A(type):
    adata = "A"
class B(metaclass=A):
    bdata = "B"
i = B()
i.bdata
dir(B)
dir(B.__class__)
B.__class__

class Client1:
    def __init__(self, value):
        self.value = value
    def spam(self):
        return "spam"
def eggsfunc(obj):
    return obj.value * 4
Client1.eggs = eggsfunc
c = Client1(9)
c.eggs()
Client1.eggs
c.ham("ab")
Client1.ham = lambda self, s: s.upper()
dir(Client1)
Client1.__dict__

# tag-metaclass-extender p. 1393
def eggsfunc(obj):
    return obj.value * 4
def hamfunc(obj, value):
    return value + 'ham'
class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)
class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2
x = Client1("A")
print(x.spam())
print(x.ham('bacon'))
def DecorExtender(cls):
    cls.eggs = eggsfunc
    cls.ham = hamfunc
    return cls
@DecorExtender
class Client2:
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2
c2 = Client2(2)
c2.eggs()
c2.ham("h")

# p. 1398
class Metaclass(type):
    def __new__(meta, clsname, supers, attrdict):
        print('in M.new')
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)
def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))
class A:
    x = 1
@decorator
class B(A):
    y = 2
    def m(self):
        return self.x + self.y
b = B()
b.y
b.m()

def spammeta(name, supers, attrs):
    return 'spam'
class C(metaclass=spammeta):
    attr = "huh?"
C.attr

from types import FunctionType
def Tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall
class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = Tracer(attrval)
        return type.__new__(meta, classname, supers, classdict)
class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= 1.0 + percent
    def lastName(self):
        return self.name.split()[-1]
b = Person("Bob", 20000)
s = Person("Sue", 30000)
print(b.name, s.name)
s.giveRaise(0.10)
print(s.pay)

# tag-metaclass-decorate-all
from types import FunctionType
def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall
def decorateAll(decorator):
    class MetaDecorate(type):  # the metaclass
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate
class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name):
        self.name = name
    def lastName(self):
        return self.name.split()[-1]
c = Person("Carl Smith")
c.lastName()

"""
List of "magic" features p. 1410
Generators, decorators, slots, properties, descriptors, metaclasses, context managers, closures, super, namespace packages, Unicode, function annotations, relative imports, keyword-only arguments, class and static methods, and even obscure applications of comprehensions and operator overloading
"""

# self-study examples p. 1499

