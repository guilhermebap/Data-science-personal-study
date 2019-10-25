'''Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista)
que recebe uma lista de strings como parâmetro e devolve o primeiro string na
ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.'''

def primeiro_lex(lista):
    menor = None
    for nome in lista:
        if menor == None:
            menor = nome
        elif menor > nome:
            menor = nome

    return menor

def testa_menor_string():
    lista1 = ["Ana", "José", "Maria", "Valdemar"]
    print(menor_string(lista1))
    assert menor_string(lista1) == "ana"
