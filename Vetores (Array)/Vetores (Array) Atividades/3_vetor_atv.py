import os
os.system('cls')

numeros = []

for i in range(5):
    numero = float(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)
for i in range(5):
    print(f"Números informados: {numeros[i]}")

print(f"Menor número: {min(numeros)}")
print(f"Maior número: {max(numeros)}")