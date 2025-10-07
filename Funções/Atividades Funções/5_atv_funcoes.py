import os
os.system('cls')

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