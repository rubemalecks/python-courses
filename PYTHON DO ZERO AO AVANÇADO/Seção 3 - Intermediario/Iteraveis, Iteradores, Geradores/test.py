import time


def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r




lista = list(range(2))
lista = iter(lista)
print(next(lista))
print(next(lista))
try:
    print(next(lista))
except StopIteration:
    print('parou')
