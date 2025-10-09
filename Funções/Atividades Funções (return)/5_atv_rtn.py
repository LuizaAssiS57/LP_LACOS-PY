import os
import datetime

os.system('cls')

# Função para calcular a idade do usuário.
def idade(ano_nas):
    ano_atual = datetime.date.today().year # Tira do sistema o ano atual.
    idade_atual = ano_atual - ano_nas
    return idade_atual

# Função para exibir a idade.
def exibir(idade_atual):
    print(f"Você tem {idade_atual} anos.")

ano_nas = int(input("Digite seu ano de nascimento: "))

# Chama a função idade() e passa o resultado diretamente para a função exibir() 
exibir(idade(ano_nas))