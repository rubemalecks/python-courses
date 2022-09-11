""" Crie um programa que tenha a função leiaInt(), que vai funcionar de 
forma semelhante à função input() do python, só que fazendo a validação 
para aceitar apenas um valor numérico. 

EX: n = leiaInt('Digite um n: ')
"""
import colorama 
colorama.init()


def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO!! digite um número válido.\033[m')

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
