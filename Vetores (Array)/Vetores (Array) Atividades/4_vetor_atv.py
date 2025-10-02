import os
os.system('cls')

numeros = []
pares = 0
impares = 0

for i in range(6):
    numero = float(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
for numero in numeros:
    print(f"Número: {numero}")
    
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")