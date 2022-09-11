from typing import List
from layout.menu import menu, separador, opcao
from arquivos.read import arqExiste, ler
from arquivos.write import criarArq, gravar, separador
from time import sleep


# VERIFICAR EXISTENCIA DE ARQUIVO DE CONSULTA
if arqExiste('clientes_rede.txt'):      # RELATÓRIO DA REDE
    rede = ler('clientes_rede.txt')
    print(rede)
else:
    criarArq('clientes_rede.txt')

if arqExiste('rei_clientes.txt'):       # RELATÓRIO INTERNO
    rede_cadastrada = ler('rei_clientes.txt')
    print(rede_cadastrada)
else:
    criarArq('rei_clientes.txt')

if arqExiste('todos_clientes.txt'):     # (TODOS OS CLIENTES)
    all_clientes = ler('todos_clientes.txt')
else:
    criarArq('todos_clientes.txt')
# ----------------------------------------------------------

separador()
op = menu(f'1 -> Clientes p/ adicionar na Rede\n2 -> Clientes p/ Remover da Rede\n3 -> Verificar se é Cliente\nR: ')

if op == 0:
    print('saindo...')
    sleep(3)

# CLIENTES PARA ADICIONAR A REDE
elif op == 1:
    add_rede = rede - rede_cadastrada
    not_add_rede = sorted(list(add_rede - all_clientes))
    add_rede = (add_rede & all_clientes)
    add_rede = sorted(list(add_rede))
    if len(add_rede) == 0:
        print('NÃO HÁ CLIENTES P/ ADICIONAR NA REDE')
        print('NÃO É NOSSO CLIENTE:', not_add_rede)
    else:
        gravar('add_rede.txt', add_rede)


# REMOVER DA REDE INTERNA
elif op == 2:
    rmv_rede = sorted(list(rede_cadastrada - rede))
    if len(rmv_rede) == 0:
        print('NÃO HÁ CLIENTE P/ REMOVER...')
    else:
        gravar('rmv_rede.txt', rmv_rede)
        print('REMOVER DA REDE INTERNA: ')
        for cnpj in rmv_rede:
            print(cnpj)
