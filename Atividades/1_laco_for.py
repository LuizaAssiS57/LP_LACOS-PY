import streamlit as st
import time

st.title("ATIVIDADE 1 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escrever um algoritmo que mostra os números pares entre 100 e 120.")

if st.button("INICIAR"):
    for i in range(100, 121, 2):
        st.write(i)
        time.sleep(1)
    st.header("FIM")