'''Escreva a função conta_letras(frase, contar="vogais"), que recebe como
primeiro parâmetro uma string contendo uma frase e como segundo parâmetro
uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o
numero de vogais presentes na frase. Quando ele for definido como "consoantes",
a função deve devolver o número de consoantes presentes na frase. Se este
parâmetro não for passado para a função, deve-se assumir o valor "vogais" para
o parâmetro.'''

def conta_letras(frase, contar="vogais"):
    frase = frase.lower().split()
    frase_sem_espaco = ""
    contagem = 0
    for palavra in frase:
        frase_sem_espaco += palavra
    for letra in frase_sem_espaco:
        if letra =="a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":
            contagem += 1
    if contar == "vogais":
        return contagem
    elif contar == "consoantes":
        return len(frase_sem_espaco) - contagem
