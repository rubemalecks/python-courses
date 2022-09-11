# O For comumente transforma nossas listas em iteradores

# Com o FOR

lista = [0, 1, 2, 3, 4, 5]

# >>> (hasattr(lista, '__next__')) --> False: a lista NÃO é um iterador
# >>> (hasattr(lista, '__iter__')) --> True: a lista é SIM um iterável

for num in lista:  # Sendo iterável podemos usar o 'for'
    print(num)  # O 'for' vai transformar 'lista' em um iterador
print("-" * 23)

# Sem o FOR, ainda podemos fazer assim:

iterador = iter(lista)  # iter é um objeto iterador que retorna um iterável

# Agora a cada iteração vai ser retornado um único valor
print(next(iterador))  # 0
print(next(iterador))  # 1
print(next(iterador))  # 2 e continuar ...


# Outro exemplo continuando a mesma sequencia.
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
