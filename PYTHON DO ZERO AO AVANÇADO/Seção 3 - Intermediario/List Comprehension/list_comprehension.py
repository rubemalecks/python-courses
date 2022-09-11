"""from random import randint

numeros = [numero + 1 for numero in range(0, 14) if numero % 2 == 0]
print(numeros)


sort_num = [randint(1, 60) for c in range(10)]
# print(sort_num)

squares = list(map(lambda x: randint(1, 60), range(10)))

print(sorted(squares))
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
# print(ex3)

test = [(a, b) for a in range(3)
        for b in range(3)]  # vão acontecer 2 "for" ao mesmo tempo
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print(test)

