import streamlit as st
import time

st.title("ATIVIDADE 3 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escreva um algoritmo que solicite do usuário um número e mostre a tabuada de multiplicação do número informado.")

numero = st.number_input("Informe um número: ", step=1)

if st.button("TABUADA"):
    for i in range(1,11):
        time.sleep(0.5)
        n = numero * i

        st.success(f"{numero} x {i} = {n}")
    st.info("FIM")