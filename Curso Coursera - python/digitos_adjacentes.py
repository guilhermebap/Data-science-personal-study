n = int(input("Digite um número inteiro: "))

digitosIguais = False

while n != 0 and (not digitosIguais):
    digitoAnterior = n % 10
    n = n // 10
    if (digitoAnterior == (n % 10)):
        digitosIguais = True

if (digitosIguais):
    print("sim")
else:
    print("não")
