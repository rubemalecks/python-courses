from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:# Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2: 
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')  
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
