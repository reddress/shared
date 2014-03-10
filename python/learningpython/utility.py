def group(source, n):
    if n == 0:
        return "error: zero length"
    def rec(s, acc):
        rest = s[n:]
        if len(rest) > 0:
            return rec(rest, [s[:n]] + acc)
        else:
            return list(reversed([s] + acc))
    if len(source) > 0:
        return rec(source, [])
    else:
        return []

group([1,[2,22,[222]],3,4,5,6,7,[8,88]], 3)

def splitstr(s, n):
    out = []
    while len(s) > 0:
        # print(s[:n])
        # out += [s[:n]]
        out += [s[len(s)-n:]]
        s = s[:-n]
    return reversed(out)

k = splitstr("1234567", 2)
"_".join(k)
k

def buggy(s, n):
    out = []
    while len(s) > 0:
        out += s[:n]  # applies extend
        s = s[n:]
    return out

buggy("12345",2)
