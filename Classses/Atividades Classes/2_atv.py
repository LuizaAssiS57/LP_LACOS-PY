import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print("\n=== EXIBINDO DADOS ===")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        


print("=== SOLICITANDO DADOS ===")
pessoa1 = Pessoa(nome= input("\nDigite seu nome: "), 
                 email= input("Digite seu E-mail: "), 
                 telefone= input("Digite seu telefone: "), 
                 endereco= input("Digite seu endereço: "))

pessoa1.mostrar_dados()