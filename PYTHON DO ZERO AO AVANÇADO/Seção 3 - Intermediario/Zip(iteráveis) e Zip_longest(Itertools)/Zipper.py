""""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
# A FUNÇÃO ZIP RETORNA UM NEXT(INTERADOR)
from itertools import count, zip_longest

# CÓDIGO
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]
estados = ["SP", "MG", "BA"]
cidades_estados = zip(estados, cidades)  # só vai unir até a menor lista

# print(list(cidades_estados))
# -----------------------------------------------


# CÓDIGO 2
estados = ["SP", "MG", "BA"]
cidades_estados = zip_longest(estados, cidades)  # só vai unir até a menor lista
# print(list(cidades_estados))  # Vai completar a menor lista com 'None'
# ---------------------------
# Caso queira predefinir um valor no lugar de 'None'
# USE O 'fillvalue'
cidades_estados = zip_longest(estados, cidades, fillvalue="Estado")
# print(list(cidades_estados))

# -----------------------------------------------
# CODIGO 3
indice = count()
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]
estados = ["SP", "MG", "BA"]
cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

# no código 3 voltamos a utilizar o zip, pois no zip_longest poderia ser
# executado infinitamente devido ao indice (indice = count()) ser um contador.
