import os
os.system('cls')

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