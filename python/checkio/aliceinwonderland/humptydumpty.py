import math

def checkio(height, width):
    c = height/2
    a = width/2
    volume = (4 * math.pi / 3) * a * a * c

    k = 2 * math.pi * a * a
    if abs(c-a) < 0.00001:  # sphere
        surfarea = 4 * math.pi * a * a
    elif c < a:  # oblate
        e = math.sqrt(1 - ((c * c) / (a * a)))
        surfarea = k * (1 + ((1 - e * e) / e) * math.atanh(e))
    else:  # prolate
        e = math.sqrt(1 - ((a * a) / (c * c)))
        surfarea = k * (1 + (c / (a * e)) * math.asin(e))

    return [round(volume, 2), round(surfarea, 2)]

checkio(4, 2)
checkio(2, 4)
checkio(2, 2)
