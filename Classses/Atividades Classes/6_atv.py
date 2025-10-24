import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Endereco:
    logarudouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print("=== DADOS DO CLIENTE ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.logarudouro}, número {self.endereco.numero}, {self.endereco.cidade}-{self.endereco.estado}")

cliente = Cliente(nome=input("Digite seu nome: "), 
                  email= input("Digite seu E-mail: "), 
                  endereco= Endereco(logarudouro= input("Digite seu endereço: "),
                                     numero= int(input("Informe o número: ")),
                                     cidade=input("Informe sua cidade: "),
                                     estado= input("Informe o estado: ").upper()))

os.system('cls')
cliente.mostrar_dados()