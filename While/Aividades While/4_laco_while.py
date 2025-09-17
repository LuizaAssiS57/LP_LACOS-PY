# import os
# os.system('cls')

# print("ATIVIDADE 3 | LAÇO DE REPETIÇÃO - WHILE")
# print("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

# tentativas = 0
# login_salvo = "luiza.assis"
# senha_salva = "123456"

# for i in range(3):
#         while True:
#             if tentativas >= 3:
#                  break
#             print(f"Tentativa: {tentativas+1}")
#             login = input("LOGIN: ")
#             senha = input("SENHA: ")
#             if login == login_salvo and senha == senha_salva:
#                 print("BEM VINDO(A)!")
#                 break
#             else:
#                 print("Login ou senha inválidos. Tente novamente.")
#                 tentativas += 1
                #tenativas = tentativas + 1
        # if tentativas >= 3:
        #     break            
            
import streamlit as st

st.title("ATIVIDADE 4 | LAÇO DE REPETIÇÃO - WHILE")

st.write("Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

tentativas = 0
login_salvo = "luiza.assis"
senha_salva = "123456"

for i in range(3):
    while :
        if tentativas >= 3:
            break
            st.info(f"Tentativa: {tentativas+1}")
            login = st.text_input("LOGIN: ")
            senha = st.text_input("SENHA: ")
            if login == login_salvo and senha == senha_salva:
                st.success("BEM VINDO(A)!")
                break
            else:
                st.error("Login ou senha inválidos. Tente novamente.")
                tentativas += 1
                #tenativas = tentativas + 1