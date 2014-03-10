def myreduce(fn, base, lst):
    result = base
    for elt in lst:
        result = fn(result, elt)
    return result

# myreduce(lambda x, y: x * y, 1, [1,2,3,4,5][:3])
