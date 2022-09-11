# https://docs.python.org/pt-br/3/library/functions.html#open

file = open("abc.txt", "w+")  # 'w+' ABRIR E REESCREVER
file.write("Linha 1\n")
file.write("Linha 2\n")
file.write("Linha 3\n")

file.seek(0, 0)  # Voltar par o inicio do arquivo
# Caso não volte ao inicio o arquivo ficaria sem nada para ler
print("Lendo linhas: ")
print(file.read())
print("############")
file.seek(0, 0)
print(file.readline(), end="")  # ler linha por linha
print(file.readline(), end="")
print(file.readline(), end="")


file.seek(0, 0)
print(file.readlines(), end="")  # destaque para o 'S', retorna uma lista
file.close()
