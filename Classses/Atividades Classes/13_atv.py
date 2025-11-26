import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: int
    endereco: str

    def dados_funcionarios(self):

        print("=!= FUNCIONÁRIO =!=")
        print(f"Nome: {self.nome} \nData de admissão: {self.data_admissao} \nMatrícula: {self.matricula} \nEndereço: {self.endereco}\n")

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str

    def dados_cliente(self):

        print("=!= CLIENTE =!=")
        print(f"Nome: {self.nome} \nData de nascimento: {self.nascimento} \nEndereço: {self.endereco}\n")

lista_funcionarios = []
lista_clientes = []

qtd_funcionarios = int(input("Quantidade de funcionário(s): "))

for i in range(qtd_funcionarios):

    print("+++ INFORMAÇÕES DO FUNCIONÁRIO +++")
    funcionario = Funcionario(
        nome= input("Digite seu nome: "),
        data_admissao= input("Digite sua data de admissão: "),
        matricula= int(input("Digite seu número de matrícula: ")),
        endereco= input("Digite seu endereço: ")
    )
    lista_funcionarios.append(funcionario)

qtd_clientes = int(input("Quantidade de cliente(s): "))

for i in range(qtd_clientes):

    print("+++ INFORMAÇÕES DO FUNCIONÁRIO +++")
    cliente = Cliente(
        nome= input("Digite seu nome: "),
        nascimento= input("Digite sua data de nascimento: "),
        endereco= input("Digite seu endereço: ")
    )
    lista_clientes.append(cliente)

nome_arquivo = "funcionarios.csv"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_funcionarios:
    for funcionario in lista_funcionarios:
        arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
        print("Dados salvos com sucesso.")

nome_do_arquivo = "clientes.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_clientes:
    for cliente in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.nascimento}, {cliente.endereco}\n")
        print("Dados salvos com sucesso.")

print("_-_-_ EXIBINDO TODOS OS FUNCIONÁRIOS _-_-_")
lista_f = []

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_f:
        lista_todos_funcionarios = arquivo_f.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, data_admissao, matricula, endereco = funcionario.strip().split(",")
            dados_usuario_f = Funcionario(nome=nome, 
                                          data_admissao=data_admissao, 
                                          matricula=matricula, 
                                          endereco=endereco)
            lista_f.append(dados_usuario_f)
    for funcionario in lista_f:
        funcionario.dados_funcionarios()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

print("_-_-_ EXIBINDO TODOS OS CLIENTES _-_-_")
lista_c = []

try:
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo_c:
        lista_todos_clientes = arquivo_c.readlines()
        for cliente in lista_todos_clientes:
            nome, nascimento, endereco = cliente.strip().split(",")
            dados_usuario_c = Cliente(nome=nome, 
                                      nascimento=nascimento, 
                                      endereco=endereco)
            lista_c.append(dados_usuario_c)
    for cliente in lista_c:
        cliente.dados_cliente()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")