"""
Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como uma valor monetário formatado.
"""

from moeda import metade, dobro, aumentar, diminuir, moeda

preco = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(aumentar(preco,10))}')
