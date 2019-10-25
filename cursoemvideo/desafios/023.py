n = int(input("Digite um número inteiro entre 0 a 9999: "))
if n < 0 or n >= 9999:
    print("Número inválido")

unidade = n % 10
dezena = (n // 10) % 10
centena = (n //100) % 10
milhar = n //1000

print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))