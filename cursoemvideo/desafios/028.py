import random
from time import sleep
numAleatorio = random.randint(0, 5) #módulo para sortear um inteiro aleatorio entre 0 e 5
print("-=-"*23)
print("Vou escolher um número entre 0 e 5 você consegue advinhar qual é?")
print("-=-"*23)

n = int(input("Digite um número inteiro: "))
print("Processando... ")
sleep(2) #Import da biblioteca sleep, faz o computador simular que ele está pensando se você acertou ou não,

if n == numAleatorio:
    print("Parabéns, você acertou!")
else:
    print("Errou o número era {}!".format(numAleatorio))