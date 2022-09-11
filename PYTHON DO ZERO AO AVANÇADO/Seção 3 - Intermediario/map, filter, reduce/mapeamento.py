from dados import lista, pessoas, produtos

'''
nova_lista = map(lambda x: x * 2, lista)
print(nova_lista)  # map() retorna iterador
print(lista)
print(list(nova_lista))  # para ver a lista podemos fazer um typecasting
'''

# Com listcomprehension
'''
nova_lista = [x * 2 for x in lista]
print(nova_lista)
'''
'''
 # exemplo
precos = map(lambda p: p['preco'], produtos)
print(list(precos)) 
'''

'''
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2) # round (valor, casas_decimais)
    return p

novos_produtos = map(aumenta_preco, produtos)
for prod in novos_produtos:
    print(prod)


nomes = map(lambda n: n['idade'] * 1.20, pessoas)

for n in nomes:
    print(n)
'''

