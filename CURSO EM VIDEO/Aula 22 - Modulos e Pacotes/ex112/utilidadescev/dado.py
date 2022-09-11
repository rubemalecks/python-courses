

def leiaDinheiro(msg):
    c = ( # CORES
    '\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m',       # 6 - branco
    )

    while True:
        print('-'*42)
        valor = str(input(msg).replace(',','.')).strip()
        print('-'*42)
        
        if valor.isalpha() or valor == '':
            print(f'{c[1]}{valor} é um preço inválido!{c[0]}')
        else:
            return float(valor)
            

