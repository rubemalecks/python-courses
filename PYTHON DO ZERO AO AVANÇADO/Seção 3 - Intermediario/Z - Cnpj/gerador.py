from random import randint

from convert import cnpj_list
from verificador import calc_dig


def gera_cnpj():
    primeiro_dig = randint(0, 9)
    segundo_dig = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    cnpj = f"{primeiro_dig}{segundo_dig}{segundo_bloco}{terceiro_bloco}{'0001'}"
    cnpj = cnpj_list(cnpj)
    cnpj.append(calc_dig(cnpj))
    cnpj.append(calc_dig(cnpj))
    return cnpj
