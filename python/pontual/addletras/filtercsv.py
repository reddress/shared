with open('all_letras.txt', 'w') as fout:
    with open('all_csv.csv') as fin:
        for line in fin:
            if len(line) > 7:
                print(line, end='', file=fout)
