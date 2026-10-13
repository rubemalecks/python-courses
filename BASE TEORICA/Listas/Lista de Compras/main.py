import os

os.system('cls')
lista = []
while True:
    op = input('Selecione uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Listar itens\n4 - Sair\nOpção: ')
    if op not in ['1', '2', '3', '4']:
        print('Opção inválida. Tente novamente.')
        continue
    
    else:
        os.system('cls')
        if op == '1':
            item = input('Item: ')
            lista.append(item)
            os.system('cls')
        elif op == '2':
            print('Lista de itens: ')
            for i, item in enumerate(lista):
                print(f'{i} - {item}')
            if len(lista) == 0:
                print('Lista vazia. Não há itens para remover.')
                continue
            else:
                while True:
                    indiceRmv = input('Digite o índice do item que deseja remover: ')
                    if indiceRmv.isdigit() and int(indiceRmv) < len(lista):
                        lista.pop(int(indiceRmv))
                        os.system('cls')
                        break
                    else:
                        print('Índice inválido. Tente novamente.')
                        continue
        elif op == '3':
            print('Lista de itens:')
            for i, item in enumerate(lista):
                print(f'{i} - {item}')
            input('Pressione Enter para continuar...')
            os.system('cls')
        elif op == '4':
            print('Saindo do programa...')
            break
