# fibonacci generators

def fib():
    base1 = 0
    base2 = 1
    while True:
        yield base2
        base1, base2 = base2, base1 + base2
        
