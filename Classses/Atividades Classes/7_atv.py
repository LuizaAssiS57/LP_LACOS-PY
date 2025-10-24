import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print("++++ DADOS DA PESSOA ++++")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")

lista_pessoas = []

for i in range(4):
    print(f"++++++ SOLICITANDO INFORMAÇÕES DA {i+1}ª PESSOA ++++++")
    pessoa = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")), 
                 altura=float(input("Digite sua altura: ")))
    lista_pessoas.append(pessoa)

os.system('cls')
print(" =+ DADOS DA PESSOA += ")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()