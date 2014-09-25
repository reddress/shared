Acompanhar vendas, reservas, pedidos aguardando desistencia ou container

O aplicativo salva informacoes dos produtos e dos clientes

# API
# Estados: (r)eserva, (d)esistencia, (p)edido, (x)cancelado, (c)ontainer,
#		   (f)aturado, (a)mostra
#
# Cliente(codigo, nome, vendedor)
#
# Produto(codigo, descricao, quantidade_pac=0, containers="")
#
# Linha(quantidade, codigo_produto)
#
# Venda(numero_pp, data_inicial, data_atualizado, codigo_cliente, estado,
#		observacoes)
#  .nova_linha(linha_str) "100 143038"
#  .apagar_linhas()
#  .cobrar(pp)
#  .remover_cobrar(pp)
#
# ATALHOS
#
# Mostrar todos os pedidos com:
# cod(codigo do produto)
# cli(nome do cliente)
#
