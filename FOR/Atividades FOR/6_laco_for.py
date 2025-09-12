import streamlit as st
import time

st.title("ATIVIDADE 6 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escreva um algoritmo que solicite ao usuário 5 valores" \
" inteiros e ao final mostre: " \
"a. quantos números são pares;" \
"b. quantos números são ímapares;")

pares = 0
impares = 0

for i in range(1,6):
    numero = st.number_input(f"INFORME O {i}° NÚMERO: ", step=1, min_value=0)

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
if st.button("INICIAR"):
    st.info(f"Quantidade de números pares: {pares}")
    st.info(f"Quantidade de números ímpares: {impares}")
else: 
    st.warning("INFORME UM NÚMERO!!")
