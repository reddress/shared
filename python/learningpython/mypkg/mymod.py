# p. 778 exercise

def countLines(name):
    lines = open(name).readlines()
    return len(lines)

#countLines("python/mymod.py")

def countChars(name):
    chars = 0
    for line in open(name):
        chars += len(line)
    return chars

#countChars("python/mymod.py")

def test(name):
    print(countLines(name))
    print(countChars(name))

if __name__ == '__main__':
    test("mymod.py")
