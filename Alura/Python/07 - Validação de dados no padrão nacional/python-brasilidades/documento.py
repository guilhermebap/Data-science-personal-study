import validate_docbr


class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('A quantidade de digitos é inválidos!')


class DocCpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.eh_valido(documento):
            self._cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def eh_valido(self, cpf):
        if len(cpf) != 11:
            return False
        else:
            validador = validate_docbr.CPF()
            return validador.validate(cpf)

    def __str__(self):
        return self.format()

    def format(self):
        return f'{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}'


class DocCnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.eh_valido(documento):
            self._cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def eh_valido(self, documento):
        if len(documento) != 14:
            return False
        else:
            validador = validate_docbr.CNPJ()
            return validador.validate(documento)

    def __str__(self):
        return self.format()

    def format(self):
        return f'{self._cnpj[:2]}.{self._cnpj[2:5]}.{self._cnpj[5:8]}/0001-{self._cnpj[-2:]}'

