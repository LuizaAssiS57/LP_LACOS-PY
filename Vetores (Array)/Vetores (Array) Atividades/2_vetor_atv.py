import os
os.system('cls')

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    status = "Aprovado"
elif media >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"Notas: {notas}")
print(f"Média: {media}")
print(f"Status: {status}")