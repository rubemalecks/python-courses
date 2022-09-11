"""
Modifique as funções que form criadas no desafio 107 para que 
elas aceitem um parâmetro a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

"""

from moeda import metade, dobro, aumentar, diminuir, moeda

preco = float(input('Digite o preço: R$ '))

print(f'\nA metade de {moeda(preco)} é {metade(preco, True)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}')
print(f'Aumentando 10%, temos {aumentar(preco,10, True)}')
print(f'Reduzindo 13%, temos {diminuir(preco, 13, True)}\n')

