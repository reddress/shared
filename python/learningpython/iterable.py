# p. 899 object supporting multiple iterations

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipYield:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
            
sy = SkipYield('abcdef')
i = iter(sy)
next(i); next(i)

def testSkipObj():
    contents = 'abcdef'
    skipper = SkipObject(contents)
    i = iter(skipper)
    print(next(i), next(i), next(i))

    for x in skipper:
        for y in skipper:
            print(x + y, end=" ")

# testSkipObj()

def gen(x):
    for i in range(x): yield i ** 2

g = gen(5)
i = iter(g)
j = iter(g)

next(i)
next(j)
list(g)
# list(gen(5))

# p. 902 combine __iter__ and yield: multiple generators, multiple scans

class SquaresYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

s = SquaresYield(1, 5)
i = iter(s)
next(i)
j = iter(s)
next(j)

#for i in s:
#    print(i)

