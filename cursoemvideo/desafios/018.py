import math as m

n = float(input("Digite um ângulo em graus: "))

# Convertendo o angulo de graus para radiano
ang = m.radians(n)

print("-" * 12)
print("Cos({}) = {}".format(n, round(m.cos(ang), 2)))
print("Sen({}) = {}".format(n, round(m.sin(ang), 2)))
print("Tan({}) = {}".format(n, round(m.tan(ang), 2)))