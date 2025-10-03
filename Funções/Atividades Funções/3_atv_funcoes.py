import os
os.system('cls')

def positivo_negativo(numero):
    if numero < 0:
        print("O número é negatvo.")
    else:
        print("O número é positivo.")

numero = int(input("Digite um número: "))
positivo_negativo(numero)