import os
os.system('cls')
from dataclasses import dataclass

# Estrutura de dados: Classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Exemplo de uso de classe.
pessoa1 = Pessoa("Alice", 3, "123.456.789-01")
pet1 = Pet("Totó", 4, 4.5)

print("\nExibindo dados da Pessoa.")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}\n")

print("Exibindo dados do Pet.")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}")