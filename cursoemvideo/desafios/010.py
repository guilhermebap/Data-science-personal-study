reais = float(input("Digite quantos reais você possui: "))

cotacaoDolar = 3.27

print("R${:0.2f} = US${:0.2f}".format(reais, reais / cotacaoDolar))