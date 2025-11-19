import os
os.system('cls')

print("ATIVIDADE 6 | LAÇO DE REPETIÇÃO - WHILE")
print("Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante para uma pessoa. A pessoa vai escolher o prato desejado. Após escolher o prato, o algoritmo deve perguntar ao usuário se ele deseja escolher outro prato. Calcule quanto deve ser pago pelo cliente.")

vlr_total = 0

while True:

    print("""
CÓDIGO      PRATO            VALOR
    1       Picanha          R$ 25,00
    2       Lasanha          R$ 20,00
    3       Strogonoff       R$ 18,00
    4       Bife Acebolado   R$ 15,00
    5       Pão com ovo      R$ 5,00
  SELECIONE 0 PARA FINALIZAR O PEDIDO
""")

    codigo = int(input("Código: "))
    if codigo == 0:
        break

    match codigo:
            case 1:
                prato = "Picanha"
                valor = 25.0
            case 2:
                prato = "Lasanha"
                valor = 20.0
            case 3:
                prato = "Strogonoff"
                valor = 18.0
            case 4:
                prato = "Bife Acebolado"
                valor = 15.0
            case 5:
                prato = "Pão com ovo"
                valor = 5.0
            case _:
                print("O código não corresponde a um dos pratos disponiveis!")

    vlr_total += valor

    mais_pedidos = input("Deseja fazer outro pedido? (S/N)").upper()

    os.system("cls")

    if mais_pedidos == "N":
        break

print(f"Valor a pagar: {vlr_total}")