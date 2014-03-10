# p. 981

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset-1)

def testMyList():
    print(list('abc'))
    x = MyList('abc')
    print(x)

    print(x[1])
    print(x[3])
    print(x[0])

testMyList()
