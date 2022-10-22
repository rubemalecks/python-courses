
def criar(nome_arq, alert=True):
    try:
        a = open(nome_arq, 'wt+')
        a.close()
    except Exception as erro:
        print('Houve um ERRO na criação do arquivo!')
        print(erro)
    else:
        if alert == True:
            print(f'FAVOR, PREENCHA OS DADOS NO ARQUIVO {nome_arq}')

def gravar(arq, escrita):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Erro a leitura, {erro}')
    else:
        for cnpj in escrita:
            a.write(f'{cnpj}\n')