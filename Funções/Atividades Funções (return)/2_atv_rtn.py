# Crie funções que recebam 2 números e retorne a soma,
# subtração, divisão e a multiplicação destes dois números
# informados.
# Obs.: Crie uma função para cada operação.

import os
import time

os.system('cls')

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(2) # Espera 2 segundos.
    os.system("cls")

# Funções de cada operação.
# Funções com parâmetros e com retorno.
def somar(n1, n2):
    soma = n1 + n2
    return soma

def subtrair(n1, n2):
    subtracao = n1 - n2
    return subtracao

def dividir(n1, n2):
    return n1 / n2 if n2 != 0 else "Divisão por zero"

def multiplicar(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

# Função para exibir os resultados.
# Função sem parâmetros e sem retorno. 
def resultado():
    print("\n=== RESULTADOS ===")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Divisão: {divisao}")
    print(f"Multiplicação: {multiplicacao}")

# Código principal.
# Função sem parâmetros e sem retorno. 
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Função com parâmetros e com retorno.
# Chamando e associando as funções.
soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)
multiplicacao = multiplicar(primeiro_numero, segundo_numero)

# Chamando a função para exibir os resultados.
resultado()