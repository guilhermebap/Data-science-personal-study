import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
     i = 1
     textos = []
     texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
     while texto:
         textos.append(texto)
         i += 1
         texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

     return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma
    lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e
    deve devolver o grau de similaridade nas assinaturas.'''
    sab = ((as_a[0] - as_b[0])
    + (as_a[1] - as_b[1])
    + (as_a[2] - as_b[2])
    + (as_a[3] - as_b[3])
    + (as_a[4] - as_b[4])
    + (as_a[5] - as_b[5]))

    return abs(sab / 6)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
    assinatura do texto.'''
    palavras = separa_palavras_total(texto)
    setencas = separa_sentencas(texto)
    soma_caracteres = numero_caracteres_total(palavras)
    soma_frases = n_frases_total(texto)

    media = soma_caracteres / len(palavras)
    type_token = n_palavras_diferentes(palavras) / len(palavras)
    razao_hapax_legomana = n_palavras_unicas(palavras) / len(palavras)
    tamanho_medio_setenca = calcula_tamanho_medio_setenca(texto)
    complexidade_setenca = soma_frases / len(setencas)
    tamanho_medio_frase = calcula_medio_frase(texto)

    return (media, type_token, razao_hapax_legomana, tamanho_medio_setenca,
    complexidade_setenca, tamanho_medio_frase)


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve
    devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''
    #aval = list()
    prob = list()
    i = 0
    while i < len(textos):
        aval = calcula_assinatura(textos[i])
        prob.append(compara_assinatura(ass_cp, aval))
        i += 1

    probabilidade = None
    texto = 0
    for index, i in enumerate(prob):
        if probabilidade == None or i < probabilidade:
            probabilidade = i
            texto = index

    return index



def separa_palavras_total(texto):
    '''Recebe um texto e retorna o número total de palavras'''
    setencas = separa_sentencas(texto)
    i = 0
    frases = list()
    while i < len(setencas):
        frases += separa_frases(setencas[i])
        i += 1
    i = 0
    palavras = list()
    while i < len(frases):
        palavras += separa_palavras(frases[i])
        i += 1
    return palavras

def numero_caracteres_total(palavras):
    '''Recebe uma lista de palavras e retorna a soma dos caracteres.'''
    i = 0
    soma= 0
    while i < len(palavras):
        soma += len(palavras[i])
        i += 1
    return soma

def n_frases_total(texto):
    '''Recebe um texto e retorna o número total de frases'''
    setencas = separa_sentencas(texto)
    frases = list()
    i = 0
    while i < len(setencas):
        frases += separa_frases(setencas[i])
        i += 1
    return len(frases)

def calcula_tamanho_medio_setenca(texto):
    soma_caractere = 0
    setencas = separa_sentencas(texto)
    i = 0
    while i < len(setencas):
        soma_caractere += len(setencas[i])
        i += 1
    media = soma_caractere / len(setencas)
    return media

def calcula_medio_frase(texto):
    '''Recebe um texto e retorna a media de caracteres em uma frase pelo
    numero de frases'''
    soma_caracteres = 0
    frases = list()
    i = 0
    sentencas = separa_sentencas(texto)
    while i < len(sentencas):
        frases += separa_frases(sentencas[i])
        i += 1
    i = 0
    while i < len(frases):
        soma_caracteres += len(frases[i])
        i += 1
    media = soma_caracteres / len(frases)
    return media

ass_cp = le_assinatura()
textos = le_textos()
prob = avalia_textos(textos, ass_cp)



print("O autor do texto {} está infectado com COH-PIAH".format(texto))
