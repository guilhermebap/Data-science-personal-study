lado1 = float(input("Informe o lado 1 do triângulo: "))
lado2 = float(input("Informe o lado 2 do triângulo: "))
lado3 = float(input("Informe o lado 3 do triângulo: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("É possível formar um triângulo com as medidas dadas!")
else:
    print("Não é possível formar um triângulo.")