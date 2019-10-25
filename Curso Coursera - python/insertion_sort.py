'''
Implemente a função insertion_sort(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
insertion sort.
'''

def insertion_sort(lista):

    for i in range(1, len(lista)):
        j = i
        while j > 0:
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
            j-=1
    return lista
