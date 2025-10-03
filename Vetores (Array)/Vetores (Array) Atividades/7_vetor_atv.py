import os
os.system('cls')

numeros = []
contador = 0

#USANDO WHILE

while True:
    numero = float(input(f"Digite o {contador+1} número: "))
    contador += 1

    if numero < 0:
        numero = 0
        numeros.append(numero)
    else:
        numeros.append(numero)
    if contador >= 5:
        break
    
for i, numero in enumerate(numeros, start=1):
    print(f"{i}º número: {numero}")

#USANDO FOR

# for i in range(5):
#     numero = float(input(f"Digite o {contador+1} número: "))
#     contador += 1

#     if numero < 0:
#         numero = 0
#         numeros.append(numero)
#     else:
#         numeros.append(numero)

# for i, numero in enumerate(numeros, start=1):
#     print(f"{i}º número: {numero}")