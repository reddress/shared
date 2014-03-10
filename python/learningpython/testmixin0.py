from listinstance import ListInstance

class Super:
    def __init__(self):
        self.data1 = 'spam mixin 0'
    def ham(self):
        pass

class Sub(ListInstance, Super):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42
    def spam(self):
        pass

x = Sub()
print(x)
