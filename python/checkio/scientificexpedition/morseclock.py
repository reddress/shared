def num2bin(n, width):
    return "{0:b}".format(n).zfill(width).replace("0", ".").replace("1", "-")

def normalize(timestr):
    return ":".join(["{0:0>2d}".format(int(num)) for num in timestr.split(":")])
    
def checkio(time):
    widths = list("24034034")
    result = []

    print("norm", normalize(time))
    for c in normalize(time):
        w = int(widths.pop(0))
        if w == 0:
            result.append(":")
        else:
            result.append(num2bin(int(c),w))
    return " ".join(result)

print(checkio("23:59:59"))
num2bin(9, 3)
