def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if n == m:
        return n
    elif resto == 0 or resto > m:
        return m
    else:
        return resto

def usuario_escolhe_jogada(n, m):
    pecas = 0
    while pecas < 1 or pecas > m or pecas > n:
        pecas = int(input("Digite o número de peças a serem retirados: "))
        if pecas < 1 or pecas > m:
            print("Jogada invalida, tente novamente.")
    return pecas


def menu ():
    user = 0
    comp = 0
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato")
    escolha = int(input(""))
    if escolha == 1:
        print("Você escolheu uma partida isolada")
        print("-=" * 40)
        print("\t\t\t\t  JOGO NIM")
        print("-=" *40)
        partida()
    elif escolha == 2:
        print("Voce escolheu um campeonato!\n")
        print("\n**********Rodada 1************")
        result = partida()
        if result == "user":
            user += 1
        elif result == "comp":
            comp += 1
        print("Placar: Você {} X {} Computador".format(user, comp))
        print("\n**********Rodada 2************")
        result = partida()
        if result == "user":
            user += 1
        elif result == "comp":
            comp += 1
        print("Placar: Você {} X {} Computador".format(user, comp))
        print("\n**********Rodada 3************")
        result = partida()
        if result == "user":
            user += 1
        elif result == "comp":
            comp += 1
        print("Placar: Você {} X {} Computador".format(user, comp))

def partida():
    n = int(input("Digite o número de peças do jogo: "))
    m = int(input("Digite o número de peças máximos que é possível retirar em uma rodada: "))
    nInicial = n
    pecas = 0
    print("\n")
    if nInicial % (m + 1) == 0:
        print("Você começa!\n")
        while n > 0:
            pecas1 = usuario_escolhe_jogada(n, m)
            print("\nVocê tirou {} peças".format(pecas1))
            n -= pecas1
            print("Restam {} peças\n".format(n))
            if n <= 0:
                print("Você ganhou!")
                return "user"
            pecas2 = computador_escolhe_jogada(n, m)
            print("\nO computador tirou tirou {} peças".format(pecas2))
            n -= pecas2
            print("Restam {} peças".format(n))
            if n <= 0:
                print("O computador ganhou!")
                return "comp"
            pecas = pecas1 + pecas2
    else:
        print("Computador começa!\n")
        while n > 0:
            pecas1 = computador_escolhe_jogada(n, m)
            print("\nO computador tirou {} peças".format(pecas1))
            n -= pecas1
            print("Restam {} peças".format(n))
            if n <= 0:
                print("O computador ganhou!")
                return "comp"
            pecas2 = usuario_escolhe_jogada(n, m)
            print("\nVocê tirou {} peças".format(pecas2))
            n -= pecas2
            print("Restam {} peças\n".format(n))
            if n <= 0:
                print("Você ganhou!")
                return "user"
        pecas = pecas1 + pecas2

menu()
