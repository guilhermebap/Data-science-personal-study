"""Como proposto na primeira vídeo-aula da semana, escreva uma função
imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime
a matriz, linha por linha. Note que NÃO se deve imprimir espaços após o
último elemento de cada linha!


Dica: lembre da primeira parte do curso, na semana 7! A função "print"
em geral adiciona uma quebra de linha ao final, mas você pode controlar
isso usando o argumento opcional "end"dessa forma:"""

def dimensoes(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    return n_linhas, n_colunas

def imprime_matriz(m):
    lin, col = dimensoes(m)
    for i in range(lin):
        for j in range(col):
            if j+1 < col:
                print(m[i][j], end=" ")
            else:
                print(m[i][j])
