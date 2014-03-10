import re

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.cleanup()

    def cleanup(self):
        if self.coeffs[len(self.coeffs)-1] == 0:
            cleaned = []
            rev = self.coeffs[::-1]
            first_nonzero = -1
            for n in range(len(rev)):
                if rev[n] == 0:
                    first_nonzero += 1
                else:
                    break
            self.coeffs = rev[:first_nonzero:-1]
        else:
            pass
        
    def xstring(self, power):
        return "*".join(["x" for i in range(power)])
        
    def __str__(self):
        output = ""
        out_list = []
        rev_coeffs = self.coeffs[::-1]
        degree = len(rev_coeffs) - 1
        for inx, coeff in enumerate(rev_coeffs):
            if abs(coeff) > 0:
                if coeff > 0:
                    output += "+"
                
                if degree - inx == 0:
                    output += str(coeff)
                else:
                    xs = self.xstring(degree - inx)
                    if coeff == 1:
                        output += xs
                    elif coeff == -1:
                        output += "-" + xs
                    else:
                        output += str(coeff) + "*" + xs
        return output[1:]

    def __add__(self, other):
        if len(self.coeffs) > len(other.coeffs):
            longer = self.coeffs[:]
            shorter = other.coeffs[:]
        else:
            longer = other.coeffs[:]
            shorter = self.coeffs[:]
        for i in range(len(shorter)):
            longer[i] += shorter[i]
        return Polynomial(longer)

    def __mul__(self, other):
        result = [0 for i in range(len(self.coeffs) + len(other.coeffs) - 1)]
        for power, coeff in enumerate(self.coeffs):
            for power_oth, coeff_oth in enumerate(other.coeffs):
                result[power + power_oth] += coeff * coeff_oth
        return Polynomial(result)

    def __sub__(self, other):
        negated = other.coeffs[:]
        for i in range(len(negated)):
            negated[i] = -negated[i]
        return self + Polynomial(negated)

def checkio(expr):
    pattern = "([0-9]+)"
    replacement = r"Polynomial([\1])"
    const_sub = re.sub(pattern, replacement, expr)
    return eval(const_sub.replace("x", "Polynomial([0,1])"))

    
p1 = Polynomial([3,2])
p2 = Polynomial([2])
p3 = Polynomial([0,-1,0,0,1])
print(p1*p2)
print(p1 * p2 + p3)

p4 = Polynomial([3,4])
p5 = Polynomial([1,1,1])
print(p4-p5)
print(p4)
print(p5)

input = "(x-1)*(x+1)"
pattern = "([0-9]+)"
replacement = r"Polynomial([\1])"
const_sub = re.sub(pattern, replacement, input)

print(eval(const_sub.replace("x", "Polynomial([0,1])")))
