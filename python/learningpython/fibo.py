def simplefib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return simplefib(n-1) + simplefib(n-2)

class nthfib:
    def __init__(self):
        self.memo = {0: 0, 1: 1}
    
    def fib(self, j):
        try:
            return self.memo[j]
        except:
            f = self.fib(j-1) + self.fib(j-2)
            self.memo[j] = f
            return f

def fibfactory():
    memo = {0: 0, 1: 1}
    def fibcalc(n):
        try:
            return memo[n]
        except:
            print("Calling fib(%s) + fib(%s)" % (n-1, n-2))
            f = fibcalc(n-1) + fibcalc(n-2)
            memo[n] = f
            print("Computing %s : %s" % (n, memo))
            return f
    return fibcalc

def fibiter(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[-1]
    
f = nthfib()
f.fib(30)
simplefib(30)

g = fibfactory()
g(20)

fibiter(20)
