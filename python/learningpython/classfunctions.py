class MyClass:
    def double(x):
        return x * 2

    def __init__(self, val):
        self.val = val

    def __str__(self):
        # return str(double(self.val))  # err: global name 'double' not defined
        # return str(self.double(self.val))  # err: self passed as 1st arg.
        return str(MyClass.double(self.val))  # works

m = MyClass(3)
print(m)


class WithDecorator:
    def __init__(self, val):
        self.val = val
    @staticmethod
    def triple(x):
        return x * 3
    def __str__(self):
        return str(self.triple(self.val))
        # works because triple declared static

w = WithDecorator(3)
print(w)
