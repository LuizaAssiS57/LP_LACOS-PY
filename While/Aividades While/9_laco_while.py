import os
os.system('cls')

par = 0
impar = 0
qnt_numero = 0
soma_geral = 0

while True:
    numero = int(input("Informe um número inteiro positivo: "))
    qnt_numero += 1
    soma_geral += numero

    if numero % 2 == 0:
        par += 1
        #media_par = 
    else:
        impar += 1

    os.system('cls')

    if numero == 0:
        break

media_geral = soma_geral / qnt_numero

print(f"Valores par: {par}\nValores ímpar: {impar}")
print(f"Média geral: {media_geral}")