
from time import sleep

from arquivo.ler import arqExiste, lerArquivo
from arquivo.criar import criar, gravar


def linha(a, b=42):
    print(f'{a}'*b)


# VERIFICAR SE ARQ BASE DA REDE (EXTERNA) EXISTE NA PASTA DO PROGRAMA
if arqExiste('base_rede.txt'):
    ...
else:
    linha('-')
    print('Base da rede NÃO EXISTE!!!!!')
    print('Criando Arquivo...',end='')
    criar('base_rede.txt')
    linha('-')


linha('-')
# VERIFICAR SE ARQ BASE (INTERNO) EXISTE NA PASTA DO PROGRAMA
if arqExiste('base_interna.txt'):
    ...
else:
    linha('-')
    print('Base interna INEXISTENTE!! ')
    print('Criando Arquivo...',end='')
    criar('base_interna.txt')
    linha('-')

relatorio_rede = lerArquivo('base_rede.txt')


relatorio_cadastro = lerArquivo('base_interna.txt')


retirar_rede = list(relatorio_cadastro - relatorio_rede)
add_rede = list(relatorio_rede - relatorio_cadastro)

criar('retirar_rede.txt', False)
gravar('retirar_rede.txt', retirar_rede)


criar('add_rede.txt', False)
gravar('add_rede.txt', add_rede)

