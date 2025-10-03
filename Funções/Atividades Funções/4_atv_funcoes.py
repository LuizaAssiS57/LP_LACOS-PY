import os
os.system('cls')

reultado = 0

def tabuada(numero):
    print("=Tabuada=")
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Digite um número: "))
tabuada(numero)