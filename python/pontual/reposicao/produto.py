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
