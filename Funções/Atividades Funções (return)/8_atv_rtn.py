# O índice de massa corpórea (IMC) de um indivíduo é obtido dividindo-se o seu peso (em Kg) por sua altura (em metros) ao quadrado. 
# Assim, por exemplo, uma pessoa de 1,67m e pesando 55kg tem IMC igual a 20,14, já que:
# Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg e de sua altura em m e a partir deles calcule o índice de massa corpórea do utilizador.

import os
os.system('cls')

# Função para calcular o IMC.
def calc_imc(peso, altura):
    return peso / (altura ** 2)

# Função para exibir o IMC.
def exibir(imc):
    print(f"Seu IMC é: {imc:.2f}")

# Entrada de dados.
peso = float(input("Digite seu peso: KG "))
altura = float(input("Digite sua altura: "))

# Chama as funções.
exibir(calc_imc(peso, altura))