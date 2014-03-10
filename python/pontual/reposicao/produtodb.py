import os
os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/")

import shelve

from produto import Produto

SHELF_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/produtodb"

pdb = shelve.open(SHELF_FILE)

def create():
    codigo = input("Codigo? ")
    nome = input("Nome? ")
    caixa = int(input("Quantidade por caixa grande? "))
    pdb[codigo] = Produto(codigo, nome, caixa)

def close():
    pdb.close()
