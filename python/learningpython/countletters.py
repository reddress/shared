def countLetters(s):
    result = {}
    for letter in s:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
