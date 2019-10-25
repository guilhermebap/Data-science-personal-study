largura = int(input("Digite a largura do retângulo: "))
h = int(input("Digite a altura do retângulo: "))

while  h > 0:
    l = largura
    while l > 0:
        print("#", end="")
        l -= 1
    print()
    h -= 1
