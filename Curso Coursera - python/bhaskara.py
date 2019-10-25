import math as m

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = m.pow(b, 2) - 4 * a * c

if delta > 0:
    print("Duas raizes reais")
    x1 = (-b + m.sqrt(delta))/(2*a)
    x2 = (-b - m.sqrt(delta))/(2*a)
    if (x1 > x2):
        aux = x2
        x2 = x1
        x1 = aux
        print("as raízes da equação são {} e {} =".format(round(x1, 2), round(x2, 2)))

elif delta == 0:
    print("Uma raiz real")
    x = -b/(2*a)
    print("a raiz desta equação é", round(x,2))

else:
    print("esta equação não possui raízes reais")
