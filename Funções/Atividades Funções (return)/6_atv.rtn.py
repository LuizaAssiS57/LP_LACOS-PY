# Escreva um programa que permita ler 3 notas de
# um aluno, usando laço de repetição e informe por
# meio de uma função a média;

import os
os.system('cls')

# Função para calcular e exibir a média.
def media(somar, notas):
    media = somar / notas
    print(f"Média: {media:.2f}")
    return media

# Pergunta ao usuário quantas notas o usuário deseja informar.
nts = int(input("Informe a quantidade de notas: "))

soma = 0
for i in range(nts):
    nota = float(input(f"Informe a {i+1}º nota: "))
    soma += nota

# Chama a função.
media(soma, nts)