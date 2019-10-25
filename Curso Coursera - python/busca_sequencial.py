'''
Implemente a função busca(lista, elemento), que busca um determinado elemento
em uma lista e devolve o índice correspondente à posição do elemento encontrado.
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado
não existir na lista, a função deve devolver o booleano False.
'''

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
