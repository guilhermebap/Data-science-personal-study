import re

class TelefoneBr:
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_telefone(telefone):
            self._telefone = telefone
        else:
            raise ValueError('Número inválido')

    def valida_telefone(self, telefone):
        padrao = re.compile(r'([\d]{2,3})?(\d{2})(\d{4,5})(\d{4})')
        if padrao.match(telefone):
            return True
        else:
            return False

    def __str__(self):
        return self.format()

    def format(self):
        padrao = re.compile(r'([\d]{2,3})?(\d{2})(\d{4,5})(\d{4})')
        resposta = padrao.search(self._telefone)
        if resposta.group(1):
            return f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
        else:
            return f'({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
