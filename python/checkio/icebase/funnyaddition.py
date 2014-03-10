# does not use plus sign

def next_in_seq(s, seq):
    seq_list = list(seq)
    for i in range(seq.find(s)):
        seq_list.pop(0)
    return seq_list[1]

def nextdigit(s):
    return next_in_seq(s, "01234567890")

def prevdigit(s):
    return next_in_seq(s, "09876543210")
                   
def nextnum(s):
    digits = reversed(list(s))
    result = []
    carry = True
    for digit in digits:
        if carry:
            if digit == "9":
                carry = True
            else:
                carry = False
            result.append(nextdigit(digit))
        else:
            result.append(digit)
    if carry:
        result.append("1")
    return "".join(reversed(result))
        
def add(nums):
    assert nums[0] > 0 and nums[1] > 0
    result = str(nums[0])
    for i in range(nums[1]):
        result = nextnum(result)
    return int(result)

add([5,7])
