import os
os.system('cls')

print("ATIVIDADE 10 | LAÇO DE REPETIÇÃO - WHILE ")
print("""
Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, sexo (M/F) e salário. 
Faça um algoritmo que informe:  
      
a) a média de salário do grupo;
b) maior e menor idade do grupo;
c) quantidade de mulheres com salário a partir de R$ 5.000,00.

Crie um menu com três opções.

Código |   Descrição

       1        |   Adicionar pessoa

       2       |   Exibir resultados

       3       |   Sair
O final da leitura de dados se dará com quando o usuário digitar o número código 3. Ao adicionar uma pessoa, deve-se limpar o terminal e apresentar o menu novamente.
""")

idades = []
sexos = []
salarios = []

while True:
    print("""
              MENU
       1     |   Adicionar pessoa
       2     |   Exibir resultados
       3     |   Sair
""")
    
    codigo = int(input("Código: "))

    if codigo == 1:
        os.system('cls')
        print("===== INFORME OS DADOS DA PESSOA =====")
        idade = int(input("IDADE: "))
        sexo = input("SEXO (M/F): ").upper()
        salario = float(input("SALÁRIO: R$ "))
        idades.append(idade)
        sexos.append(sexo)
        salarios.append(salario)
        os.system('cls')
    elif codigo == 2:
        print("===== RESULTADOS =====")
        if len(salarios) == 0:
            print("Nenhuma pessoa cadastrada ainda.")
        else:
            media = sum(salarios) / len(salarios)
            maior = max(idades)
            menor = min(idades)
            mulheres_salarios = 0
            for i in range(len(sexos)):
                if sexos[i] == "F" and salarios[i] >= 5000:
                    mulheres_salarios += 1
            print(f"\nMédia salarial: R$ {media:.2f}")
            print(f"Maior idade: {maior}")
            print(f"Menor idade: {menor}")
            print(f"Mulheres com salário maior que R$ 5.000,00 {mulheres_salarios}")
    elif codigo == 3:
        print("ENCERRANDO...")
        break
    else:
        print("Código inválido! Tente novamente.")