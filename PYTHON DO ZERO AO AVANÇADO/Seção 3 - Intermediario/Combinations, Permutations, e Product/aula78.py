# mypy: ignore-errors
"""
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa
Permutação - ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ["Luiz", "Andre", "Eduardo", "Letícia", "Fabrício", "Rose"]

# COMBINATIONS

for grupo in combinations(pessoas, 2):
    print(grupo)

# ('Luiz', 'Andre')
# ('Luiz', 'Eduardo')
# ('Luiz', 'Letícia')
# ('Luiz', 'Fabrício')
# ('Luiz', 'Rose')
# ('Andre', 'Eduardo')
# ('Andre', 'Letícia')
# ('Andre', 'Fabrício')
# ('Andre', 'Rose')
# ('Eduardo', 'Letícia')
# ('Eduardo', 'Fabrício')
# ('Eduardo', 'Rose')
# ('Letícia', 'Fabrício')
# ('Letícia', 'Rose')
# ('Fabrício', 'Rose')

# Retorna todas as combinações possíveis (sem se impostar com a ordem)
# ~ que dizer que a combinação (A, B) é = (B, A), sendo assim ... só uma será retornada.
"""------------------------------"""
# PERMUTATIONS

for grupo in permutations(pessoas, 2):
    print(grupo)  # (a, b) != (b, a)

# OBS: Permutations não considera valores repetidos uma combinação valida.
# para isso usaremos:


# PRODUCT

for grupo in product(pessoas, repeat=3):  # (repeat=2) -> grupos de 2
    print(grupo)
