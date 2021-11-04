from unittest import TestCase
from src.leilao.dominio import Leilao, Usuario, Lance
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self) -> None:
        self.gui = Usuario('Gui', 500)

        self.lance_gui = Lance(self.gui, 100.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500)

        lance_yuri = Lance(yuri, 150.0)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)

        menor_valor_esperado = 100
        maior_valor_esparado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esparado, self.leilao.maior_lance)

    def test_nao_deve_permitir_fazer_um_lance_menor_ou_igual_ao_ultimo_Lance(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500)
            lance_yuri = Lance(yuri, 50)

            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_menor_e_o_maior_lance_quando_o_leiao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_gui)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(100, self.leilao.maior_lance)

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri', 500)
        vini = Usuario('Vini', 500)

        lance_yuri = Lance(yuri, 150.0)
        lance_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(lance_vini)

        menor_valor_esperado = 100
        maior_valor_esparado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esparado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_gui)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500)

        lance_yuri = Lance(yuri, 200)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_lance_seja_do_mesmo_usuario(self):
        with self.assertRaises(LanceInvalido):
            lance_gui200 = Lance(self.gui, 200)

            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui200)


