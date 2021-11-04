import requests


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self._cep = cep
        else:
            raise ValueError('CEP inválido!')
    
    def cep_eh_valido(self, cep):
        if len(cep) != 8:
            return False
        else:
            return True

    def __str__(self):
        return self.format()

    def format(self):
        return f'{self._cep[:5]}-{self._cep[5:]}'

    def acessar_cep(self):
        url = 'https://viacep.com.br/ws/' + self._cep + '/json/'
        r = requests.get(url)
        return (
            r.json()['bairro'],
            r.json()['localidade'],
            r.json()['uf'])


