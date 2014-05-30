# compare J's application from right to left to chaining Python methods

class NumWrapper:
    def __init__(self, number):
        self.num = number
    def add(self, n2):
        return NumWrapper(self.num + n2.num)
    def mul(self, n2):
        return NumWrapper(self.num * n2.num)

n1 = NumWrapper(3)
n2 = NumWrapper(4)
n3 = NumWrapper(5)

# in J, 3 * 4 + 5 = 3 * (4 + 5) = 3 * 9 = 27
# compute first from the right
n4 = n1.mul(n2.add(n3))
print(n4.num)

print(3 * 4 + 5)  # left-to-right produces 17
print(n1.mul(n2).add(n3).num)
