"""
Faça um programa que tenha um função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)

Adicione também docstring da função.
"""

def notas(*x_notas, sit=False):
    """[Analise de Notas]

    Args:
        x_notas (list): [Lista de Notas].
        sit (bool, optional): [True or False]. Defaults to False.
        

    Returns:
        [dict]: [dados finais]
        [bool]: [arg opcional com situacao da turma]
    """
    from statistics import mean
    qtd_notas = len(x_notas)
    maior_nota = max(x_notas)
    menor_nota = min(x_notas)
    media_notas = mean(x_notas)
    if media_notas >= 7:
        avaliacao = 'BOA'
    elif media_notas >= 5:
        avaliacao = 'RAZOÁVEL'
    else: 
        avaliacao = 'RUIM'
    if sit:
        dados_finais = {'Total de Notas: ': qtd_notas, 'Maior Nota': maior_nota, 'Menor Nota': menor_nota, 'Médias Finais': media_notas, 'Situação': avaliacao}
        return dados_finais
    else:
        dados_finais = {'Total de Notas: ': qtd_notas, 'Maior Nota': maior_nota, 'Menor Nota': menor_nota, 'Médias Finais': media_notas}
        return dados_finais

help(notas)
print(notas(5.5, 2.5, 1.5))
