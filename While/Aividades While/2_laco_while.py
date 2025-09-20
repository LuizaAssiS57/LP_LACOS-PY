import os
os.system('cls')

print("ATIVIDADE 2 | LAÇO DE REPETIÇÃO - WHILE")
print("Escreva um algoritmo que solicite duas notas para um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Calcule e mostre a média aritmética do aluno.")

QNT_NOTAS = 2
soma = 0

for i in range(QNT_NOTAS):

    while True:
        nota = float(input(f"INFORME A {i+1}° NOTA: "))
        if nota < 0 or nota > 10:
            print("A nota deve ser entre 0 ou 10.")
        else:
            soma += nota
            break

media = soma / QNT_NOTAS

print(f"MÉDIA: {media}")

# Streamlit version

# import streamlit as st

# st.title("ATIVIDADE 2 | LAÇO DE REPETIÇÃO - WHILE")

# st.write("Escreva um algoritmo que solicite duas notas para um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Calcule e mostre a média aritmética do aluno.")

# QNT_NOTAS = 2
# soma = 0

# for i in range(QNT_NOTAS):

#     while True:
#         nota = st.number_input(f"INFORME A {i+1}° NOTA: ", min_value=0, max_value=10)
#         if i < 0 or i > 10:
#             st.warning("A nota deve ser entre 0 ou 10.")
#             break
        
#         soma = soma + nota

# media = soma / QNT_NOTAS

# if st.button("VER MÉDIA"):
#     st.info(f"MÉDIA: {media}")