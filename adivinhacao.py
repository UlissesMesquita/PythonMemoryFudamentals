numero_secreto = 42
total_tentativas = 3
rodada = 1


while(rodada <= total_tentativas):

    print("Tentativa: {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digete seu número:")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você Acertou!")
    else:
        if (maior):
            print("Você errou! Seu chute foi maior do que o numero secreto!", numero_secreto)
        else:
            print("Você errou! Seu chute foi menor do que o numero secreto! O numero secreto foi: ", numero_secreto)

    print("Fim do Jogo!")

    rodada = rodada + 1