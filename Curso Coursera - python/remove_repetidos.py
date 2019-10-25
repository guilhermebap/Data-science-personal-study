def remove_repetidos(lista):
    nova_lista = list(set(lista))
    nova_lista.sort()
    return  nova_lista
