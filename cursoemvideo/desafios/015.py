km = float(input("Quantos km o carro rodou: "))
dias = int(input("Quantos dias o carro foi alugado: "))
precodia = 60
precokm = 0.15

total = precodia * dias + precokm * km

print("O total a ser pago é de R${}".format(total))