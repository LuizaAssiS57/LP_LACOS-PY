import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Endereco:
    logarudouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

pessoa = Pessoa(nome=input("Digite seu nome: "), 
                idade=int(input("Digite sua idade: ")),
                endereco= Endereco(logarudouro= input("Digite seu endereço: "),
                                   numero= int(input("Informe o número: "))))

os.system('cls')
print("=== DADOS DO CLIENTE ===")
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Endereço: {pessoa.endereco.logarudouro}, {pessoa.endereco.numero}")