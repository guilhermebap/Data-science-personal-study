'''
Implemente a função encontra_impares(lista), que recebe como parâmetro uma
lista de números inteiros e devolve uma outra lista apenas com os números
ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''

def encontra_impares(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 1:
            return [lista[0]]
        else:
            return []
    else:
        if lista[0] % 2 == 1:
            return [lista[0]] + encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])
