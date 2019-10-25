'''
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros
correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe
parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.
'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if (self.a)**2 == (self.b)**2 + (self.c)**2:
            return True
        elif (self.b)**2 == (self.a)**2 + (self.c)**2:
            return True
        elif (self.c)**2 == (self.a)**2 + (self.b)**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        ta = [self.a, self.b, self.c]
        tb = [triangulo.a, triangulo.b, triangulo.c]
        ta.sort()
        tb.sort()
        if ta[0] % tb[0] == 0 and ta[1] % tb[1] == 0 and ta[2] % tb[2] == 0:
            return True
        elif tb[0] % ta[0] == 0 and tb[1] % ta[1] == 0 and tb[2] % ta[2] == 0:
            return True
        else:
            return False



t1 = Triangulo(5, 4, 3)
t2 = Triangulo(5, 4, 3)
print(t1.semelhantes(t2))
