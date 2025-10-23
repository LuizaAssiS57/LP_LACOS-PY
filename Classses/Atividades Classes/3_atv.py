import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print("=== DADOS DE ENTREGA ===")
        print(f"\nNome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print("\n==== DADOS DE MARKETING ====")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

print("===== SOLICITANDO DADOS =====")
cliente1 = Cliente(nome= input("DIGITE SEU NOME: "), 
                   email= input("DIGITE SEU E-MAIL: "),
                   endereco= input("DIGITE SEU ENDEREÇO: "))

os.system('cls')
cliente1.dados_entrega()
cliente1.dados_email_marketing()