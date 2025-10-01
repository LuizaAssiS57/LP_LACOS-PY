import os 
os.system('cls')

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}º nota: "))
    notas.append(nota)

# print(f"Notas: {notas}")

for i in range(3):
    print(f"Nota: {notas[i]}")

print(f"Soma: {sum(notas)}")