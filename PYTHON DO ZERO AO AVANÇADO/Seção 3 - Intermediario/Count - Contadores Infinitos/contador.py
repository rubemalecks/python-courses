"""
        count - Intertools
"""
# mypy: ignore-errors

from itertools import count

contador = count()

"""
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
"""

# Se não definir um ponto de parada o count() vai seguir infinitamente

# Podemos definir o start, step (INICIO/SALTO)
"""
contador = count(start=7, step=-1)
for valor in contador:
    print(valor)
    if valor <= -10 or valor >= 10:
        break
# é necessário definir um ponto de parada para evitar loops infinitos
"""


# OUTRO EXEMPLO DE USO
contador = count()
nomes = ["Jimm", "Pam", "Michael Scott"]
nomes = list(zip(contador, nomes))
print(nomes)

# Mesmo com novos elementos eles já terão o próprio indice
