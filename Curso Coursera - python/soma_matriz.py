'''Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e
devolve uma matriz que represente sua soma caso as matrizes tenham
dimensões iguais. Caso contrário, a função deve devolver False.'''

def dimensoes(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    print("{}x{}".format(n_linhas, n_colunas))
    return n_linhas, n_colunas

def soma_matrizes(m1, m2):
    matriz = []
    lin1, col1 = dimensoes(m1)
    lin2, col2 = dimensoes(m2)
    if lin1 == lin2 and col1 == col2:
        for i in range(lin1):
            coluna = []
            for j in range(col1):
                coluna.append(m1[i][j] + m2[i][j])
            matriz.append(coluna)
        return matriz
    else:
        return False
