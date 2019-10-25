'''
Implemente a função ordena(lista), que recebe uma lista com números inteiros
como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o
algoritmo selection sort.
'''

def ordena(lista):
    for i in range(len(lista)):
        menor_elemento = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor_elemento]:
                menor_elemento = j
        lista[i], lista[menor_elemento] = lista[menor_elemento], lista[i]
    return lista
