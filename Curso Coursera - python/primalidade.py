n = int(input("Digite um número inteiro: "))

divisores = 0
divisor = 1
while (divisores <= 2 and divisor <= n):
    if n % divisor == 0:
        divisores+= 1
    divisor += 1

if (divisores == 2):
    print("primo")
else:
    print("não primo")
