import os
os.system('cls')

print("ATIVIDADE 11 | LAÇO DE REPETIÇÃO - WHILE ")
print("""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos das famílias da cidade. 
A prefeitura deseja saber:  

a) total de famílias que responderam a pesquisa;
b) média do salário da população;
c) média do número de filhos;
d) maior salário;
e) menor salário.

Crie um menu com duas opções.
Código   |   Descrição

     1   |   Adicionar família
     2   |   Sair e exibir resultados

O final da leitura de dados se dará com quando o usuário digitar o número código 2. 
""")

salarios = []
filhos = []

while True:
    print("""
             MENU
     1   |   Adicionar família
     2   |   Sair e exibir resultados
""")
    
    codigo = int(input("Código: "))

    if codigo == 1:
        os.system('cls')
        print("----- CADASTRO DE FAMILIAS -----")
        salario = float(input("Salário da família: R$ "))
        numero_de_filhos = int(input("Núemro de filhos: "))
        salarios.append(salario)
        filhos.append(numero_de_filhos)
        os.system('cls')
    elif codigo == 2:
        if len(salarios) == 0:
            print("Nenhuma família foi cadstrada ainda.")
        else:
            total_de_familas = len(salarios)
            media_salario = sum(salarios) / total_de_familas
            media_de_filhos = sum(filhos) / total_de_familas
            maior = max(salarios)
            menor = min(salarios)
            print("----- RESULTADOS DA PESQUISA -----")
            print(f"Total de famílias: {total_de_familas}")
            print(f"Média de salário: {media_salario:.2f}")
            print(f"Média de filhos: {media_de_filhos:.1f}")
            print(f"Maior sálario: {maior:.2f}")
            print(f"Menor salário: {menor:.2f}")
        break
    else:
        print("Código inválido! Tente novamente.")