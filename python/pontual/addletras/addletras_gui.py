import tkinter as tk
from tkinter.filedialog import askopenfilename
import odswriter as ods

mapping = {}

with open('A_PROD_LIST.txt') as fin:
    for line in fin:
        codigo = line.strip()
        numbers = codigo[:6]
        if numbers not in mapping:
            mapping[numbers] = []
        mapping[numbers].append(codigo[6:])

def addletras(number):
    if str(number) not in mapping:
        return str(number)
    else:
        return '\n'.join([str(number) + letter for letter in mapping[str(number)]])

orig_path_filename = askopenfilename()
print(orig_path_filename)

orig_filename = orig_path_filename.split("/")[-1].split('.')[0]
print(orig_filename)

dest_path = "/".join(orig_path_filename.split("/")[:-1]) + "/"
print(dest_path)

# dest_path_filename = dest_path + orig_filename + "_letras.csv"
dest_path_filename = dest_path + orig_filename + "_letras.ods"
print(dest_path_filename)

with ods.writer(open(dest_path_filename, 'wb')) as fout:
# with open(dest_path_filename, 'w') as fout:
    with open(orig_path_filename) as fin:
        for line in fin:
            codigo = line.strip()
            if len(codigo) > 6:
                print('Warning: bypassing ' + codigo)
                # print(codigo, file=fout)
                fout.writerow([codigo.strip()])
            else:
                # print(addletras(codigo), file=fout)
                for cod_with_letra in addletras(codigo).split():
                    fout.writerow([cod_with_letra.strip()])
