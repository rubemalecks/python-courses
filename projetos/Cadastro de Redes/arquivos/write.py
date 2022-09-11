def separador(sinal='-', qtd=42):
    print(f'{sinal}'*qtd)

def criarArq(novo_arq):
    from time import sleep
    try:
        a = open(novo_arq, 'wt+')
        a.close()
    except Exception as erro:
        print('[ERRO] = ', erro)
    else:
        print('Criando Arquivo', end='...')
        sleep(3)
        print()
        print(f'{novo_arq} - Criado com Sucesso!!\nFavor, Preencher com os dados ESPECÍFICOS!!')
    separador()

def gravar(arq, dados_gravar):
    try:
        a = open(arq, 'w+')
    except Exception as erro:
        print('[erro]', erro)
    else:
        for cnpj in dados_gravar:
            a.write(f'{cnpj}\n')

