import os
os.system('cls')

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

if numero < 0:
    numero = 0

print(f"{numeros}")