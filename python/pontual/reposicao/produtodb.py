import os
os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/")

import shelve

from produto import Produto
from datetime import datetime

SHELF_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/produtodb"

pdb = shelve.open(SHELF_FILE)

def create():
    codigo = input("Codigo? ")
    caixa = int(input("Quantidade por caixa grande? "))
    info = input("Nome? ")
    vendas = int(input("Vendas 2013? "))
    pdb[codigo] = Produto(codigo, caixa, info, vendas)

def close():
    pdb.close()

def listpdb():
    print(list(pdb.keys()))
