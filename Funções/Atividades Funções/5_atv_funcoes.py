import os
os.system('cls')

# ATIVIDADE 5 | Funções

# Escreva um programa que permita receber do usuário duas
# notas de um aluno e usando duas funções: 


# - Informe por meio de uma função a média;


# - Informe por meio de uma função se a média for maior ou
# igual a 7, o aluno estará aprovado, caso contrário, estará
# reprovado.

QNT_NOTAS = 2
soma = 0

def media(somar, QNT_NOTAS):
    media = somar / QNT_NOTAS
    print(f"Média: {media}")
    return media

def status(media):
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print(f"Aluno(a) está: {status}")

for i in range(QNT_NOTAS):
    nota = float(input(f"Informe a {i+1}º nota: "))
    soma += nota

boletim = media(soma, QNT_NOTAS)
status(boletim)