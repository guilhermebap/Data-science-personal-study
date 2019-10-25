largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

h = altura
while  h > 0:
    l = largura
    if h is altura or h is 1:
        while l > 0:
            print("#", end="")
            l -= 1
    while l > 0:
        if l == 1 or l == largura:
            print("#", end="")
        else:
            print(" ", end = "")
        l -= 1
    print()
    h -= 1
