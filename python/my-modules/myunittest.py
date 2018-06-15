import unittest

description = """
# Suppose there is a function square(x)

def square(x):
    return x * x

# We alternate good and bad tests
test(
    sq(9), 81,
    sq(3), 33,
    sq(7), 49,
    sq(1), 1,
    sq(0), 10,
)

"""

def test(*pair_args):
    trial = pair_args[::2]
    expected = pair_args[1::2]
    tc = unittest.TestCase('__init__')
    tc.assertEqual(trial, expected)
    print("* All tests passed (^o^) *")
