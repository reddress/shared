import csv
import re

PONTUAL = "d:/pontual/clientes/cli_pontual_csv.csv"
UNIAO = "d:/pontual/clientes/cli_uniao_csv.csv"
SHORT = "d:/pontual/clientes/cli_short.csv"

def normalize(s):
    # remove all whitespace and replace comma with dot
    s = s.replace(",", ".")
    whitespace_pat = re.compile(r'\s')
    s = whitespace_pat.sub('', s)
    return s

def parsecsv(filename):
    clientes = {}
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        found_id = 0
        for row in reader:
            if found_id:
                clientes[found_id] = normalize(row[0].strip())
                found_id = 0
            else:
                try:
                    found_id = int(row[0])
                except ValueError:
                    # print("Not an ID:", row[0])
                    pass 
    return clientes 

def parseall():
    ptl = parsecsv(PONTUAL)
    uni = parsecsv(UNIAO)

    for id in sorted(ptl):
        # print(id) 
        if ptl[id] != uni[id]:
            print(id)
            print("PTL:", ptl[id])
            print("UNI:", uni[id])
            print()
    print(len(ptl))
    print(len(uni))

    return {'p': ptl, 'u': uni}

def test():
    testeql(normalize("a, b, c"), "a.b.c")
    testeql(normalize("a	b,,   c."), "ab..c.")
            
if __name__ == "__main__":
    parseall()

