import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")), 
                 altura=float(input("Digite sua altura: ")))

print("\n=== DADOS DA PESSOA ===")
print(f"\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos.\nPeso: {pessoa1.peso} KG.\nAltura: {pessoa1.altura} m.")