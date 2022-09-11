def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
        # mensagem que será mostrada indicando o erro
    return n1 / n2


# print(divide(2, 0))

try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print("log:", error)


"""
# OUTRO EXEMPLO:

def teste():
    try:
        n = int(input('Digite um numero entre 1 e 7: '))
        if n < 1 or n > 7:
            raise ValueError
        else:
            print('Obrigado!!')
    except ValueError:
        print('entrada inválida')

teste()
"""
