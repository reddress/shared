from datetime import datetime
import pickle
import unicodedata

# API
# Estados: (r)eserva, (d)esistencia, (p)edido, (x)cancelado, (c)ontainer,
#          (f)aturado, (a)mostra
#
# Cliente(codigo, nome, vendedor)
#
# Produto(codigo, descricao, quantidade_pac=0, containers="")
#
# Linha(quantidade, codigo_produto)
#
# Venda(numero_pp, data_inicial, data_atualizado, codigo_cliente, estado,
#       observacoes)
#  .nova_linha(linha_str) "100 143038"
#  .apagar_linhas()
#  .cobrar(pp)
#  .remover_cobrar(pp)
#
# SHORTCUTS
#
# Mostrar todos os pedidos com
# cod(codigo do produto)
# cli(nome do cliente)


PICKLE_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/aspetta/data.pickle"

# clientes = {}
# produtos = {}
# vendas = {}

date_fmt = "%a %d/%m/%y %H:%M"
short_date = "%a %d/%m"

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != 'Mn')

estados = {"r": "Reserva", "d": "Desistencia", "p": "Pedido", "x": "Cancelado",
           "c": "Container", "f": "Faturado", "a": "Amostra"}

class Cliente:
    def __init__(self, codigo, nome, vendedor):
        codigo = str(codigo)
        self.codigo = codigo
        self.nome = nome
        self.vendedor = vendedor
        clientes[codigo] = self

    def __repr__(self):
        return "{} ({}) {}".format(self.nome, self.vendedor, self.codigo)

class Produto:
    def __init__(self, codigo, descricao,
                 quantidade_pac=0, containers=""):
        codigo = str(codigo).upper()
        descricao = strip_accents(descricao).lower()
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade_pac = int(quantidade_pac)
        self.containers = containers
        produtos[codigo] = self

    def __repr__(self):
        return "{} {} ({} {})".format(self.codigo, self.descricao,
                                      self.quantidade_pac, self.containers)

class Linha:
    def __init__(self, quantidade, codigo_produto):
        self.quantidade = int(quantidade)
        self.codigo_produto = codigo_produto

    def __repr__(self):
        return "{} pcs {}".format(self.quantidade,
                                  produtos[self.codigo_produto])
        
class Venda:
    def __init__(self,
                 numero_pp=-1,
                 data_inicial=datetime.now(),
                 data_atualizado=datetime.now(),
                 codigo_cliente=505,
                 estado=estados['r'],
                 observacoes="",
                 ativo=True):
        if numero_pp == 0:
            numero_pp = min(vendas.keys()) - 1
        self.numero_pp = numero_pp
        self.data_inicial = data_inicial
        self.data_atualizado = data_atualizado
        self.codigo_cliente = str(codigo_cliente)
        self.estado = estado
        self.observacoes = observacoes
        self.ativo = ativo
        self.linhas = []
        self.pedidos_para_cobrar = set()
        vendas[numero_pp] = self

    def nova_linha(self, linha_str):
        linha_parts = linha_str.split()
        self.linhas.append(Linha(int(linha_parts[0]), linha_parts[1].upper()))
        self.data_atualizado = datetime.now()

    def apagar_linhas(self):
        self.linhas = []
        self.data_atualizado = datetime.now()

    def cobrar(self, pp):
        self.pedidos_para_cobrar.add(pp)
        self.data_atualizado = datetime.now()

    def remover_cobrar(self, pp):
        self.pedidos_para_cobrar.discard(pp)
        self.data_atualizado = datetime.now()

    def __repr__(self):
        fmt = "\n\n{pp} {ativo}\n{data_ini}\n{data_atual}\n{estado} {cliente}\nObs.: {obs}\n{linhas}\n {cobrar}"
        ativo_flag = "Ativo" if self.ativo else "Inativo"
        return fmt.format(pp=self.numero_pp,
                          ativo=ativo_flag,
                          data_ini=self.data_inicial.strftime(date_fmt),
                          data_atual=self.data_atualizado.strftime(date_fmt),
                          estado=self.estado,
                          cliente=clientes[self.codigo_cliente],
                          obs=self.observacoes,
                          linhas="\n".join(map(str, self.linhas)),
                          cobrar=self.pedidos_para_cobrar)
        
    def recursive_summary(self, prefix=""):
        fmt = "\n{pre}({pp}) {estado}; {cliente}; [{data}] {data_atual}\n{pre}{linhas}\n{pre}Obs: {obs}\n{children}"
        newline_prefix = "\n" + prefix
        # if self.ativo:
        return fmt.format(pre=prefix,
                          pp=self.numero_pp,
                          estado=self.estado,
                          cliente=clientes[self.codigo_cliente],
                          data=self.data_inicial.strftime(short_date),
                          data_atual=self.data_atualizado.strftime(short_date),
                          linhas=newline_prefix.join(map(str, self.linhas)),
                          obs=self.observacoes,
                          children="".join([vendas[cod].recursive_summary(prefix+"\t") for cod in self.pedidos_para_cobrar]))
        #else:
        #    return ""

def load():
    global clientes, produtos, vendas
    with open(PICKLE_FILE, 'rb') as p:
        clientes, produtos, vendas = pickle.load(p)

def reset():
    global clientes, produtos, vendas
    clientes = {}
    produtos = {}
    vendas = {}
    Produto(143038, "Caneca de inox 180 ml")
    Produto(143035, "Kit Churrasco")
    Cliente(505, "Pontual", "Pontual")
    Venda()
    Venda(1)
    Venda(2)
    vendas[1].cobrar(-1)
    vendas[2].cobrar(1)
    Venda(3)
    vendas[-1].nova_linha("100 143038")
    vendas[-1].nova_linha("12 143035")
    vendas[1].nova_linha("30 143038")

def save():
    global clientes, produtos, vendas
    with open(PICKLE_FILE, 'wb') as p:
        pickle.dump([clientes, produtos, vendas], p)

def novo_cliente(codigo=""):
    if codigo == "":
        codigo = input("Codigo do cliente: ")
    nome = input("({}) Nome do cliente: ".format(codigo))
    vendedor = input("Vendedor(a): ")
    Cliente(codigo, nome, vendedor)

def novo_produto(codigo=""):
    if codigo == "":
        codigo = input("Codigo do produto: ")
    codigo = codigo.upper()
    descricao = input("({}) Descricao: ".format(codigo))
    quantidade_pac = input("Quantidade PAC: ")
    if len(quantidade_pac) == 0:
        quantidade_pac = 0
    containers = input("Container(s): ")
    Produto(codigo, descricao, int(quantidade_pac), containers)

def nova_venda():
    numero_pp = input("Numero do pre-pedido: ")
    if len(numero_pp) == 0:
        numero_pp = min(vendas.keys()) - 1

    data_str = input("({}) Data do pre-pedido (dd/mm/aaaa): ".format(numero_pp))
    if len(data_str) == 0:
        data_inicial = datetime.now()
    else:
        data_parts = data_str.split("/")
        data_inicial = datetime(int(data_parts[2]),
                                int(data_parts[1]),
                                int(data_parts[0]))
        
    codigo_cliente = input("({}) Codigo do cliente: ".format(numero_pp))
    if codigo_cliente not in clientes:
        novo_cliente(codigo_cliente)
        
    estado = input("(r)esv, (d)esist, (p)edido, (x)cancelado, (c)ontainer, (f)aturado, (a)mostra? ").lower()
    if len(estado) == 0:
        estado = "r"
    obs = input("Observacoes: ")
    Venda(numero_pp=int(numero_pp), codigo_cliente=codigo_cliente, estado=estados[estado], observacoes=obs, data_inicial=data_inicial)

    numero_pp = int(numero_pp)
    if numero_pp < 0:
        numero_pp = min(vendas.keys())

    line = input("Quantidade e codigo (linha) ")
    while line != "":
        line_parts = line.split()
        if line_parts[1].upper() not in produtos:
            novo_produto(line_parts[1])
        vendas[numero_pp].nova_linha(line.upper())
        line = input("Quantidade e codigo (linha+) ")

def load_nomes():
    with open("produto_nomes.txt",encoding="utf-8") as f:
        for line in f:
            line_parts = line.split(";")
            Produto(line_parts[0], strip_accents(line_parts[1]).strip())

def novo_pac():
    codigo = input("Codigo: ")
    pac_parts = input("Qtde. e containers: ").split()
    produtos[codigo].quantidade_pac = int(pac_parts[0])
    produtos[codigo].containers = " ".join(pac_parts[1:])

def novo_estado():
    # pp = numero do pre-pedido
    pp = int(input("Pre-pedido: "))
    if pp not in vendas:
        print("Pre-pedido inexistente.")
        return
    estado = input("(r)esv, (d)esist, (p)edido, (x)cancelado, (c)ontainer, (f)aturado, (a)mostra? ").lower()
    if len(estado) == 0:
        estado = "r"
    vendas[pp].estado = estados[estado]
    
def cobrar(cobrador, pp_reserva):
    vendas[cobrador].cobrar(pp_reserva)

def nao_cobrar(cobrador, pp_reserva):
    vendas[cobrador].remover_cobrar(pp_reserva)

def show(pp, all=False):
    if all:
        print(vendas[pp].recursive_summary())
    else:
        if vendas[pp].ativo:
            print(vendas[pp].recursive_summary())

def codigo_in_linhas(codigo, linhas):
    codigo = str(codigo).upper()
    for linha in linhas:
        if codigo == linha.codigo_produto:
            return True
    return False

def show_pps(pps, all=False):
    # pp = numero do pre-pedido
    for pp in sorted(pps, key=lambda pp: vendas[pp].data_inicial):
        show(pp)
        
def cod(c, all=False):
    pps = [pp for pp in vendas if codigo_in_linhas(c, vendas[pp].linhas)]
    show_pps(pps, all)

def cli(c, all=False):
    pps = [pp for pp in vendas if c.lower() in clientes[vendas[pp].codigo_cliente].nome.lower()]
    show_pps(pps, all)

def on(pp):
    vendas[int(pp)].ativo = True

def off(pp):
    vendas[int(pp)].ativo = False

def all(all_flag=False):
    pps = [pp for pp in vendas if vendas[pp].ativo]
    show_pps(pps, all_flag)

def des(all=False):
    pps = [pp for pp in vendas if vendas[pp].estado == estados["d"]]
    show_pps(pps, all)

def cont(all=False):
    pps = [pp for pp in vendas if vendas[pp].estado == estados["c"]]
    show_pps(pps, all)

def cont_num(cn, all=False):
    # procurar pedidos aguardando container especifico, cn = container number
    # display vendas where str(cn) in produto.containers
    pps = []
    cn = str(cn)
    for pp in vendas:
        for linha in vendas[pp].linhas:
            if cn in produtos[linha.codigo_produto].containers:
                pps.append(pp)
    show_pps(pps, all)

def rest(codigo_produto):
    # count quantidade_pac and subtract amounts from all active pedidos
    # matching codigo_produto
    codigo_produto = str(codigo_produto)
    total = int(produtos[codigo_produto].quantidade_pac)

    reservando = 0
    for pp in vendas:
        if vendas[pp].ativo:
            for linha in vendas[pp].linhas:
                if linha.codigo_produto == codigo_produto:
                    reservando += int(linha.quantidade)
    print("Sobram: " + str(total - reservando) + " pcs")
    
def ref(pp_original, pp_novo):
    # make a new reference to a venda, after pre-pedido number is assigned
    # by faturamento
    vendas[int(pp_novo)] = vendas[int(pp_original)]
    
def print_help():
    print("""
    q: quit
    all: display all active vendas
    d: desistencia
    c: container

    pp [numero pre-pedido]: display venda unconditionally
    rest [codigo_produto]
    cn [numero_container]
    on [pp]
    off [pp]
    cod [codigo_produto]
    """)

def loop():
    print("Enter 'h' for help")

    show_all = False
    
    while True:
        show_status = " show all" if show_all else " only ativo"
        user_input = input("Aspetta{}) ".format(show_status))
        if user_input.strip() == "":
            continue

        user_input_tokens = user_input.split()
        command = user_input_tokens[0]
            
        if len(user_input_tokens) == 1:
            if command == 'q':
                print("Saving...")
                save()
                print("Bye!")
                break
            elif command == 'h':
                print_help()
            elif command == 'all':
                all(show_all)
            elif command == 'd':
                des(show_all)
            elif command == 'c':
                cont(show_all)
            elif command == 'show':
                show_all = not show_all
        else:
            arguments = user_input_tokens[1:]
            
            if command == "rest":
                rest(arguments[0])
            elif command == "cn":
                cont_num(arguments[0], show_all)
            elif command == "on":
                on(arguments[0])
            elif command == "off":
                off(arguments[0])
            elif command == "cod":
                cod(arguments[0], show_all)
            elif command == "pp":
                print(vendas[int(arguments[0])])
            elif command == "ref":
                ref(arguments[0], arguments[1])
            elif command == "cli":
                cli(" ".join(arguments), show_all)
                
# do not remove this line
load()
print("Run loop() for shortcut CLI")
