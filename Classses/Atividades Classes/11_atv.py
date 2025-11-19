import os 
from dataclasses import dataclass
os.system('cls')

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str

    def exibir_dados(self):
        print("=====+ DADOS DO PACIENTE +=====")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print(f"CPF: {self.cpf}")

lista_pacientes = []

qtd = int(input("Informe a quantidade de pessoas que deseja cadastrar: "))

for i in range(qtd):

    print("+++ CADASTRO DE PACIENTE +++")
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        peso= float(input("Digite seu peso: ")),
        altura= float(input("Digite sua altura: ")),
        cpf= input("Digite seu CPF: ")
    )
    lista_pacientes.append(paciente)
    
nome_do_arquivo = "dados_do_paciente.csv"
with open(nome_do_arquivo, "a", encoding="uft-8") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura}, {paciente.cpf}\n")
        print("Dados salvos com sucesso.")

print("\nExibindo todos os pacientes: ")
lista = []
try:
    # "r" - read 
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade, peso, altura, cpf = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade), peso=float(peso), altura= float(altura), cpf=cpf)
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
