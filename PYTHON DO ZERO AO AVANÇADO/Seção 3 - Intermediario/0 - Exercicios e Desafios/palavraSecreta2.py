
palavraSecreta = "teste"
chances = 5
letrasAcertadas = ''
while True:
    letraInput = input("\nDigite uma letra: ").lower()

    if letraInput in palavraSecreta:
        letrasAcertadas += letraInput
    else:
        chances -= 1

    palavraFormada = ''
    for letra in palavraSecreta:
        if letra in letrasAcertadas:
            palavraFormada += letra
        else:
            palavraFormada += '*'
    print(f"\nPalavra formada: {palavraFormada}")
    print(f"Chances restantes: {chances}")
    if palavraFormada == palavraSecreta:
        print(f"\nParabéns! Você acertou a palavra secreta: {palavraSecreta}")
        break
    if chances == 0:
        print(f"\nVocê perdeu! A palavra secreta era: {palavraSecreta}")
        break