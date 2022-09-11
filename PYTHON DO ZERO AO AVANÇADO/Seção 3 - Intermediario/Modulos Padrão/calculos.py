# https://docs.python.org/pt-br/3/py-modindex.html

import math

PI = math.pi


def dobro(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == "__main__":  # OBS1
    lista = [1, 2, 3, 4, 5]
    print(dobro(lista))
    print(multiplica(lista))
    print(PI)


# OBS1
"""Caso o modulo esteja sendo executado diretamente(o próprio arquivo) a condição "if" (__name__ == '__main__') returna True, caso o contrario (__name__ == 'nome_do_modulo')o que estiver nesse bloco if não será executado.
"""
