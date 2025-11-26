import os
os.system("cls || clear")

while True:
    print("""
            MENU
    CREATE | 1
    READ   | 2
    UPDATE | 3
    DELETE | 4
    """)

    lista_clientes = []

    codigo = int(input("Código: "))

    match codigo:
        case 1:
            print("=+= CREATE =+=")
            nome = input("Nome: ")
            lista_clientes.append(nome)
            print(f"O nome: {nome} foi inserido com sucesso!")
        case 2:
            print("=+= READ =+=")
            print(lista_clientes)
        case 3:
            print("=+= UPDATE =+=") 
            nome_para_atualizar = input("Qual nome deseja atualizar? ")
            if nome_para_atualizar in lista_clientes:
                novo_nome = input("Novo nome: ")
                indice = lista_clientes.index(nome_para_atualizar)
                lista_clientes[indice] = novo_nome
                print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
            else:
                print(f"O nome {nome_para_atualizar} não foi encontrado.")

            print(lista_clientes)
        case 4:
            print("=+= DELETE =+=")
            nome_para_excluir = input("Qual nome deseja excluir? ")
            if nome_para_excluir in lista_clientes:
                lista_clientes.remove(nome_para_excluir)
                print(f"{nome_para_excluir} foi excluído com sucesso!")
            else:
                print(f"O nome {nome_para_excluir} não foi encontrado.")

            print(lista_clientes)
        case _:
            print("Código inválido.")

    continuar = input("Deseja continuar? (S/N) ").upper()
    if continuar != "S":
        break