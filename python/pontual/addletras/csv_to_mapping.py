mapping = {}

with open('A_PROD_LIST.txt') as fin:
    for line in fin:
        codigo = line.strip()
        numbers = codigo[:6]
        if numbers not in mapping:
            mapping[numbers] = []
        mapping[numbers].append(codigo[6:])
