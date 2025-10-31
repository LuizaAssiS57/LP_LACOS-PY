texto_para_salvar = "Texto que você quer salvar"

with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write(texto_para_salvar)

print("O texto foi salvo com sucesso no arquivo meu_arquivo.txt")