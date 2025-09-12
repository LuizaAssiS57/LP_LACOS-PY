import os
os.system('cls')

print("ATIVIDADE 1 | LAÇO DE REPETIÇÃO - WHILE")
print("Escreva um algoritmo que solicite ao usuário a nota de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Mostre a nota informada pelo usuário.")

while True:
    nota = int(input("Digite uma nota: "))
    if nota >= 0 and nota <= 10:
        break

print("Nota: ", nota)