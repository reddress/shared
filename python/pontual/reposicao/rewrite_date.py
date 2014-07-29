# set back dates matching 28/07 and in produtodb

import os
import os.path
import shelve
import codecs

from datetime import datetime

class Produto:
    def __init__(self, codigo, caixa, info, vendas=0, lastmod=datetime.now()):
        self.codigo = codigo
        # self.nome = nome.upper()
        # self.ultimocont = ultimocont
        self.caixa = caixa
        self.info = info
        self.vendas = vendas
        # self.pedidos = pedidos
        self.lastmod = lastmod
    def __repr__(self):
        return "%s - %s" % (self.codigo, self.info.split()[0])

SHELF_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/produtodb"
pdb = shelve.open(SHELF_FILE)

DATA_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/java/AAAutomation/data/"

def rewrite(key):
    #f.write(format_data(key))
    #f.close()
    
    with open(DATA_DIR + key + ".txt", encoding="utf8") as infile:
        firstline = infile.readline().strip()
        firstline_parts = firstline.split(";")
        firstline_parts = [part if part.strip() != '' else '0' for part in firstline_parts]
        if firstline_parts[0][:5] == '28/07':
            firstline_parts[0] = '01/01/14'
        # print(key + ": " + ", ".join(firstline_parts))
        firstline_out = ";".join(firstline_parts)
        data_out = ""
        for line in infile:
            data_out += line
            # print(line.strip())
    print(key + " " + firstline_out)
    f = codecs.open(DATA_DIR + key + ".txt", 'w', encoding="utf8")
    #f = codecs.open(DATA_DIR + "tmp.txt", 'w', encoding="utf8")
    f.write(firstline_out + "\n")
    f.write(data_out)
    f.close()

#for key in pdb:
#    if len(key) > 5:
#        if os.path.isfile(DATA_DIR + key + ".txt"):
#            rewrite(key)

def read_date(key):
    with open(DATA_DIR + key + ".txt") as infile:
        firstline = infile.readline().strip()
        print(key + ": " + firstline)
        for line in infile:
            print(line.strip())
        
def write_to_data_file(key):
    # with open(DATA_DIR + key + ".txt", 'w', encoding="UTF-8") as out:
    f = codecs.open(DATA_DIR + key + ".txt", 'w', encoding="utf8")
    f.write(format_data(key))
    f.close()
        
pdb.close()
