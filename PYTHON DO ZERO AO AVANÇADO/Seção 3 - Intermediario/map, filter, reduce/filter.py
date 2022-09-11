from dados import lista, pessoas, produtos
#
# Sintaxe

# filter(func, sequencia)
# func -> filtro definido por 'def' ou 'lambda'
# sequencia -> qualquer sequencia (lista, dicionario e etc...)
"""
nova_lista = filter(lambda x: x > 5, lista)  # filter(func[bool], sequencia)
print(list(nova_lista))
nova_lista = [x for x in lista if x > 5]  # faz o mesmo
print(nova_lista)

nova_lista = filter(lambda p: p["preco"] > 50, produtos)
for prod in nova_lista:
    print(prod)
"""
# ao invés do lambda, podemos usar uma função especifica
"""
def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
        return True
nova_lista = filter(filtra, produtos)
for prod in nova_lista:
    print(prod)
"""


def maior_idd(pessoas):
    if pessoas["idade"] >= 18:
        return True


nova_lista = filter(maior_idd, pessoas)
for p in nova_lista:
    print(p)
