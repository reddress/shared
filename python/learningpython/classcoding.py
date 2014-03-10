class SharedData:
    s = 42

x = SharedData()
y = SharedData()

x.s += 100  # does not change other instances, but attaches a name to x
            # otherwise, x.s looks up value in class by inheritance
            # inheritance happens on reference, not assignment
x.s
y.s

SharedData.s += 1  # changes all instances
x.s
y.s

class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)

x = MixedNames(1)
x.display()

MixedNames.display(x)

class MyClass:
    def classOnly():
        print("class only")

d = MyClass()
MyClass.classOnly()

class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')
        # or: assert False, 'action must be defined'
        # assert checks if statement is False, if so, raises an error

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    def method(self):
        print("start Extender.method")
        Super.method(self)
        print("end Extender.method")

class Provider(Super):
    def action(self):
        print("in Provider.action")

for klass in (Inheritor, Replacer, Extender):
    print("\n" + klass.__name__ + '...')
    klass().method()
print('\nProvider: ')
x = Provider()
x.delegate()

Inheritor.__name__

y = Extender()
# y.delegate()

x = 11

def f():
    print(x)

def g():
    x = 22
    print(x)

class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55
        print(x)

g()
C.x
k = C()
k.m()
k.x

x = 11
def h2():
    x = 33
    def nested():
        global x
        x = 66
    nested()

x
h2()
x

"""
p. 884 quiz
1. a class that delegates actions to its subclasses
2. becomes a class attribute
3. it is not automatically called, so manual calls execute its statements
4. call the superclass' method
5. it is not looked at, does not belong in LEGB rule
6. Johmama
"""

class MyClass:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return str(self.n)

m = MyClass(9)
m
n = m.__class__(8)
n
