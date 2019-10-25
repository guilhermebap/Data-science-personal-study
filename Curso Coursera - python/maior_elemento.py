def maior_elemento(lista):
    maior = None
    for i in lista:
        if maior is None or maior < i:
            maior = i
    return maior

lista = [1, 3, 1, 5, 6, 10, 5, 12, 20, 2, 3]
print(maior_elemento(lista))
