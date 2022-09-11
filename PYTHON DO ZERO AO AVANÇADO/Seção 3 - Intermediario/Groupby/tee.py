iterador_a = iter(range(10))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(iterador_a))

# Esgotou o iterador []
print(list(iterador_a))
# Com tee, ele vai criar 'n' cópias do iterador:

from itertools import tee

iterador_a = iter(range(10))

# Duas cópias (note que o segundo parâmetro tem o padrão de 2)
iterador_a_copia_1, iterador_a_copia_2 = tee(iterador_a, 2)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(iterador_a_copia_1))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(iterador_a_copia_2))
print(list(iterador_a_copia_2))
