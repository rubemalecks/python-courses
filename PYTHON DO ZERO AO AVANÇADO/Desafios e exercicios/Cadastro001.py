#   Exercício Python 094 - Unindo dicionários e listas
#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários
#   em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas
#       B) A média de idade
#       C) Uma lista com as mulheres
#       D) Uma lista de pessoas com idade acima da média

cadastro = list()
pessoas = dict()
mulheres = list()

while True:
    nome = str(input("Nome: ")).upper()
    sexo = str(input("Sexo[F/M]: ")).upper()
    idade = int(input("Idade: "))
    pessoas.update({nome: {'sexo': sexo, 'idade': idade}})
    cadastro.append(pessoas.copy())
    pessoas.clear()


    continuar = str(input("Continuar[S/N]: ")).upper()
    if continuar[0] !=  "S":
        break

valores_idade = [
    [dado[1]["idade"] for dado in pessoas.items()] for pessoas in cadastro
]


valores_idade = [item for sublista in valores_idade for item in sublista]

media = (sum(valores_idade)) / len(valores_idade)
print(media)
