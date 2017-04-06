def testequal(expression, expected):
    print("\ntesting", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("... PASS\n")
    else:
        print("*** FAIL\n")

# alias
testeql = testequal
