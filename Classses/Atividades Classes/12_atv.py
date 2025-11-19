import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome: str
    nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):

        print("=!= DADOS DO FUNCIONÁRIO =!=")
        print(f"Nome: {self.nome} \nData de Nascimento: {self.nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")

lista_funcionarios = []

qtd_funcionarios = int(input("Quantidade de usuário(s): "))

for i in range(qtd_funcionarios):

    print("+++ INFORMAÇÕES DO FUNCIONÁRIO +++")
    funcionario = Funcionario(
        nome= input("Digite seu nome: "),
        nascimento= input("Digite sua data de nascimento: "),
        rg= input("Digite seu rg: "),
        cpf= input("Digite seu CPF: ")
    )
    lista_funcionarios.append(funcionario)

nome_do_arquivo = "funcionarios.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_usuarios:
    for funcionario in lista_funcionarios:
        arquivo_usuarios.write(f"{funcionario.nome}, {funcionario.nascimento}, {funcionario.rg}, {funcionario.cpf}\n")
        print("Dados salvos com sucesso.")

print("_-_-_ EXIBINDO TODOS OS FUNCIONÁRIOS _-_-_")
lista = []

try:
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, nascimento, rg, cpf = funcionario.strip().split(",")
            dados_usuario = Funcionario(nome=nome, nascimento=nascimento, rg=rg, cpf=cpf)
            lista.append(dados_usuario)
    for funcionario in lista:
        funcionario.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
