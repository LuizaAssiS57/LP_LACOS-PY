import os
os.system('cls')

# Função para calcular a média.
def media(qtd_notas, notas):
    return notas / qtd_notas

# Função para verificar se o aluno esta aprovado ou reprovado.
def status(media_final):
    return "Aprovado" if media_final >= 7 else "Reprovado"

# Função para exibir o boletim.
def boletim(media_final, status):
    print(f"Média: {media_final:.2f}")
    print(f"Aluno(a) está: {status}")


# Pergunta ao usuário quantas notas o usuário deseja informar.
qtd_notas = int(input("Informe a quantidade de notas: "))
notas = 0

for i in range(qtd_notas):
    nota = float(input(f"Informe a {i+1}º nota: "))
    notas += nota

# Chama as funções.
media_aluno = media(qtd_notas, notas) 
status_aluno = status(media_aluno)
# Exibe o boletim.
boletim(media_aluno, status_aluno)