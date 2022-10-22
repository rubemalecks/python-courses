
def separador(sinal='-', qtd=42):
    print(f'{sinal}'*qtd)

                # MENU DE OPÇÕES
def menu(msg):
    print('ANALIZADOR DE REDES DE CLIENTES'.center(42))
    separador()
    while True:
        try:
           x = int(input(msg).center(42))
        except(ValueError, TypeError):
            print('\033[0;30;41mERRO - Por favor digite uma opção válida!\033[m')
            separador()
            continue
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não digitar.')
            separador()
            return 0
        else:
            separador()
            return x


    # INDICADOR DE OPÇÕES


def opcao(op=0):
    try:
        if op == 0:
            print('O usuário Saiu!')
            separador('.')
        elif op == 1:   # Mostrar Clientes Novos da Rede
            ...
        elif op == 2:   # Mostrar Cliente p/ excluir da Rede
            ...
        elif op == 3:   # Ler Lista da Rede e ver se é nosso Cliente
            ...
    except Exception as erro:
        print(f'Ocorreu um erro ->> {erro}')
        
