def checkio(data):
    if (list(filter(str.isupper, data)) and list(filter(str.islower, data)) and
        list(filter(str.isdigit, data)) and len(data) >= 10):
        return True
    else:
        return False
checkio("assassaaasasas")
