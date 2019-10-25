numero = input("Digite um número inteiro: ")
tam = len(numero)
numeroInt = int(numero)
if tam >= 3:
    numeroInt = numeroInt % 100
dezenas = numeroInt //10

print("O dígito das dezenas é {}".format(dezenas))
