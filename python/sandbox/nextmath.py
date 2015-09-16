# With a primitive function "next", equivalent to x += 1,
# write my_add, my_mult, and my_pow

def next(x):
    return x + 1

def my_add(x, y):
    total = x
    ct = 0
    while (ct < y):
        total = next(total)
        ct = next(ct)
    return total

def my_mult(x, y):
    total = 0
    ct = 0
    while (ct < y):
        total = my_add(total, x)
        ct = next(ct)
    return total

def my_pow(base, n):
    total = 1
    ct = 0
    while (ct < n):
        total = my_mult(total, base)
        ct = next(ct)
    return total

assert next(2) is 3, "2 + 1 != 3"
assert my_add(3, 2) is 5, "3 + 2 != 5"
assert my_mult(9, 9) is 81, "9 * 9 != 81"
assert my_pow(2, 8) is 256, "2 ^ 8 != 256"

def my_tetration(b, n):
    total = b
    ct = 0
    while (ct < n):
        total = my_pow(total, b)
        ct = next(ct)
    return total

my_tetration(2, 3)
