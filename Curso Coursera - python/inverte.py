i = 1
lista = []
while i != 0:
    i = int(input("Digite um número: "))
    lista.append(i)
tam = len(lista)
while tam > 1:
    print(lista[tam-2])
    tam -= 1
