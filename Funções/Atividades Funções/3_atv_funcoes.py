import os
os.system('cls')

# ATIVIDADE 3 | Funções

# Crie uma função  que receba um número e mostre uma
# mensagem informando se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.") 
        
numero = float(input("Digite um número: "))
par_ou_impar(numero)