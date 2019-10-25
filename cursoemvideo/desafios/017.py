import math as m

catOp = float(input("Digite o tamanho do cateto oposto: "))
catAd = float(input("Digite o tamanho do cateto adjacente: "))

hipotenusa = m.hypot(catOp, catAd) # mesma coisa que sqrt(x^2 + y^2)
print("A hipotenusa do triângulo retangulo de lado {} e lado {} vale {:.2f}".format(catOp, catAd, hipotenusa))
