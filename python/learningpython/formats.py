"""
p. 752
"""

def commas(n):
    digits = str(n)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(n, numwidth=0, currency="\u00a5"):
    sign = '-' if n < 0 else ''
    n = abs(n)
    whole = commas(int(n))
    fract = ('%.2f' % n)[-2:]
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

if __name__ == '__main__':
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')

        tests = 0, 1, -1, 1.23, 1., 1.2, 3.1251234
        tests += 12.34, 12.344, 12.345
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2
        tests += -1.2345, -1.2
        tests += -(2 ** 32),
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))
    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

        
