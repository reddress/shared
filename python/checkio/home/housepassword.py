import re

def checkio(data):
    return bool(re.search("[A-Z]", data) and re.search("[0-9]", data) and
                re.search("[a-z]", data) and len(data) >= 10)

checkio("A93a4asdfff")
checkio("asssasasasassa")
checkio("A234")
