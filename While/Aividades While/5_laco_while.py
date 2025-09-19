import os 
os.system('cls')

print("ATIVIDADE 5 | LAÇO DE REPETIÇÃO - WHILE")
print("\nEscreva um algoritmo que leia três notas de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: Se a média for a partir de 7, aprovado; Se a média for entre 5 e 6,9, o aluno está em recuperação; Caso seja menor que 5, o aluno está reprovado.")

tentativas = 0
soma = 0
nota = 0

#for i in range(4):

while True:
    if tentativas >= 4:
        break
    nota = float(input(f"Informe a {nota+1}° nota: "))
        #nota = float(input(f"INFORME A {i+1}° NOTA: ", min_value=0, max_value=10))
    if nota < 0 or nota > 10:
        print("A nota deve ser entre 0 ou 10.")
        break
        
    soma =+ nota

media = soma / 4

if media >= 7:
    status = "aprovado"
elif media >= 5:
    status = "recuperação"
else:
    status = "reprovado"

print(f"MÉDIA: {media}")
print(f"O aluno está {status}")

# Streamlit version

# import streamlit as st

# st.title("ATIVIDADE 5 | LAÇO DE REPETIÇÃO - WHILE")

# st.write("\nEscreva um algoritmo que leia três notas de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente. Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: Se a média for a partir de 7, aprovado; Se a média for entre 5 e 6,9, o aluno está em recuperação; Caso seja menor que 5, o aluno está reprovado.")

# QNT_NOTAS = 3
# soma = 0

# for i in range(QNT_NOTAS):

#     while True:
#         nota = st.number_input(f"INFORME A {i+1}° NOTA: ", min_value=0, max_value=10)
#         if i < 0 or i > 10:
#             st.warning("A nota deve ser entre 0 ou 10.")
#             break
        
#         soma =+ nota

# media = soma / QNT_NOTAS

# if media >= 7:
#     status = "aprovado"
# elif media >= 5:
#     status = "reprovação"
# else:
#     status = "reprovado"

# if st.button("VER MÉDIA"):
#     st.info(f"MÉDIA: {media}")
#     st.info(f"O aluno está {status}")