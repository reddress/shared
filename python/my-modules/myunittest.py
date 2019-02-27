import unittest

description = """
# Suppose there is a function sq(x) that squares numbers

def sq(x):
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

# previously it was called just 'test'
def pairtest(*pair_args):
    """https://stackoverflow.com/questions/18084476/is-there-a-way-to-use-python-unit-test-assertions-outside-of-a-testcase"""
    
    tc = unittest.TestCase('__init__')

    trial = pair_args[::2]
    expected = pair_args[1::2]
    for t, e in zip(trial, expected):
        if isinstance(t, float):
            tc.assertAlmostEqual(t, e)
        else:
            tc.assertEqual(t, e)
            
    print("\n\n* All tests passed \\(^o^)/ \n")
