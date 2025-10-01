import os
os.system('cls')

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

for i in range(3):
    print(f"Nota: {notas[i]}")

print(f"Média: {media:.2f}")