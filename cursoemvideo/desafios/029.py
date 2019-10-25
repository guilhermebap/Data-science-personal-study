velocidade = float(input("Informe a velocidade do seu carro: "))

limite = 80

if velocidade <= limite:
    print("Velocidade permitida!")
else:
    multa = 7 * (velocidade - limite)
    print("Velocidade acima da velocidade de {} permitido!".format(limite))
    print("Multa no valor de R${:.2f}".format(multa))