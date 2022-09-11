"""def minha_funcao():
    print("olá, estou na minha função!")

def funcao_superior(funcao):
    print('olá mundo')
    funcao()


funcao_superior(minha_funcao)
"""


def decorator(funcao):
    def funcao_superior():
        print("olá mundo")
        funcao()

    return funcao_superior


@decorator
def minha_funcao():
    print("olá, estou na minha função!")


# minha_funcao()


def validar(func):
    return func


@validar
def soma(a, b):
    return a + b


print(soma(1, 2))
