# card holder

class CardHolder:
    acctlen = 8
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr
    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)
    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 100:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)
    def getAcct(self):
        return self.__acct[:-3] + "***"
    def setAcct(self, value):
        value = value.replace("-", "")
        if len(value) != self.acctlen:
            raise TypeError("invalid acct number")
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)
    def remainGet(self):
        return self.retireage - self.age
    remain = property(remainGet)
#def loadclass():
#    import sys, importlib
#    modulename = sys.argv[1]
#    module = importlib.import_module(modulename)
#    print("[using %s]" % module.CardHolder)
#    return module.CardHolder
bob = CardHolder('1234-5999', 'bob smith', 40, 'main st')
bob.acct
bob.name
