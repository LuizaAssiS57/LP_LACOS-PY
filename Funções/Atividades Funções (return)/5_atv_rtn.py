import os
import datetime

os.system('cls')

def idade(ano_nas, ano_atual):
    ano_atual = datetime.date.today().year
    idade_atual = ano_atual - ano_nas
    return idade



