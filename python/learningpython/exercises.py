# p. 467 Part III

# 1a.

s = 'spam'
for c in s:
    print(ord(c))

# 1b.

sum = 0
for c in s:
    sum += ord(c)
print(sum)

# 1c.

lst = []
for c in s:
    lst.append(ord(c))
lst

list(map(ord, s))

# 2.
for i in range(5):
    print("hello %d\n\a" % i)

# 3.
d = {'a': 1, 'b': 2, 'd': 4, 'c': 3}
for k in sorted(d):
    print(d[k])

# 4a.
L = [32, 1, 2, 4, 8, 16, 22, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i + 1
else:
    print(X, 'not found')

# 4b.
L = [1, 2, 4, 8, 16, 22, 32, 64]
X = 5
for n in L:
    if 2 ** X == n:
        print('at index', L.index(n))
        break
else:
    print(X, 'not found')

# 4c.
if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')

# 4d.
L = []
for i in range(6):
    L.append(2 ** i)
L

# 4e.
# place 2 ** X inside a variable

# 4f.
# yes

# 5 do not want to do
