def converte_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:
    numero = converte_num(input("Digite um numero: "))
    if numero is not None:
        print(numero * 5)
    else:
        print('isso não é um número.')
