### p. 373
# an alternative to case/switch branching

choice = "ham"
print({'spam': 1.23,
       'ham': 9.99,
       'eggs': 2.30}[choice])

foods = {'spam': 1, 'ham': 2, 'eggs': 3}
foods[choice]

arith = {'add': lambda x, y: x + y, 'sub': lambda x, y: x - y}
arith['add'](2, 3)

# specifying a default
choice = "bread"
foods.get(choice, "no such item")

### p. 383
# convoluted ternary

X = True
X = False
Z = "z"
Y = "y"
#false, true value of X
A = [Z, Y][bool(X)]
A

# same as:
A = Y if X else Z
A

### p. 384
# short-circuiting
# use or for defaults

X = A or "the default"

# careful if both sides of or need to be run, call them or
# assign them to temporary variables.

### p. 385
# aggregate truth: any, all
L = [0,1,2,3]
any(L)
all(L)

### p. 385 quiz
# 1. if...elif...else or dictionary choices
# 2. x = y if a else z
# 3. () [] {} or backslash
# 4. boolean truth, or 1 and 0
