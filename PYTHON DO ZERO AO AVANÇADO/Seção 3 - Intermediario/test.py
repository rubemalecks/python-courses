"""
def decorador(func):
    def wrapper():
        print("decorada")
        func()

    return wrapper


# if __name__ == "__main__":


@decorador
def minha_funcao():
    print("minha função")


minha_funcao()
"""

result_sum_list = []
cnpj = [0, 9, 1, 6, 5, 0, 2, 8, 0, 0, 0, 1]
conciliador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
for i, num in enumerate(cnpj):
    result_sum_list.append(cnpj[i] * conciliador[i])
print(result_sum_list)
print(sum(result_sum_list))