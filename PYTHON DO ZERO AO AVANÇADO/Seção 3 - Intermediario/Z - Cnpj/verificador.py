def calc_dig(cnpj):
    result_sum_list = []
    if len(cnpj) == 12:
        conciliador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    else:
        conciliador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i, num in enumerate(cnpj):
        result_sum_list.append(cnpj[i] * conciliador[i])
    soma = sum(result_sum_list)
    r = 11 - (soma % 11)
    if r >= 10:
        r = 0
    return r
