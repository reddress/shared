class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary += self.salary * percent / 100
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "[Empl. %s, $%s]" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, 'makes food')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")

robo = PizzaRobot("Robo")
print(robo)
robo.work()
robo.giveRaise(20)
print(robo)

for C in Employee, Chef, Server, PizzaRobot:
    obj = C(C.__name__)
    obj.work()
    print(obj)

