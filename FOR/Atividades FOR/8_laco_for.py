import streamlit as st
import time

st.title("ATIVIDADE 8 | LAÇO DE REPETIÇÃO: FOR")

st.subheader("Escrever um programa de computador que solicite do usuário 3 notas" \
" e, ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado." \
" Considere que para aprovação, deve-se obter média maior ou igual a 7, " \
"para ser reprovado, a média deve ser menor que 4.")

soma = 0
media = 0

for i in range(3):
    nota = st.number_input(f"INFORME A {i+1}° NOTA: ", min_value=0, max_value=10)
    soma = soma + nota
    media = soma / 3

    if media >= 7:
        status = "Aprovado"
    elif media >= 4:
        status = "Recuperação"
    else:
        status = "Reprovado"

if st.button("VERIFICAR"):
    st.info(f"Média: {media:.1f}")
    st.success(f"Status: {status}")

    if status == "Aprovado":
        st.balloons()
    else:
        st.snow()