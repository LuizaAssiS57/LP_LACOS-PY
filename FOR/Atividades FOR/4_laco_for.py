import streamlit as st
import time

st.title("ATIVIDADE 4 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escreva um algoritmo que solicite ao usuário um número" \
" e faça a contagem regressiva a partir do número informado até o número 1," \
" aguardando um segundo para exibri cada número.")

numero = st.number_input("Escolha um número: ", step=1)

if st.button("INICIAR"):
    for i in range(numero, 0, -1):
        st.info(i)
        time.sleep(1)

    st.success("💀")
    st.balloons()