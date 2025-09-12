import streamlit as st
import time

st.title("ATIVIDADE 7 | LAÇO DE REPETIÇÃO: FOR")

st.header("Escrever um programa de computador que solicite" \
" do usuário 4 notas e, ao final, apresente a média.")

somar = 0
media = 0

for i in range(1, 5):
    nota = st.number_input(f"Informe a {i}° nota: ")
    somar = somar + nota
    media = somar / 4

if st.button("VER MÉDIA"):
    st.success(f"Média: {media}")