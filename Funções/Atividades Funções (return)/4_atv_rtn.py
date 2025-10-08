import os
os.system('cls')

def infla(preco):
    if preco >= 200:
        preco_final = preco + (preco * 0.20)
    else:
        preco_final = preco + (preco * 0.10)
    return preco_final

def resultado():
    print(f"Valor a pagar: {preco}")

preco = float(input("Informe o valor do produto: "))

resultado()