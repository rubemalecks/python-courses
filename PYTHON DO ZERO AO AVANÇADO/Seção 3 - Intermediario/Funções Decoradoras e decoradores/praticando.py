def externa(id):
    dic = {"pt": "Oi", "en": "hello", "jp": "ohayou"}

    def interna(nome):
        print(f"{dic[id]}, {nome}!!")

    return interna


saudacao = externa("jp")

saudacao('poko')