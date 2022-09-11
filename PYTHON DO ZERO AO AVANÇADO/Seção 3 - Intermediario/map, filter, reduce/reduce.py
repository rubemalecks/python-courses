from functools import reduce

from dados import lista, pessoas, produtos

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)  # 55

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades)
