from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor_do_lance):
        if valor_do_lance <= self.__carteira:
            lance = Lance(self, valor_do_lance)
            leilao.propoe(lance)
            self.__carteira -= valor_do_lance
        else:
            raise LanceInvalido('Valor do lance é maior que o valor na carteira')


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self._menor_lance = 0
        self._maior_lance = 0

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance):
        if self._lance_eh_valido(lance):
            if not bool(self._tem_lances()):
                self._menor_lance = lance.valor

            self._maior_lance = lance.valor

            self.__lances.append(lance)

    def __str__(self):
        return f'O maior lance é R${self._maior_lance} e o menor lance é de R${self._menor_lance}'

    @property
    def menor_lance(self):
        return self._menor_lance

    @property
    def maior_lance(self):
        return self._maior_lance

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido('O usuário não pode dar dois lances seguidos')

    def _valor_do_lance_eh_maior_que_o_anterior(self, lance):
        if self.__lances[-1].valor < lance.valor:
            return True
        else:
            raise LanceInvalido('O valor do lance é menor que o último lance do leilão')

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance)
                                          and (self._valor_do_lance_eh_maior_que_o_anterior(lance)))




