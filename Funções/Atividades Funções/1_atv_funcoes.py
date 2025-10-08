import os
os.system('cls')

# ATIVIDADE 1 | Funções

# def saudacao(nome):

#     print(f"Olá, {nome}! Bem-vindo(a) ao nosso site.")


# # Exemplo de uso da função

# nome_visitante = "Marta"

# saudacao(nome_visitante)
# Modifique o código acima solicitando ao usuário que
# informe o nome para ser exibido na mensagem de boas-
# vindas.

def saudacao(nome, idade, altura, peso):
    print(f"Olá, {nome}! Bem-vindo(a) ao nosso site.")
    print(f"Sua idade é {idade} anos.")
    print(f"Você tem {altura}cm de altura.")
    print(f"Você pesa {peso}Kg.")

print("Solicitando dados...")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
saudacao(nome, idade, altura, peso)