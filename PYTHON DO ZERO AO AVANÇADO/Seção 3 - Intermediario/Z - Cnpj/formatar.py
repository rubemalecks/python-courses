def format_cnpj(cnpj):
    cnpj.insert(2, ".")
    cnpj.insert(6, ".")
    cnpj.insert(10, "/")
    cnpj.insert(-2, "-")
    formatado = []
    for item in cnpj:
        formatado.append(str(item))
    return "".join(formatado)
