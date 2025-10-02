import os
os.system('cls')

numeros = []
soma_positivos = 0
negativos = 0

for i in range(5):
    numero = float(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

for i in numeros:
    if i < 0:
        negativos += 1
    else: 
        soma_positivos += numero
        
print(f"Negativos: {negativos}")
print(f"Soma dos positivos: {soma_positivos}")