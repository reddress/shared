def bitand(u, v):
    return u & v
def bitor(u, v):
    return u | v
def bitxor(u, v):
    return u ^ v

def num_to_bits(num):
    return "{0:b}".format(num)

def compute_grid(m, n, op):
    """
    place n's bits in first row, and m's bits in first column.
    apply op operation to fill in rest of grid, then add the result
    """
    mbits = num_to_bits(m)
    nbits = num_to_bits(n)

    grid = [['' for col in range(len(nbits)+1)] for row in range(len(mbits)+1)]

    grid[0][1:] = list(nbits)             # first row
    for row in range(1, 1 + len(mbits)):  # first column
        grid[row][0] = mbits[row-1]

    for row in range(1,len(grid)):        # apply bit operator to rest of grid
        for col in range(1,len(grid[0])):
            grid[row][col] = op(int(grid[0][col]), int(grid[row][0]))

    # sum rows of results, ignoring first row and column
    # join bits into a string, then convert to base 10 and add them
    return sum([int("".join(map(str,row[1:])), 2) for row in grid[1:]])

def checkio(first, second):
    return sum([compute_grid(first, second, op)
                for op in [bitand, bitor, bitxor]])
    

#####
# does not seem to be good solution

class StephanInt:
    """
    An integer supporting modified bitwise operations used to build the
    partial results held in the bit matrices.
    """
    def __init__(self, value):
        self.value = value

    def __and__(self, bit):
        """
        self.value is the top row in each bit matrix
        bit is the left-most value used to compute the "and" result
        in subsequent rows.

        bit should be 1 or 0, but no checking is done for other values
        """
        if bit == 1:
            return self.value
        else:
            return 0
    def __or__(self, bit):
        """
        Similar to __and__
        """
        if bit == 1:
            # all bits in self.value become 1
            return 2 ** (len("{0:b}".format(self.value))) - 1
        else:
            return self.value
    def __xor__(self, bit):
        """
        Invert bit values if bit is 1
        """
        if bit == 0:
            return self.value
        else:
            return 2 ** (len("{0:b}".format(self.value))) - 1
            

s = StephanInt(6)
s & 1
s | 1

t = StephanInt(2)
t & 1
