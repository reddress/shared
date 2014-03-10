from small import x, y

# from module import name1, name2
# is equivalent to:
# import module
# name1 = module.name1
# name2 = module.name2
# del module

import small
x = 42
x
y
y[0] = 42
small.x
small.__dict__
dir(small)
small.__file__
small.__name__
