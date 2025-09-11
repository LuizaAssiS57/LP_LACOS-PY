import streamlit as st
import time

st.title("ATIVIDADE 5 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escrever um programa de computador que solicite do usuário" \
" 5 números inteiros e, ao final, apresente a soma de todos os números lidos.")


soma = 0

for i in range(1,6):
    numero = st.number_input(f"INFORME O {i}° NÚMERO: ", step=1, min_value=0)
    time.sleep(0.5)
    soma = soma + numero

if st.button("CALCULAR"):
    st.success(f"A soma dos números é: {soma}")
    st.balloons()
else:
    st.info("INFORME UM NÚMERO")