# export for use in Java GUI

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

def format_data(key):
    try:
        produto = pdb[key]

        try:
            lastmod_value = produto.lastmod.strftime("%d/%m/%y")
            return """{date};{antigo};{caixa}
            {info}""".format(date=lastmod_value,
                             antigo=produto.vendas,
                             caixa=produto.caixa,
                             info=produto.info)
        except:
            return """{date};{antigo};{caixa}
            {info}""".format(date="01/06/2014",
                             antigo=produto.vendas,
                             caixa=produto.caixa,
                             info=produto.info)
    except:
        print("cannot read " + key)


for key in pdb:
    if len(key) > 5:
        print(key)
        print(format_data(key))
        #if os.path.isfile(DATA_DIR + key + ".txt"):
        #   print("skipping " + key)
        #else:
        #    print("add " + key)
        #        try:
        #            print("|"+key+"|")
        #            write_to_data_file(key)
        #       except:
        #            pass


#def write_to_data_file(key):
#    # with open(DATA_DIR + key + ".txt", 'w', encoding="UTF-8") as out:
#    f = codecs.open(DATA_DIR + key + ".txt", 'w', encoding="utf8")
#    f.write(format_data(key))
#    f.close()    
        
pdb.close()
