import os
os.system('cls')

# ATIVIDADE 2 | Funções

# Faça um programa que imprime a tabuada de um número
# informado pelo usuário de 1 a 10 utilizando uma função
# para exibir o resultado.

reultado = 0

def tabuada(numero):
    print("=Tabuada=")
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Digite um número: "))
tabuada(numero)