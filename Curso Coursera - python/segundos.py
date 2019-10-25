inputSegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = inputSegundos // (3600 * 24)
inputSegundos = inputSegundos - (dias * 3600 * 24) # segundos restando

horas = inputSegundos // (3600)
inputSegundos = inputSegundos - (horas * 3600) # segundos restando

minutos = inputSegundos // 60
inputSegundos = inputSegundos - (minutos * 60)  # segundos restando

segundos = inputSegundos # segundos restando

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))
