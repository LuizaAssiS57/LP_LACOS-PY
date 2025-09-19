import os 
os.system('cls')

qnt_nota = 0
soma = 0

while True:
    nota = float(input("Informe a nota do aluno: "))

    soma += nota
    qnt_nota += 1

    media = soma / qnt_nota

    otr_nota = input("Deseja adicionar outra nota? (S/N) ").upper()

    if otr_nota == "N":
        break

print(f"Média: {media:.2f}")