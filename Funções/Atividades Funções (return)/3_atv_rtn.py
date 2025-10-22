# Fazer um programa que solicita um valor em metros e por meio de uma função, retorna o correspondente em centímetros.
import os
os.system('cls')

def calc_centimetros(n1):
    return n1 * 100

def resposta(metros, centimetros):
    print(f"{metros} metros equivalem a {centimetros} centímetros.")

n1 = float(input("Informe o valor em metros: "))
resultado = calc_centimetros(n1)
resposta(n1, resultado)