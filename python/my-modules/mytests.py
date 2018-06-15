import sys

def asst(value, expected, message=""):
    print("assert", value, "equals", expected, "({})".format(message))
    assert value == expected, message
    
def testequal(expression, expected):
    print("testing", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("(^o^) PASS\n")
        return 0
    else:
        print("(._.) FAIL\n")
        return 1

# alias
testeql = testequal

# http://stackoverflow.com/questions/32000934/python-print-a-variables-name-and-value

# def pr_(expression):
#     frame = sys._getframe(1)
#     print(expression, '=', repr(eval(expression, frame.f_globals, frame.f_locals)))

def pr(s):
    """prs('a b c') calls pr_endnone, pr for each of the names"""
    if type(s) != str:
        raise ValueError("Argument to pr() must be a string")
    frame = sys._getframe(1)
    names = s.split()
    for name in names:
        print(name, '=', repr(eval(name, frame.f_globals, frame.f_locals)), end=", ")
    print()
