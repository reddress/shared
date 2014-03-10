# p. 1072
class Adder:
    def add(self, x, y):
        print("Not Implemented.")
    def __init__(self, data):
        self.data = data

class ListAdder(Adder):
    def add(self, arg1, arg2):
        return arg1 + arg2
    def __add__(self, other):
        return self.add(self.data, other)

class DictAdder(Adder):
    def add(self, d1, d2):
        for key in d2:
            d1[key] = d2[key]
        return d1

la = ListAdder(1)
la.add([1],[3,4])
la.data

# 2. ans. see p. 1490
# my answer
class MyList(list):
    def __init__(self, start=[]):
        self.data = start[:]
        list.__init__(start)
    def __repr__(self):
        return repr(self.data)
m = MyList([1,2,3])
m.data
m
n = MyList(m)
n.data
k = list.__init__([1])
print(k)

# book answer
class MyList:
    def __init__(self, start):
        self.wrapped = list(start)
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __repr__(self):
        return repr(self.wrapped)
x = MyList("spam")
x + ["eggs"]

# 3. p. 1073
class MyListSub(MyList):
    addcounter = 0
    def __add__(self, other):
        MyListSub.addcounter += 1
        MyList.__add__(self, other)
    def getcount(self):
        return MyListSub.addcounter
    # for per-instance counter, initialize addcounter in __init__ and
    # update self.addcounter.
mls = MyListSub([1])
mls2 = MyListSub([2])
mls + ['a']
mls2 + ['b']
print(mls.getcount())

# 4. p. 1073
class Attrs:
    def __setattr__(self, attr, val):
        print("setting %s to %s" % (attr, val))
        self.__dict__[attr] = val
    def __getattr__(self, attr):
        print("getting %s" % attr)
        return self.__dict__[attr] * 2
a = Attrs()
a.val = "1"
b = Attrs()
a.val  # does not call "getting %s", must wrap (see Wrapper in tagged.py)
a.__dict__
[name for name in dir(a) if not name[0] == "a"]

# 5 solution on p. 1493
a = set([1,2,3])
b = set([1,3,5,10,20])
a & b
a | b
z = set("mississippi")
for k in z:
    print(k)
z & set("massachussets")
class SetSubclass(set):
    def __init__(self, *args):
        self.set = set(args)
    def __repr__(self):
        return repr(self.set)
    def __and__(self, other):
        return SetSubclass(*list(self.set & other.set))
ssc = SetSubclass(1,2,3)
ssc
ssc2 = SetSubclass(3,2,4,6)
ssc3 = SetSubclass(2)
type(ssc3)
ssc4 = ssc & ssc3 & ssc
ssc4

# 6. p. 1074
# for super in self.__class__.__bases__:
#    names.append(super.__name__)

# 7. p. 1075
class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        print(self.customer.food)
class Customer:
    def __init__(self):
        pass
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)
    def printFood(self):
        pass
class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)
class Food:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
lunch = Lunch()
lunch.order("Mega Burger")
lunch.result()

# 8. p. 1075, solution p. 1496
class Animal:
    def reply(self):
        self.speak()
class Mammal(Animal):
    pass
class Cat(Mammal):
    def speak(self):
        print("meow")
class Dog(Mammal):
    def speak(self):
        print("woof")
class Primate(Mammal):
    def speak(self):
        print("Ook! Ook!")
class Hacker(Primate):
    #def speak(self):
    #    print("Hello world")
    pass
spot = Cat()
spot.reply()
h = Hacker()
h.reply()

# 9.
class Customer:
    def line(self):
        print("thats one ex-bird")
class Clerk:
    def line(self):
        print("no it isn't")
class Parrot:
    def line(self):
        print("None")
class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()
    def action(self):
        for actor in self.__dict__:
            print(actor, ":", end="")
            self.__dict__[actor].line()
s = Scene()
s.__dict__
s.action()
