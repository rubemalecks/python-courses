def master(salud):   
    print(salud)
    def decorador(func):
        def interna(s):
            return func(s)
        return interna
    return decorador

@master('ohayo')
def saudacao(saud):
    return saud


print(saudacao("Rubem"))
