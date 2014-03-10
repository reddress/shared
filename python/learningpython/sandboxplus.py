# continuation of sandbox

print(1+1)

def fun1():
    return "fn 1"

def fun2():
    return "fn 2"

for fn in [fun1, fun2]:
    print(fn.__name__)
