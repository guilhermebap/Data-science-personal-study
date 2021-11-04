from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido
import pytest



@pytest.fixture
def gui():
    return Usuario('Gui', 100)


@pytest.fixture()
def leilao():
    return Leilao('celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(gui, leilao):
    gui.propoe_lance(leilao, 50)

    assert gui.carteira == 50


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_na_carteira_do_usuario(gui, leilao):
    gui.propoe_lance(leilao, 1.0)

    assert gui.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_o_valor_na_carteira_do_usuario(gui, leilao):
    gui.propoe_lance(leilao, 100)

    assert gui.carteira == 0


def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_na_carteira_do_usuario(gui, leilao):
    with pytest.raises(LanceInvalido):
        gui.propoe_lance(leilao, 150)
