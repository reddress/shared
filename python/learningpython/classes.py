# p. 514 preview
class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1

H = tester(99)
# H('spam')
H.a = 2
H.a

H
class SubTester(tester):
    f = 3

s = SubTester(2)
s.f

class C2:
    ...

class C3: ...

class C1(C2, C3):
    def setname(self, who):
        self.name = who

I1 = C1()
I1.setname("bob")
I1.name

class likeRat:
    # since ints are immutable, need to override __new__
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def toFloat(self):
        return self.numer/self.denom
n = likeRat(2,3)
n.toFloat()

class Person:
    def __init__(self, name):
        self.name = name
    population = 0
        
class Worker(Person):
    def __init__(self, name, salary):
        super().__init__("worker: " + name)
        Person.population += 1
        self.salary = salary
    def __str__(self):
        return self.name + " salary: " + str(self.salary)
    def giveRaise(self,percent):
        self.salary *= 1 + (percent/100)

j = Worker("John", 299)
# print(j)
j.giveRaise(20)
j.population
Person.population
k = Worker("Kay", 200)
l = Worker("larry", 200)

"""
p. 795 quiz
1. code reuse and conceptualizing real world objects
2. bottom up and left-to-right in inheritance tree
3. class obj. is like a factory that creates instances
4. refers to the caller
5. initialization when creating instance
6. call class name as a function
7. class name(superclasses):
8. inside parentheses
"""

# p. 799
class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("king")
y.setdata(133)

y.display() #prints
x.data = "new val"
x.display()

class SecondClass(FirstClass):
    def display(self):
        print("second class : %s" % self.data)

z = SecondClass()
z.setdata(33)
z.display()

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return "third class %s" % self.data
    def mul(self, other):
        self.data *= other

class ThirdAndHalf(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdAndHalf(self.data + other.data)
    def __str__(self):
        return "%s" % self.data
        
a = ThirdClass('abc')
a.display()
print(a)
b = a + 'def'
print(b)
b.mul(3)

d = ThirdAndHalf(9)
e = ThirdAndHalf(10)
f = d + e + e
print(f)

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs, self.age)

rec2 = Person('Sue', ['dev', 'cto'])
rec2.info()

"""
p. 815 quiz
1. create namespaces
2. classes create instances
3. either in its definition or through class.attr
4. through init or outside, with instance.attr
5. the caller, implied subject of method call
6. by defining same named function or defining __op__ functions
7. to mimic built-in functionality
8. __init__
9. inheritance tree and that they are objects like other things

p. 855 quiz
1. from the loaded class info
2. the shelve loads the module
3. avoid redundancy, when logic changes you need to change only one place
4. same as 3.
5. same as 3.
6. same as 3.
7. ? used for directing by controller layer, composition passes down to
   delegate, while inheritance passes up
8. shelve keys 
9. change pay to phone numbers
"""

"""
p. 1071 quiz
1. subclass, wrapper
2. add extra logic and modify attributes
3. add (object) in 2.x, in 3.x all are new-style
4. mro, new-style always have object at root
5. static methods do not require instance first argument
6. yes, but both may need to be used everywhere to be useful
7. ..
"""
