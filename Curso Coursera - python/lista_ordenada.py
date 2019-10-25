'''
Escreva a função ordenada(lista), que recebe uma lista com números inteiros
como parâmetro e devolve o booleano True se a lista estiver ordenada e False
se a lista não estiver ordenada.
'''

def ordenada(lista):
    for i in range(len(lista)):
        menor_elemento = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor_elemento]:
                return False
    return True
