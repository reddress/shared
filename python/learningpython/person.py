# p. 818

from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + (percent/100)))
    def shout(self):
        print("I AM", self.name.upper())
#    def __repr__(self):
#        return '[Person: %s (%s), %s]' % (self.name, self.job, self.pay)

bob = Person('Bob smith')
sue = Person('Sue jones', job="dev", pay=10000)
print(bob.name, bob.pay)
print(sue.name, sue.pay)

if __name__ == '__main__':
    # self test code
    print(Person("Kate Ashley").name)

sue.giveRaise(5)
sue.pay

print(sue)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)  # avoid cut-paste old ver.

mary = Manager("Mary Anne", pay=20000)
print(mary)
mary.giveRaise(10)

class Assistant:
    def __init__(self, name, pay):
        self.person = Person(name, 'assist', pay)
    def giveRaise(self, percent, bonus=5):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)

a = Assistant("Alice Watson", 2000)
a.lastName()
a.giveRaise(10)
a

class Dept:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        print("type: %s" % type(self.members))
        for person in self.members:
            print(person)

devel = Dept(bob, sue)
devel.showAll()
devel.addMember(Manager("Harry", 30000))

class RedMage(Person):
    def __init__(self, name, *skills):
        Person.__init__(self, name, job="RM", pay=0)
        self.skills = skills

rm = RedMage("Tony", "fight", "black", 'white')
rm

