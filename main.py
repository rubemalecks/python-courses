texto = 'Rubem'
iterador = iter(texto) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break