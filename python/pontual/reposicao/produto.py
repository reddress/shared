from datetime import datetime

class Produto:
    def __init__(self, codigo, nome, caixa, vendas={}, ultimocont="", pedidos="", lastmod=datetime.now()):
        self.codigo = codigo
        self.nome = nome.upper()
        self.caixa = caixa
        self.vendas = vendas
        self.ultimocont = ultimocont
        self.pedidos = pedidos
        self.lastmod = lastmod
    def __repr__(self):
        return "[%s] %s - %s" % (self.lastmod.strftime("%Y-%m-%d"),
                                 self.codigo, self.nome)
