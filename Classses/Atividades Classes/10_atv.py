import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 3
lista_livros = []

print(" =+= SOLICITANDO DADOS =+= ")
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        nome= input("Nome da obra: "),
        autor= input("Autor: "),
        categoria= input("Categoria: "),
        preco= float(input("Preço: "))
    )
    lista_livros.append(livro)

print()
print(" ¨+¨ SALVANDO DADOS ¨+¨ ")
arquivo = "catalogos.txt"

with open(arquivo, "a") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"Nome: {livro.nome}\nAutor: {livro.autor}\nCategoria: {livro.categoria}\nPreço: R${livro.preco}\n")
    print("SALVO COM SUCESSO! :)")