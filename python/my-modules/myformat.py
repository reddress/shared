def printrow(*elems, w=8):
    elem_format = "{:>" + str(w) + "}"
    format_str = elem_format * len(elems)
    print(format_str.format(*elems))
