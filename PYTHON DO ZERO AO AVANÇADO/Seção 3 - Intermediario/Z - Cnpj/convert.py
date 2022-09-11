import re


def remover_caracteres(cnpj):
    return re.sub(r"[^0-9]", "", cnpj)


def cnpj_list(cnpj):
    lista = []
    for n in cnpj:
        lista.append(int(n))
    return lista
