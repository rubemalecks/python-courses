'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import requests

try:
    r = requests.get('http://pudim.com.br/')
   
except:
    print(f'\033[0;30;41mO site está fora do ar.\033[m')
else:
    print('\033[0;30;42mO site está no ar!!!\033[m')

    