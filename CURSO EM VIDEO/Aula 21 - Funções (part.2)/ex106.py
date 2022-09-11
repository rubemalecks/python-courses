""""
Faça um mini-sistema que utilize o InteractiveHelp do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o
programa se encerrará.

OBS: Use Cores.
"""

import colorama
colorama.init()

from time import sleep

c = ( # CORES
    '\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m',       # 6 - branco
    )


comando = ''


# FUNÇÃO PRINCIPAL
def ajuda(com):
    help(com)

# FUNÇÃO DE MENSAGEM
def txt(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
<<<<<<< HEAD
    print('~' * tam, c[0])
=======
    print('~' * tam)
    print(c[0], end='')
>>>>>>> 7cc14a4f0bb06971c43acbe0e82f51030aba6c1d

txt('SISTEMA DE AJUDA PyHELP', 2)

# PROGRAMA PRINCIPAL - HELP
<<<<<<< HEAD
while True:
=======
while comando == '':
>>>>>>> 7cc14a4f0bb06971c43acbe0e82f51030aba6c1d
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando.upper() == 'FIM':
        break
    else:
        txt(f'Acessando o manual do comando \'{comando}\'', 4)
        print(c[5])
        ajuda(comando)
        print(c[0])
<<<<<<< HEAD

txt('ATÉ LOGO!', 1)
=======
txt('ATÉ LOGO!', 1)
>>>>>>> 7cc14a4f0bb06971c43acbe0e82f51030aba6c1d
