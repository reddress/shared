# see wikipedia

from math import sqrt

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def estimate_pi(steps):
    c = (2 * sqrt(2)) / 9801
    sum = 0
    for k in range(steps):
        sum += (fact(4*k) * (1103 + 26390 * k))/(fact(k) ** 4 * (396 ** (4*k)))

    estimate = 1 / (c * sum)
    print(estimate)
    return estimate
    
