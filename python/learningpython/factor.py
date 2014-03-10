import math

def factor(n):
    if n < 2:
        return [1]
    else:
        for i in range(1, n+1):
            print i
            if n % i == 0:
                return [i] + factor(int(n/i))
                break
                                
