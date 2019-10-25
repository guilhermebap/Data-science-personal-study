import math as m

h = float(input("Digite a altura da parede: "))
w = float(input("Digite a largura da parede: "))

area = h * w
areaTinta = 2

print("Para pintar uma parede de {:0.2f} m^2 é necessário {} litros de tinta".format(area, m.ceil(area/areaTinta)))