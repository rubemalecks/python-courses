nome = str(input('Digite seu nome completo: ').strip())
print('Analisando nome ...')
print('Em maiusculo: ', nome.upper())
print('Em minusculo: ', nome.lower())
print('Letras ao todo: ', len(nome) - nome.count(' '))
nome1 = nome.split()
print('Letras no primeiro nome:', len(nome1[0]))
