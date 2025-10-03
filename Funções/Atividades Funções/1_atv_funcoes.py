import os
os.system('cls')

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