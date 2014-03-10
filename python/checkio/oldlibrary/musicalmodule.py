def gcd(a,b):
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, a%b)

gcd(14, 21)
