import os
os.system('cls')

print("ATIVIDADE 8 | LAÇO DE REPETIÇÃO - WHILE ")
print("Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. O final da leitura acontecerá quando for lido um valor negativo. Mostre a média aritmética dos números informados pelo usuário.")

quant_nota = 0
soma = 0

while True:
    nota = int(input("Informe um valor inteiro: "))
    quant_nota += 1

    if nota < 0:
        quant_nota -= 1
        break
    else:
        soma += nota


media = soma / quant_nota

print(f"Média: {media:.2f}")