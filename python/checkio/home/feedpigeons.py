class Pigeon:
    def __init__(self, name):
        self.ate = 0
        self.name = name
    def fed(self):
        return bool(self.ate)
    def eat(self):
        self.ate += 1

class Yard:
    def __init__(self, food):
        self.food = food
        self.pigeons = [Pigeon("my pigeon")]  # my pigeon
        self.time = 2
    def tick(self):
        for p in self.pigeons:
            if self.food > 0:
                self.food -= 1
                p.eat()
        for i in range(self.time):
            self.pigeons.append(Pigeon("min. " + str(self.time) + " Pigeon " +
                                       str(self.time)))
        self.time += 1
    def describe(self):
        print("-"*30, "minute", self.time-2)
        print("Yard with %s food" % self.food)
        for p in self.pigeons:
            print("%s ate? %s - %s" % (p.name, p.fed(), p.ate))
    def countfedpigeons(self):
        return list(map(Pigeon.fed, self.pigeons)).count(True)
        
def checkio(number):
    yard = Yard(number)
    while yard.food > 0:
        yard.tick()
    print("Fed pigeons: " + str(yard.countfedpigeons()))
    return yard.countfedpigeons()
    
checkio(90)
