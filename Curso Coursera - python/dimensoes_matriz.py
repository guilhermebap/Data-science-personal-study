'''Escreva uma função dimensoes(matriz) que recebe uma matriz
como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.'''

def dimensoes(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    print("{}x{}".format(n_linhas, n_colunas))
