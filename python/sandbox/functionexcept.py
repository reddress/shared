def divide(x):
    try:
        print(3/x)
    except AttributeError:
        print("Exception")

class MyObj:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
m = MyObj(1,2)

def read(m):
    try:
        print(m.a)
        print(m.c)
    except ZeroDivisionError:
        print("m exception")

read(m)
