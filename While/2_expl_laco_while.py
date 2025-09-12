import streamlit as st

st.title("LAÇO DE REPETIÇÃO - WHILE")

nota = st.number_input("Digite um número: ", step=1)

if st.button("VERIFICAR"):
    if nota < 0 or nota > 10:
        st.warning("A nota deve ser entre 0 ou 10.")
    else:
        st.info(f"NOTA: {nota}")