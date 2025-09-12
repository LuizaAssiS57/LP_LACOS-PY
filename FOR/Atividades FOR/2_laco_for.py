import streamlit as st
import time

st.title("ATIVIDADE 2 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escrever um algoritmo que moatra os números ímpares entre 1 e 20.")

if st.button ("INICIAR"):
    for i in range(1,21, 2):
        st.write(i)
        time.sleep(0.5)
    st.info("FIM")