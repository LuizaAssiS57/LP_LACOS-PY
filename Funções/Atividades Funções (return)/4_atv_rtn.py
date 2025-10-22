# Fazer um programa que solicita o preço de um produto e
# inflaciona esse preço em 10% se ele for menor que 100 e
# em 20% se ele for maior ou igual a 100. 
# Utilize uma função com retorno para obter o resultado
# solicitado.

import os
os.system('cls')

# Função para calcular a inflação do preço.
def infla(preco):
    if preco <= 100:
        preco_final = preco * 1.10
    else:
        preco_final = preco * 1.20
    return preco_final

# Função para exibir o preço final.
def resultado(preco_final):
    print(f"Valor a pagar: {preco_final:.2f}")

preco = float(input("Informe o valor do produto: R$ "))
# Chamando as funções.
preco_corri = infla(preco)
resultado(preco_corri)