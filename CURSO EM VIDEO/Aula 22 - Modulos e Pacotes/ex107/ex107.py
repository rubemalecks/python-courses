"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Ler um preço 
# informar a metade, dobro, e aumentar e diminuir % com base no argumento passado pelo usuario.
"""
from moeda import metade, dobro, aumentar, diminuir

preco = float(input('Digite o preço: R$ '))

print(f'A metade de {preco} é R$ {metade(preco)}')
print(f'O dobro de {preco} é R$ {dobro(preco)}')
print(f'Aumentando 10%, temos R$ {aumentar(preco,10)}')
