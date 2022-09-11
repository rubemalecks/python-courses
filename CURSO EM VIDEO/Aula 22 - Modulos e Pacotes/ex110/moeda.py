'''
Adicione o módulo moeda.py criado nos desafios anteriores, uma função 
chamada resumo(), que mostre na tela algumas informações geradas pelas 
funções que já temos no módulo criado até aqui.
'''
def resumo(preco, aum=10, dim=5):

    print('-'*30)
    print('RESUMO DE VALOR'.center(30))
    print('-'*30)


    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{aum}% de aumento: \t{aumentar(preco, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(preco, dim, True)}')
    print('-'*30)




def aumentar(preco=0, aum_taxa=0, formato=False):
    res = preco + (preco * (aum_taxa/100))
    if formato: 
        return moeda(res)
    return res


def diminuir(preco=0, d_taxa=0, formato=False):
    res = preco - (preco * (d_taxa/100))
    if formato: 
        return moeda(res)
    return res
    

def dobro(preco=0, formato=False):
    res = preco*2
    if formato: 
        return moeda(res)
    return res
    

def metade(preco=0, formato=False):
    res = preco/2
    if formato: 
        return moeda(res)
    return res


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


