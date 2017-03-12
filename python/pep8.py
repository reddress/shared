def o_rly(var_one,
          var_two):
    pass

class MyDbl:
    def __init__(self, val=1):
        self.val = val
    def double(self):
        return MyDbl(self.val*2)

c = MyDbl()

c.double()  # 2

d = (c.double()  # 2 
     .double()   # 4
     .double()   # 8
     .double())  # 16

naming_conventions = """

modules should have short, all-lowercase names. underscores can be used to improve readability.

packages should also have short, all-lowercase names, although underscores are discouraged.

class names use CamelCase

function names, method names and variables use snake_case

"""
