distancia = float(input("Informe a distância até o destino: "))

if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45
print("O custo da viagem será de R${:.2f}".format(custo))

#Operador ternario
#preço = distancia * 0.50 if distancia <= 200 else distancia*0.45