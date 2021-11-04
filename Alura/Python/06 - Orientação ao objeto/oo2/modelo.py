class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def ano(self):
        return self._ano

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self._ano} \nLikes: {self._likes}\n'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self._ano} \nDuração do filme: {self._duracao} \nLikes: {self._likes}\n'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporada(self):
        return self._temporadas

    def __str__(self):
        return f'Nome: {self._nome} \nAno: {self._ano} \nNúmero de temporadas: {self._temporadas} \nLikes: {self._likes}\n'


class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
DoctorWho = Serie('Doctor who - temporada x', 2020, 50)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
DoctorWho.dar_like()

series_e_filmes = [vingadores, DoctorWho, tmep, demolidor]
minha_playlist = Playlist('Fim de semana', series_e_filmes)

for programa in minha_playlist:
    print(programa)

print(f'O tamanho da minha playlist é: {len(minha_playlist)}')