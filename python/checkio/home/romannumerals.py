def getroman(num):
    r_thousands = ["M", "MM", "MMM"]
    r_hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    r_tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    r_ones = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    out = ""

    if num >= 1000:
        n_thousands = num // 1000
        num -= n_thousands * 1000
        out += r_thousands[n_thousands-1]

    if num >= 100:
        n_hundreds = num // 100
        num -= n_hundreds * 100
        out += r_hundreds[n_hundreds-1]
        
    if num >= 10:
        n_tens = num // 10
        num -= n_tens * 10
        out += r_tens[n_tens-1]

    if num > 0:
        n_ones = num
        out += r_ones[n_ones-1]
        
    return out

def checkio(data):
    return getroman(data)

checkio(499)
