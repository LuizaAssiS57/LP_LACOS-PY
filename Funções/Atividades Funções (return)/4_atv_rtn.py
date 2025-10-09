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