def decorador(argumentos_decorador):
    print(argumentos_decorador, end=", ")
    """
    PARAMETROS DO DECORADOR
    """

    def decorador_real(func):
        """
        RECEBER FUNÇÃO
        """

        def executed_function(argumentos_funcao):
            """
            EXECUTAR A FUNÇÃO
            """
            print(argumentos_funcao)

        return executed_function

    return decorador_real


@decorador("ohayo")
def name(nome):
    return nome


name("poko")


# ------------------------------------------------
# OUTRO EXEMPLO


def revisar(f):
    def func_interna(a, b):
        if b == 0:
            raise ZeroDivisionError("Não pode dividir Zero")
        return f(a, b)

    return func_interna


@revisar
def divisao(a, b):
    return a / b


print(divisao(7, 2))
