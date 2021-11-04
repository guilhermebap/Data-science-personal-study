from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self._data_de_cadastro = datetime.today()

    def valida_data(self):
        pass

    def __str__(self):
        return self.format()

    def format(self):
        return self._data_de_cadastro.strftime('%Y/%m/%d %H:%M')

    def dia_da_semana(self):
        dias_da_semana = [
            'Segunda-feira', 'Terça-feira', 'Quarta-feira',
            'Quinta-feira', 'Sexta-feira', 'Sábado',
            'Domingo'
        ]
        return dias_da_semana[self._data_de_cadastro.weekday() - 1]

    def mes_do_ano(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        return meses_do_ano[self._data_de_cadastro.month]

    def tempo_cadastro(self):
        diferenca = (datetime.today() + timedelta(days=3)) - self._data_de_cadastro
        return diferenca

