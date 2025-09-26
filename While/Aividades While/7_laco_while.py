import os 
os.system('cls')

print("ATIVIDADE 7 | LAÇO DE REPETIÇÃO - WHILE")
print("Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, se a resposta do usuário for “N”, o programa fará a média aritmética das notas informadas e mostrará a média aritmética para o usuário. Obs.: Use um contador dentro do laço de repetição para contar a quantidade de iterações (loops).")

qnt_nota = 0
soma = 0
contador = 0

while True:
    nota = float(input("Informe a nota do aluno: "))

    soma += nota
    qnt_nota += 1
    contador += 1

    media = soma / qnt_nota

    otr_nota = input("Deseja adicionar outra nota? (S/N) ").upper()

    if otr_nota == "N":
        break

print(f"Média: {media:.2f}")
print(f"Quantidade de notas: {contador}")