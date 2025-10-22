# Escreva um programa que permita ler 2 notas de um aluno e informe
# por meio de funções:
# A nota deve ser entre 0 e 10;
#  A média;
# Com base na média, se o aluno está aprovado ou reprovado.
# Critério para aprovação: média 7,0. 

import os
import time
os.system('cls')

notas = []
QTD_NOTAS = 2
# Função para calcular a média.
def media(notas):
    return sum(notas) / QTD_NOTAS

# Função para verificar se o aluno esta aprovado ou reprovado.
def status(media_final):
    return "Aprovado" if media_final >= 7 else "Reprovado" # Return usando operação ternária

# Função para exibir o boletim.
def boletim(media_final, status):
    print("=== BOLETIM ===")
    print(f"Média: {media_final:.2f}")
    print(f"Aluno(a) está: {status}")

# Pergunta ao usuário quantas notas o usuário deseja informar.

for i in range(QTD_NOTAS):
    while True:
        nota = float(input(f"Informe a {i+1}º nota: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Tente novamente!")
            time.sleep(2)
    
# Chama as funções.
media_aluno = media(notas) 
status_aluno = status(media_aluno)
# Exibe o boletim.
boletim(media_aluno, status_aluno)