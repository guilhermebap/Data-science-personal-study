from dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido

gui = Usuario('Gui', 150)
yuri = Usuario('Yuri', 150)

lance_gui = Lance(gui, 150.0)
lance_yuri = Lance(yuri, 100.0)

leilao = Leilao('Celular')

leilao.propoe(lance_yuri)
leilao.propoe(lance_gui)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance no valor de R$ {lance.valor}')

if True:
    raise LanceInvalido('A')