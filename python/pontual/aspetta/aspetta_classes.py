from datetime import datetime

class Estado:
    reserva = "reserva"
    desistencia = "desistencia"
    pedido = "pedido"
    cancelado = "cancelado"
    container = "container"

class Cliente:
    def __init__(self, codigo, nome, vendedor):
        self.codigo = codigo
        self.nome = nome
        self.vendedor = vendedor
        clientes[codigo] = self

    def __repr__(self):
        return "{} {} ({})".format(self.codigo, self.nome, self.vendedor)

class Produto:
    def __init__(self, codigo, descricao,
                 quantidade_pac, containers):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade_pac = quantidade_pac
        self.containers = containers
        produtos[codigo] = self

    def __repr__(self):
        return "{} {} ({} {})".format(self.codigo, self.descricao,
                                      self.quantidade_pac, self.containers)

class Linha:
    def __init__(self, quantidade, codigo_produto):
        self.quantidade = quantidade
        self.codigo_produto = codigo_produto

    def __repr__(self):
        return "{} pçs {}".format(self.quantidade, self.codigo_produto)
        
class Venda:
    def __init__(self,
                 numero_pp=-1,
                 data_inicial=datetime.now(),
                 data_atualizado=datetime.now(),
                 codigo_cliente=505,
                 estado=Estado.reserva,
                 observacoes=""):
        if numero_pp < 0:
            numero_pp = min(vendas.keys()) - 1
        self.numero_pp = numero_pp
        self.data_inicial = data_inicial
        self.data_atualizado = data_atualizado
        self.codigo_cliente = codigo_cliente
        self.estado = estado
        self.observacoes = observacoes
        self.linhas = []
        vendas[numero_pp] = self

    def add_linha(self, linha_str):
        linha_parts = linha_str.split()
        self.linhas.append(Linha(int(linha_parts[0]), linha_parts[1]))

    def __repr__(self):
        format_str = "{0} {1} {2} {3} {4} {5} {6}"
        return format_str.format(self.numero_pp,
                                 self.data_inicial,
                                 self.data_atualizado,
                                 clientes[self.codigo_cliente],
                                 self.estado,
                                 self.observacoes,
                                 "\n".join(self.linhas))
