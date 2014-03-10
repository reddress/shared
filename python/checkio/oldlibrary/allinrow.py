def flatten(lst):
    out = []
    for elt in lst:
        if isinstance(elt, list):
            out.extend(flatten(elt))
        else:
            out.append(elt)
    return out
    

flatten([1,[[2]],[[[3, 4]]],[5,6,[7],8]])
