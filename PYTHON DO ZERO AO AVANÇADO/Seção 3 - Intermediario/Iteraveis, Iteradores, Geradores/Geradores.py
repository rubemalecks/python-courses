import sys
import time
from types import GeneratorType

lista = list(range(0, 1000))

# >>> print(sys.getsizeof(lista))  # Retorna o tamanho ocupado na memoria por
# este 'objeto'


"""
Na forma mostrada acima, a lista vai reter todos os valores e armazena na
memória, se quisermos otimizar nosso código, não seria ideal salvar todos os
valores na memória.
"""


# Podemos usar Geradores para evitar este problema, cada vez que precisarmos
# deste valor irem


# Geradores vão todos os valores mas não salva todos na memoria

"""' Função Simples [exemplo1]"""


"""
def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()
for v in g:
    print(v)
"""

# GERADOR [exemplo2]

"""

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()  # >>> g -->> <generator object gera at 0x000002025AC36030>


# for v in g:
#     print(v)
# Os valores aparecem na hora da execução, ao invés de esperar todos como no [exemplo1]

print(hasattr(g, "__next__"))  # True
print(hasattr(g, "__iter__"))  # True

# O gerador é um iterador e um iterável, ou seja... podemos imprimir os valor
# sem a obrigatoriedade do uso do laço for/while, assim:

print(next(g))
print(next(g))
print(next(g))

"""

# OUTRO EXEMPLO[3] DE USO:

"""
def gera():
    variavel = "Valor 1"
    yield variavel
    variavel = "Valor 2"
    yield variavel
    variavel = "Valor 3"
    yield variavel


g = gera()

print(next(g))
print(next(g))
print(next(g))

"""
"""
________________________________________________________
Caso chamemos pela terceira vez ...
"""
# >>> print(next(g))
# já que não há + nenhuma valor o python vai levantar uma exceção chamada StopIteration


"""Exemplo [4]"""

l1 = [x for x in range(1000)]  # lista --> <class 'list'>
l2 = (x for x in range(1000))  # gerador --> <class 'generator'>
print(f"l1 ocupa {sys.getsizeof(l1)} na memoria")
print(f"l2 ocupa {sys.getsizeof(l2)} na memoria")


# Finalizando ...
variavel = zip("alo", "alo")
print(isinstance(variavel, GeneratorType))  # VERIFICOU SE VARIAVEL É DO TIPO GERADOR

# PODEMOS TRANSFORMAR EM UM DESTA FORMA

variavel = ((x, y) for x, y in zip("alo", "alo"))
print(isinstance(variavel, GeneratorType))  # é um gerador
print(list(variavel))
