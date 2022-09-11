
# ARQUIVO EXISTE ?

def arqExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# LER ARQUIVO

def ler(arq):
    dados = set()
    try:
        a = open(arq, 'rt')
    except Exception as erro:
        print('Erro ao ler o arquivo!')
        print(erro)
    else:
        for cnpj in a:
            cnpj = cnpj.replace('\n', '').strip()
            if len(cnpj) > 0:
                dados.add(cnpj)  
        return dados