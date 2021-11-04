from documento import Documento
from telefones_br import TelefoneBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cpf = 12354367996
objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)
print()
cnpj = 34201366000140
objeto_cnpj = Documento.cria_documento(cnpj)
print(objeto_cnpj)
print()
telefone = '553132450820'
objeto_telefone = TelefoneBr(telefone)
print(objeto_telefone)

print()

objeto_data = DatasBr()
print(objeto_data)
print(objeto_data.dia_da_semana())
print(objeto_data.mes_do_ano())
print(objeto_data.tempo_cadastro())

print()
cep = 30380410
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade, estado = objeto_cep.acessar_cep()
print(f'{bairro}, {cidade}/{estado}')