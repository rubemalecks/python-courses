string = '012345678901234567890123456789012345678901234567890123456789'
""" # EX1 : separar esta string para retornar uma lista assim: """
# ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
lista = [string[i:i+10] for i in range(0, 60, 10)]
print(lista)
""" 
# Explicação:
~ para cada letra de 'string' no intervalo de (0 até 60, saltando de 10 em 10):
lista = (recebe) o item atual de string(i) até i + 10 (até os proximos 10 itens)
"""

""" # EX2 : Juntar as listas apenas separando por '.' (ponto) """
retorno = '.'.join(lista)
print(retorno)
print('='*23)
