def tiravogal(palavra):
    from copy import copy
    new_palavra = copy(palavra)
    vogais = ('a', 'e', 'i', 'o', 'u')
    for letra in palavra:
        if letra in vogais:
            new_palavra = new_palavra.replace(letra,'_ ')
    return new_palavra


def trocaletra(palavra):
    from copy import copy
    new_palavra = copy(palavra)
    letra_num = ('a', 'e', 'i', 'o', 's')
    numeros = ('4', '3', '1', '0', '5')
    for letra in palavra:
        if letra in letra_num:
            new_palavra = new_palavra.replace(letra, numeros[letra_num.index(letra)])
    return new_palavra
