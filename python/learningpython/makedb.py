from person import Person, Manager

bob = Person("Bob Smith")
sue = Person("Sue Jones", job='dev', pay=10000)
tom = Manager("Tom Lane", 40000)

import shelve
db = shelve.open('python/persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

dir(tom)
bob.shout()
