from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, SemDesconto

class Calculador_de_descontos:

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(SemDesconto()))

        return desconto.calcular(orcamento)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print(f'Desconto calculado: {desconto}')
    # imprime 38.5