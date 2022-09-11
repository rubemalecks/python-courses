def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            x = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;30;41mERRO - Por favor digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não digitar.')
            return 0
        else:
            return x


def menu(lista):
    cabecalho('MENU PRINCIPAL'.center(42))
    c = 1
    for op in lista:
        print(f'\033[33m{c}\033[m - \033[34m{op}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    print(linha())
    return opc
