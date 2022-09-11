"""
    Faça um programa que tenha uma função chamada ficha(), que receba 2 parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado 
não tenha sido informado corretamente.
"""

def scout_soccer(nome='<desconhecido>', gols=0):
    """[Ficha de Dados do Jogador]

    Args:
        nome (str, optional): [Nome do Jogador]. Defaults to 'desconhecido'.
        gols (int, optional): [Quantidade de Gols]. Defaults to 0.

    Returns:
        [dict]: [nome: nome do jogador, gols: quantidade de gols]
    """

    dados = {'nome': nome, 'gols': gols}

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')



n = str(input('Nome do Jogador: '))
g = str(input('Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '': # se nome for vazio
    scout_soccer(gols=g)
else:
    scout_soccer(n, g)