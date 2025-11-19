import os 
os.system('cls')

print("ATIVIDADE 3 | LAÇO DE REPETIÇÃO - WHILE")
print("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

login_slv = "luiza.assis"
senha_slv = "123456"
while True:
    login = input("LOGIN: ")
    senha = input("SENHA: ")
    if login != login_slv or senha != senha_slv:
        print("Login ou senha inválidos. Tente novamente.")
        continue
    else:
        break


# Streamlit version

# import streamlit as st

# st.title("ATIVIDADE 3 | LAÇO DE REPETIÇÃO - WHILE")

# st.write("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")

# login = st.text_input("LOGIN: ")
# senha = st.text_input("SENHA: ", type="password")

# login_salvo = "luiza.assis"
# senha_salva = "123456"

# # while True:
    
# #     if login == login_salvo and senha == senha_salva:
# #         st.success("BEM VINDO(A)")
# #         break
# #     else:
# #         st.error("Login ou senha inválidos. Tente novamente.")

# if st.button("ENTRAR"):
#     if login == login_salvo and senha == senha_salva:
#         st.success("BEM VINDO(A)")
#     else:
#         st.error("Login ou senha inválidos. Tente novamente.")
