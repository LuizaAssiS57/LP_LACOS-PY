import os
os.system('cls')

print("ATIVIDADE 9 | LAÇO DE REPETIÇÃO - WHILE ")
print("Faça um algoritmo que leia uma quantidade não determinada de números inteiros positivos. Calcule: quantidade de números pares e ímpares; média de valores pares média geral dos números lidos. O número que encerrará a leitura será o número zero.")

par = 0
impar = 0
qnt_numero = 0
soma_geral = 0
soma_par = 0

while True:
    numero = int(input("Informe um número inteiro positivo: "))

    if numero == 0:
        break

    qnt_numero += 1
    soma_geral += numero

    if numero % 2 == 0:
        par += 1
        soma_par += numero 
    else:
        impar += 1

    os.system('cls')

if par > 0:
    media_par = soma_par / par
else:
    media_par = 0

media_par = soma_par / par if par != 0 else 0
media_geral = soma_geral / qnt_numero if qnt_numero != 0 else 0

media_geral = soma_geral / qnt_numero

print(f"""
Números par: {par}
Números ímpar: {impar}
Média dos números pares: {media_par:.2f}
Média geral: {media_geral:.2f}
""")
# print(f"Números par: {par}\nNúmeros ímpar: {impar}")
# print(f"")
# print(f"")