def mytests(*tests):
    """
    Test whether a function call equals a given value.
    mytests((mysquare(3), 9),
    (mysquare(9), 81),
    (mysquare(-3), 9))  # last one fails
    """

    all_pass = True
    i = 1
    tests_failed = []
    for test in tests:
        if test[0] != test[1]:
            print("test #" + str(i), "FAIL", end=" ")
            tests_failed.append(i)
            all_pass = False
        else:
            print("test #" + str(i), "ok  ", end=" ")
        print("evaluated", test[0], "expected", test[1])
        i += 1
    print()
    if all_pass:
        print("All tests Passed")
    else:
        print("Test(s)", ", ".join(map(str, tests_failed)), "did not Pass")


