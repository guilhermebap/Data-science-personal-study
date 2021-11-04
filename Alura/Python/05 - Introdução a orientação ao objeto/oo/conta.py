class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor depositado deve ser positivo')

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_disponivel_a_sacar >= valor

    def sacar(self, valor):
        if valor > 0:
            if self.__pode_sacar(valor):
                self.__saldo -= valor
            else:
                print(f'O valor {valor} passou o limite')
        else:
            print('O valor sacado deve ser positivo')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

# Para chamar um metodo estático devemos digitar Conta.codigo_banco
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


