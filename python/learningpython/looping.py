### p. 388

"""
from random import randint

while randint(1,10) > 5:
    print("rolled > 5")
else:                    # executes if break not encountered
    print('exit loop')
"""

"""
# use break
while True:
    n = randint(1, 10)
    print(n)
    if n > 5:
        break
else:                    # never executed because of break
    print("exit loop")
"""

"""
x = "spam"
while x:
    print(x, end=">")
    x = x[1:]
"""

# p. 391

# use 'break' to exit interactive loops (REPLs)

"""
while True:
    userin = input("Enter a letter: ")
    if userin == 'q':
        print("Bye.")
        break
    try:
        print(ord(userin))
    except:
        pass
"""

# while and else

"""
y = 999
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
"""

"""
obj = [1,2,3,0,4,5]
while True:
    x = obj.pop()
    if not x: break
    print(x)
"""

a = [1,2,3,4]
for n in a:
    print(n)
else:
    print("done")
print("n =", n)

s = "asbd"
for c in s:
    print(ord(c))

T = [(1,3), (4,5), (6,9)]
for (a,b) in T:
    print(a + b)

D = {'a': 1, 'b': 2}
for (key, val) in D.items():
    print(key, "=>", val)

S = "abcdefghijk"
for c in S[::2]:
    print(ord(c))

L = [1,2,3]
K = [0,L,0]

L
K

i = 0
while i < len(L):
    L[i] += 1
    i += 1

L
K

L = [x + 1 for x in L]
L
K

[c * i for (i, c) in enumerate("abcd")]


# p. 412 run shell commands and retrieve output

import os
F = os.popen('dir')
for line in F:
    print(line)

F.close()

# p. 414 quiz
# 1. while is more general, for is used with iterables
# 2. break exits loop, continue jumps to the top of loop
# 3. after leaving while/for loop normally (without break)
# 4. use range or counter variable with while
# 5. indexing, skipping elements
