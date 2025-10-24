import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco

cliente1 = Cliente(nome= "Luiza", 
                   endereco= Endereco(
                       logradouro= "Rua A", 
                       numero= 333))

print("Mostrar dados do cliente.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco.logradouro}")
print(f"Número: {cliente1.endereco.numero}")