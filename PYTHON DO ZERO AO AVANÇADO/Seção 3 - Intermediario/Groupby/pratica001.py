from itertools import groupby, tee

pessoas = [
    {"Nome": "Rubem", "idade": 23, "Genero": "masculino"},
    {"Nome": "Rebeca", "idade": 19, "Genero": "feminino"},
    {"Nome": "Jimm", "idade": 28, "Genero": "masculino"},
    {"Nome": "Pam", "idade": 25, "Genero": "feminino"},
]


# def ordem(item):
#     return item["Genero"]

ordem = lambda item : item['Genero']
pessoas.sort(key=ordem)

pessoas_agrupadas = groupby(pessoas, ordem)

for genero, valores_agrupados in pessoas_agrupadas:
    print(f"Genero: {genero}")
    for pessoas in valores_agrupados:
        print(pessoas)
