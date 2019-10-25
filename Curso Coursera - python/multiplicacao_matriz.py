import imprime_matriz

def cria_matriz(lin, col, valor):
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplica_matriz(m1, m2):
    n_lin1, n_col1 = len(m1), len(m1[0])
    n_lin2, n_col2 = len(m2), len(m2[0])
    assert n_col1 == n_lin2
    matriz = cria_matriz(n_lin1, n_col2, 0)


    for linha in range(n_lin1):
        for coluna in range(n_col2):
            for x in range(n_col1):
                matriz[linha][coluna] += (m1[linha][x] * m2[x][coluna])

    imprime_matriz.imprime_matriz(matriz)
    return matriz

if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[1, 2], [3, 4], [5, 6]]
    multiplica_matriz(m1, m2)
