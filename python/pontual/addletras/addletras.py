mapping = {}

mapping['137350'] = ['A','B','K','L','P','R']
mapping['140117'] = ['', 'R', 'S', 'V']
mapping['141733'] = ['A']
mapping['141713'] = ['']

def addletras(number):
    if str(number) not in mapping:
        return str(number)
    else:
        return '\n'.join([str(number) + letter for letter in mapping[str(number)]])

print(addletras('140117'))
