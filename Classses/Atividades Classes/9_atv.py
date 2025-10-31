import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: str

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("+=+=+ SOLICITANDO DADOS DO ALUNO +=+=+")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("Nome: "),
        idade=int(input("Idade: ")),
        email=input("E-mail: "),
        telefone=input("Telefone: ")
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados...")
arquivo = "DADOS_ALUNOS.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"\nNome: {aluno.nome}\nIdade: {aluno.idade}\nE-mail: {aluno.email}\nTelefone: {aluno.telefone}\n")
    print("Salvo com sucesso!")