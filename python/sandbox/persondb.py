import shelve

SHELF_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/sandbox/person.db"

persondb = shelve.open(SHELF_FILE)

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        # self.age = age
    def __str__(self):
        return self.name + " extra: " + str(self.height)

def populateAge():
    b = Person("Bob", 35)
    persondb["bob"] = b

def populateHeight():
    s = Person("Sarah", 170)
    persondb["sarah"] = s
    
def readage(id):
    return persondb[id].age

def readheight(id):
    return persondb[id].height
