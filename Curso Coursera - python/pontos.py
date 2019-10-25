import math as m

x1 = int(input("Digite o primeiro número: "))
y1 = int(input("Digite o segundo número: "))
x2 = int(input("Digite o terceiro número: "))
y2 = int(input("Digite o quarto número: "))

D = m.sqrt(m.pow(x2-x1, 2) + m.pow(y2-y1, 2))
if D >= 10:
    print("longe")
else:
    print("perto")
