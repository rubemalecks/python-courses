"""salarioinicial = float(input('informe o salario inicial: '))
salarioreajustado = float(input('informe o salario reajustado: '))

salarioinicial(salarioreajustado*20/100)+ salarioreajustado

print('o salario reajustado: ', salarioreajustado)"""


dia1 = int(input("Dia: "))
mes1 = int(input("Mês: "))
ano1 = int(input("Ano: "))

print("=" * 13)

dia2 = int(input("Dia: "))
mes2 = int(input("Mês: "))
ano2 = int(input("Ano: "))

print("=" * 13)
print('data + recente: ', end='')
if ano1 > ano2:
    print(f"DIA {dia1} DO {mes1:02d} DE {ano1}")
else:
    print(f"DIA {dia2} DO {mes2:02d} DE {ano2}")
