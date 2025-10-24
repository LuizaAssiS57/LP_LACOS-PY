import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}\n")

    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}")

print("\n===== SOLICITANDO DADOS =====")

lista_pessoas = []

for i in range(3):
    pessoa = Pessoa(nome= input("\nDigite seu nome: "),
                    cpf= input("Digite seu CPF: "),
                    telefone= input("Digite seu telefone: "))
    lista_pessoas.append(pessoa)
    

os.system('cls')
print(" =+ DADOS DA PESSOA += ")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

print("\n+++ TELEFONE +++")
for pessoa in lista_pessoas:
    pessoa.dados_sms_marketing()