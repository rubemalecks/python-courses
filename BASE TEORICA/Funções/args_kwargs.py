
def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]}\t {kwargs["sobrenome"]}'

print(mostra_nomes(nome='rubem', sobrenome='álecks'))