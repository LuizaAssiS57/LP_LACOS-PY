import os
import time
from dataclasses import dataclass

os.system('cls || clear')  # Limpar terminal

lista_clientes = []
lista_produtos = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: Endereco

    def mostrar_dados_cliente(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone} \nEndereço: {self.endereco.logradouro}, número {self.endereco.numero}, {self.endereco.cidade}-{self.endereco.estado}")

@dataclass
class Produto:
    nome_produto: str
    quantidade: int
    lote: int
    validade: str

    def mostrar_dados_produto(self):
        print(f"Nome: {self.nome_produto} \nQuantidade: {self.quantidade} \nLote: {self.lote} \nValidade: {self.validade}")

# Verificar se a lista está vazia
def lista_esta_vazia_cliente(lista_clientes):
    if not lista_clientes:
        print('\nNão há clientes cadastrados.')
        return True
    return False

def lista_esta_vazia_produto(lista_produtos):
    if not lista_produtos:
        print('\nNão há produtos cadastrados.')
        return True
    return False

# Adicionar cliente
def adicionar_cliente(lista_clientes):
    print('\n+=+=+=+ ADICIONAR CLIENTE +=+=+=+')
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = Endereco(logradouro= input("Endereço: "),
                                     numero= int(input("Número: ")),
                                     cidade=input("Cidade: "),
                                     estado= input("Estado: ").upper())

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    lista_clientes.append(novo_cliente)

    print(f'\nCliente {nome} adicionado com sucesso!')

# Adicionar produto
def adicionar_produto(lista_produtos):
    print("\n_-_-_ ADICIONAR PRODUTO _-_-_")
    nome_produto = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    lote = int(input("Lote: "))
    validade = input("Validade: ")

    novo_produto = Produto(nome_produto=nome_produto, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)

# Encontrar cliente por nome.
def encontrar_por_nome(lista_cliente, nome_buscar):
    nome_buscar_upper = nome_buscar.upper()
    for cliente in lista_cliente:
        if cliente.nome.upper() == nome_buscar_upper:
            return cliente
    return None

# Encontrar produto por lote.
def encontrar_por_lote(lista_produtos, lote_buscar):
    for produto in lista_produtos:
        if produto.lote == lote_buscar:
            return produto
    return None

# Mostrar todos os clientes.
def mostrar_todos_cliente(lista_clientes):
    if lista_esta_vazia_cliente(lista_clientes):
        return

    print('\n===== LISTA DE CLIENTES =====')
    for cliente in lista_clientes:
        cliente.mostrar_dados_cliente()

# Mostrar todos os produtos.
def mostrar_todos_produto(lista_produtos):
    if lista_esta_vazia_produto(lista_produtos):
        return

    print('\n===== LISTA DE PRODUTOS =====')
    for produto in lista_produtos:
        produto.mostrar_dados_produto()

# Atualizar aluno
def atualizar_cliente(lista_clientes):
    if lista_esta_vazia_cliente(lista_clientes):
        return

    mostrar_todos_cliente(lista_clientes)

    print('\n++++++ ATUALIZAR DADOS DO CLIENTE ++++++')
    nome_buscar = input("Informe o nome do cliente: ")
    cliente = encontrar_por_nome(lista_clientes, nome_buscar)

    if cliente:
        print('\nCliente encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome: {cliente.nome}')
        novo_nome = input('Nome atualizado: ')

        print(f'E-mail: {cliente.email}')
        novo_email = input('Novo E-mail: ')

        print(f'Telefone: {cliente.telefone}')
        novo_telefone = input('Novo telefone: ')

        print(f'Endereço atual: {cliente.endereco}')
        novo_endereco = input('Novo endereço: ')

        if novo_nome:
            cliente.nome = novo_nome
        if novo_email:
            cliente.email = novo_email
        if novo_telefone:
            cliente.telefone = novo_telefone
        if novo_endereco:
            cliente.endereco = novo_endereco

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nCliente {nome_buscar} não encontrado no sistema.')

# Atualizar produto.
def atualizar_produto(lista_produtos):
    if lista_esta_vazia_produto(lista_produtos):
        return

    mostrar_todos_produto(lista_produtos)

    print('\n++++++ ATUALIZAR DADOS DO PRODUTO ++++++')
    lote_buscar = int(input("Informe o lote do produto: "))
    produto = encontrar_por_lote(lista_produtos, lote_buscar)

    if produto:
        print('\nProduto encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome: {produto.nome_produto}')
        novo_nome_produto = input('Nome atualizado: ')

        print(f'Quantidade: {produto.quantidade}')
        nova_quantidade = input('Novo quantidade: ')

        print(f'Lote: {produto.lote}')
        novo_lote = input('Novo lote: ')

        print(f'Validade atual: {produto.validade}')
        nova_validade = input('Validade: ')

        if novo_nome_produto:
            produto.nome_produto = novo_nome_produto
        if nova_quantidade:
            produto.quantidade = nova_quantidade
        if novo_lote:
            produto.lote = novo_lote
        if nova_validade:
            produto.validade = nova_validade

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\n({lote_buscar}) não encontrado no sistema.')

# Excluir cliente.
def excluir_cliente(lista_clientes):
    if lista_esta_vazia_cliente(lista_clientes):
        return

    mostrar_todos_cliente(lista_clientes)

    nome_buscar = input('\nDigite o nome do cliente que deseja excluir: ')
    cliente = encontrar_por_nome(lista_clientes, nome_buscar)

    if cliente:
        lista_clientes.remove(cliente)
        print(f'\nCliente {cliente.nome} excluído com sucesso!')
    else:
        print('\nCliente não encontrado.')

# Excluir produto.
def excluir_produto(lista_produtos):
    if lista_esta_vazia_produto(lista_produtos):
        return

    mostrar_todos_produto(lista_produtos)

    lote_buscar = input('\nDigite o lote do produto que deseja excluir: ')
    produto = encontrar_por_lote(lista_produtos, lote_buscar)

    if produto:
        lista_produtos.remove(produto)
        print(f'\nProduto {produto.lote} excluído com sucesso!')
    else:
        print('\nProduto não encontrado.')

# MENU PRINCIPAL
while True:
    print("""
===== MAMÃO COM AÇÚCAR =====
1  |  ADICIONAR CLIENTE
2  |  MOSTRAR TODOS OS CLIENTES
3  |  ATUALIZAR CLIENTE
4  |  EXCLUIR CLIENTE
5  |  ADICIONAR PRODUTO
6  |  MOSTRAR TODOS OS PRODUTOS
7  |  ATUALIZAR INFORMAÇÕES DE UM PRODUTO
8  |  EXCLUIR PRODUTO
0  |  SAIR DO PROGRAMA
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_cliente(lista_clientes)
        case 3:
            atualizar_cliente(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 5:
            adicionar_produto(lista_produtos)
        case 6:
            mostrar_todos_produto(lista_produtos)
        case 7:
            atualizar_produto(lista_produtos)
        case 8:
            excluir_produto(lista_produtos)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 1 and opcao != 0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")