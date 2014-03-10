def checkio(data):
    text = data.lower()
    freq = {}
    for c in text:
        if c.isalpha():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
    vals = {}
    for (k, v) in freq.items():
        if v in vals:
            vals[v] += k
        else:
            vals[v] = k
    s = sorted(vals, reverse=True)
    return sorted(vals[s[0]])[0]

checkio("bbbooocadddfffzzz")
