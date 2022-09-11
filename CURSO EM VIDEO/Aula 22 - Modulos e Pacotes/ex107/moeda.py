"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro()e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Ler um preço 
# informar a metade, dobro, e aumentar 10% e diminuir 13%.
"""

def aumentar(preco, taxa=0):
    res = preco + (preco * (taxa/100))
    return res

def diminuir(preco, taxa=0):
    res = preco - (preco * (taxa/100))
    return res

def dobro(preco):
    res =  preco*2
    return res

def metade(preco):
    res = preco/2
    return res

