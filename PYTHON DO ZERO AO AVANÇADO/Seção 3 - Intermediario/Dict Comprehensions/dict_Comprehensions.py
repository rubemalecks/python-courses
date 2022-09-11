'''
Dict Comprehensions
Dict Comprehensions foram introduzidas na linguagem através da especificação PEP 274.

Sua sintaxe básica é:


# {chave: valor for elemento in iteravel}


chave: será a chave de cada elemento do dicionário resultante.
valor: valor daquela chave.
elemento: é a unidade de iteração do iterável iterável (se for uma lista, por exemplo, elemento irá receber o valor iteração à iteração)
iteravel: conjunto de dados que estão sendo iterados (pode ser uma lista ou um set, por exemplo)
Pra esclarecer, vamos à um exemplo:
'''
import locale

dicionario = {elemento: elemento*2 for elemento in range(6)}
print(dicionario)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# cada elemento da lista de range(6) (0, 1, 2, 3, 4, 5) será convertido em uma chave própria
# (elemento*2) - será o valor de cada chave, ex: o valor da chave será (chave x 2)

'''Outro exemplo, com chaves alfabéticas e manipulação de strings com f-strings:'''

lista = ['Ferrari', 'Lamborghini', 'Porshe']
dicionario = {
    f'{elemento.lower()}': f'Montadora: {elemento.upper()}' for elemento in lista
}
print(dicionario)

'''
# Configura o locale pra Português do Brasil (pt_BR)
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')


carros_esportivos = {
    'ferrari': 1299000,
    'lamborghini': 1100000,
    'porsche': 759000
}


dict_saida = {
    chave: f'{chave.upper()}: {locale.currency(valor)}' for chave, valor in carros_esportivos.items()
}

print(dict_saida)
'''
