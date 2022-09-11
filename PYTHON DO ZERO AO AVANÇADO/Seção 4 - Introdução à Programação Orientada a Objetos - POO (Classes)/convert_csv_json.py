import csv
import json

try:
    arq = open("exemplo2.csv", "rt")
except Exception as erro:
    print(erro)

next(arq)  # ignorar linha 0

cadastro_hogwarts = dict()
for dado in list(arq):
    dado = dado.split(",")
    cadastro_hogwarts[dado[0]] = {"nome": dado[0]}, {"nascimento": dado[1]}, {"casa": dado[2]}

print(cadastro_hogwarts)
