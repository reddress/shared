def isvalidIP(s):
    nums = s.split(".")
    for n in nums:
        if not n.isdigit():
            return False
        if len(n) > 1:
            if n[0] == "0":
                return False
    return len(nums) == 4 and len(list(filter(lambda n: int(n) in range(0,256),
                                              nums))) == 4

def extractIPs(s):
    words = s.split(" ")
    out = []
    for word in words:
        if isvalidIP(word):
            out.append(word)
    return out

def extractIPs_filter(s):
    words = s.split(" ")
    return list(filter(isvalidIP, words))
    
def checkio(text):
    return extractIPs(text)

extractIPs("10.0.0.1 and 1.1.1.001 00126.0.0.256")
extractIPs_filter("10.0.0.1 and 1.1.1.001 00126.0.0.256")

extractIPs("")
