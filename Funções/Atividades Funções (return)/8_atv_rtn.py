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