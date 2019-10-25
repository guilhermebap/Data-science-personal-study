"""Duas matrizes são multiplicáveis se o número de colunas da primeira é igual
ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2)
que recebe duas matrizes como parâmetro e devolve True se as matrizes forem
multiplicavéis (na ordem dada) e False caso contrário."""

def dimensoes(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    return n_linhas, n_colunas

def sao_multiplicaveis(m1, m2):
    lin1, col1 = dimensoes(m1)
    lin2, col2 = dimensoes(m2)
    if col1 == lin2:
        return True
    else:
        return False
