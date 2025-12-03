import os
import time
from dataclasses import dataclass

os.system('cls || clear')  # Limpar terminal

lista_alunos = []

@dataclass
class Endereco:
    logarudouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str
    nascimento: str
    ra: str
    curso: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.nascimento} \nR.A.: {self.ra} \nCurso: {self.curso} \nEndereço: {self.endereco.logarudouro}, número {self.endereco.numero}, {self.endereco.cidade}-{self.endereco.estado}")

# Verificar se a lista está vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print('\nNão há alunos cadastrados.')
        return True
    return False

# Adicionar aluno
def adicionar_alunos(lista_alunos):
    print('\n+=+=+=+ ADICIONAR ALUNO +=+=+=+')
    nome = input('Nome: ')
    nascimento = input('Data de Nascimento: ')
    ra = input('R.A.: ')
    curso = input('Curso: ')
    endereco = Endereco(logarudouro= input("Digite o endereço: "),
                                     numero= int(input("Informe o número: ")),
                                     cidade=input("Informe sua cidade: "),
                                     estado= input("Informe o estado: ").upper())

    novo_aluno = Aluno(nome=nome, nascimento=nascimento, ra=ra, curso=curso, endereco=endereco.logarudouro, endereco=endereco.numero, endereco=endereco.cidade, endereco=endereco.estado)
    lista_alunos.append(novo_aluno)

    print(f'\nAluno {nome} adicionado com sucesso!')

# Encontrar aluno por R.A.
def encontrar_por_ra(lista_alunos, ra_buscar):
    for aluno in lista_alunos:
        if aluno.ra == ra_buscar:
            return aluno
    return None

# Mostrar todos os alunos
def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    print('\n===== LISTA DE ALUNOS =====')
    for aluno in lista_alunos:
        aluno.mostrar_dados()

# Atualizar aluno
def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)

    print('\n++++++ ATUALIZAR DADOS DO ALUNO ++++++')
    ra_buscar = input('Digite o R.A. do aluno: ')
    aluno = encontrar_por_ra(lista_alunos, ra_buscar)

    if aluno:
        print('\nAluno encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome: {aluno.nome}')
        novo_nome = input('Novo nome: ')

        print(f'Data de Nascimento: {aluno.nascimento}')
        novo_nascimento = input('Atualização: ')

        print(f'Antigo R.A.: {aluno.ra}')
        novo_ra = input('Novo R.A.: ')

        print(f'Curso atual: {aluno.curso}')
        novo_curso = input('Novo curso: ')

        print(f'Endereço atual: {aluno.endereco}')
        novo_endereco = input('Novo endereço: ')

        if novo_nome:
            aluno.nome = novo_nome
        if novo_nascimento:
            aluno.nascimento = novo_nascimento
        if novo_ra:
            aluno.ra = novo_ra
        if novo_curso:
            aluno.curso = novo_curso
        if novo_endereco:
            aluno.endereco = novo_endereco

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nCPF {ra_buscar} não encontrado.')

# Excluir aluno
def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)

    ra_buscar = input('\nDigite o R.A. do aluno que deseja excluir: ')
    aluno = encontrar_por_ra(lista_alunos, ra_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print(f'\nAluno {aluno.ra} excluído com sucesso!')
    else:
        print('\nAluno não encontrado.')

# MENU PRINCIPAL
while True:
    print("""
===== GERENCIADOR DE ALUNOS =====
1  |  ADICIONAR
2  |  MOSTRAR TODOS
3  |  ATUALIZAR
4  |  EXCLUIR
0  |  SAIR
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_alunos(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 1 and opcao != 0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")