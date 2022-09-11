# flake8: ignore-errors
# Funções anônimas / expressões lambda
l = lambda x: x * 2  # no terminal >>> (lambda x: x*2)(7)
print(l(7))  # atribuímos a função objeto a uma variável

# syntax

# lambda arguments: expression  # ignore_line


# Exemplo + Avançado:

pessoas = [
    {"Nome": "Rubem", "idade": 23},
    {"Nome": "Rebeca", "idade": 19},
    {"Nome": "Jimm", "idade": 28},
    {"Nome": "Pam", "idade": 25},
]

pessoas.sort(key=lambda x: x["idade"], reverse=True)
# key= Parametro para ordenar a sequencia. Neste exemplo ele irá ordenar pela 'idade'.
# reverse=True -> serve para ordenar a sequencia de forma reversa
print(pessoas)
