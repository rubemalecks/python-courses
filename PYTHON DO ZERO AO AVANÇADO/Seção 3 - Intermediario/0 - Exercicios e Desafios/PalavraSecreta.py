palavraSecreta = "python"

palavraOcultada = list(palavraSecreta)
palavraOcultadaL = list("*"*len(palavraOcultada))

chances = 4
while True:
    print("*"*42)
    print("Palavra Ocultada: ", "".join(palavraOcultadaL))
    print("Chances restantes: ", chances)
    while True:
        print("*"*42)

        inputUsuario = input("Digite uma letra: ")
        if (len(inputUsuario) != 1) or (type(inputUsuario) != str):
            print("Digite apenas uma letra!")
            continue
        break
    print (type(inputUsuario))

    posicao = palavraOcultada.index(inputUsuario) if inputUsuario in palavraOcultada else -1
    if (posicao>= 0):
        palavraOcultadaL[posicao] = palavraOcultada[posicao] = inputUsuario
    else:
        print("Letra não encontrada")
        chances -= 1
    if chances == 0:
        print("Você perdeu!")
        break
    if "*" not in palavraOcultadaL:
        print("Você ganhou!")
        break