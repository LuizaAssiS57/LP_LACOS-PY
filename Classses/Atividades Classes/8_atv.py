import os 
from dataclasses import dataclass
os.system('cls')

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print("=+=+= DETALHES DO LIVRO =+=+=")
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")

livro = Livro(titulo=input("Título: "), 
              ano=int(input("Ano de publicação: ")), 
              autor= Autor(nome=input("Autor: "),
                           biografia=input("Biografia: ")))

os.system('cls')
livro.exibir_detalhes()