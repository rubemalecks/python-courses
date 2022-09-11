'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            x = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;30;41mERRO - Por favor digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não digitar.')
            return 0
        else:
            return x
            

def leiaFloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;30;41mERRO - Por favor digite um número Real válido.\033[m')
        except (KeyboardInterrupt):
            print('O usuário não informou nada')
            return 0
        else:            
            return x            

print('-'*42)
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print('-'*42)

print(f'O número inteiro digitado foi {n1}\nO número real digitado {n2}')
