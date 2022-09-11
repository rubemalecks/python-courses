from convert import cnpj_list, remover_caracteres
from formatar import format_cnpj
from gerador import gera_cnpj
from verificador import calc_dig

while True:
    op = input("[0] ->  Gerar Cnpj \n[1] ->  Validar Cnpj\nR: ")
    print("--" * 13)
    if op == "0":
        cnpj = gera_cnpj()
        cnpj = format_cnpj(cnpj)
        print(cnpj)
        break
    elif op == "1":
        # REMOVER CARACTERES
        cnpj_input = remover_caracteres(input("Digite o cnpj: "))
        print("--" * 13)

        # CONVERTER P/ LISTA |  REMOVER DÍGITOS P/ DEPOIS VERIFICAR

        cnpj_inicial = cnpj_list(cnpj_input)
        cnpj = cnpj_input[:-2]

        # CONVERTER STR EM LIST
        cnpj = cnpj_list(cnpj)

        # VERIFICANDO O 1º DÍGITO
        dig1 = calc_dig(cnpj)
        cnpj.append(dig1)

        # VERIFICANDO O 2º DÍGITO
        dig2 = calc_dig(cnpj)
        cnpj.append(dig2)

        # REFORMATANDO
        cnpj = format_cnpj(cnpj)
        cnpj_inicial = format_cnpj(cnpj_inicial)

        # VERIFICANDO SE É VÁLIDO
        sequencia = cnpj[0] * len(remover_caracteres(cnpj))

        if sequencia == remover_caracteres(cnpj):
            print(f"{cnpj} - CNPJ INVÁLIDO !!")

        elif cnpj_inicial == cnpj:
            print(f"{cnpj} - CNPJ VÁLIDO !!")
        else:
            print(f"{cnpj} - CNPJ INVÁLIDO !!")
        break
    else:

        print("Digite uma opção válida!")
        print("--" * 13)
