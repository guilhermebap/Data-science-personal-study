def menor_nome(lista_nome):
    nome_mais_curto = None
    lista_nome
    for nome in lista_nome:
        if nome_mais_curto == None:
            nome_mais_curto = nome.strip().capitalize()
        elif len(nome.strip()) < len(nome_mais_curto):
            nome_mais_curto = nome.strip().capitalize()

    return nome_mais_curto
