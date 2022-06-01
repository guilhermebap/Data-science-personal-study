USE vendas_sucos;

##############################
# ALTERANDO REGISTROS
##############################

SELECT *
FROM produtos;

UPDATE produtos
SET preco_lista = 5
WHERE CODIGO = '1000889';

UPDATE produtos
SET embalagem = 'PET', tamanho = '1 Litro', descritor = 'Sabor da Montanha - 1 Litro - Uva'
WHERE codigo = '1000889';

UPDATE produtos
SET preco_lista = preco_lista * 1.1
WHERE sabor = 'Maracujá';

SELECT *
FROM clientes;

UPDATE clientes
SET endereco = 'R. Jorge Emílio 23', 
	bairro = 'Santo Amaro', 
    cidade = 'São Paulo', 
    estado = 'SP', 
    CEP = '8833223'
WHERE CPF = 19290992743;

SELECT *
FROM clientes;

SELECT *
FROM vendedores;

SELECT *
FROM sucos_vendas.tabela_de_vendedores;

SELECT *
FROM vendedores AS A
INNER JOIN sucos_vendas.tabela_de_vendedores AS B
ON A.matricula = SUBSTRING(B.matricula, 3);

UPDATE (vendedores AS A
		INNER JOIN sucos_vendas.tabela_de_vendedores AS B
		ON A.matricula = SUBSTRING(B.matricula, 3))
SET A.ferias = B.de_ferias;

SELECT *
FROM clientes;

SELECT *
FROM vendedores;

SELECT *
FROM clientes AS A
INNER JOIN vendedores AS B
ON A.bairro = B.bairro;

UPDATE clientes as A
	INNER JOIN vendedores AS B
	ON A.bairro = B.bairro
SET A.volume_compra = A.volume_compra * 1.3;

SELECT *
FROM clientes;

######################################
# DELETANDO REGISTROS
######################################

SELECT *
FROM produtos;

DELETE FROM produtos 
WHERE CODIGO = '1001000';

DELETE FROM produtos
WHERE tamanho = '1 Litro' AND SUBSTRING(descritor, 1, 15) = 'Sabor dos Alpes';

SELECT *
FROM sucos_vendas.tabela_de_produtos;

DELETE FROM produtos
WHERE codigo NOT IN (SELECT codigo_do_produto 
					 FROM sucos_vendas.tabela_de_produtos);
				
SELECT *
FROM notas;

SELECT *
FROM notas AS A
INNER JOIN clientes AS B
on A.CPF = B.CPF
WHERE B.idade <= 18;

DELETE A FROM notas AS A
INNER JOIN clientes AS B
ON A.CPF = B.CPF
WHERE B.idade <= 18;

SELECT *
FROM notas;


CREATE TABLE `produtos2` (
  `codigo` varchar(10) NOT NULL,
  `descritor` varchar(100) DEFAULT NULL,
  `sabor` varchar(50) DEFAULT NULL,
  `tamanho` varchar(50) DEFAULT NULL,
  `embalagem` varchar(50) DEFAULT NULL,
  `preco_lista` float DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO produtos2
SELECT *
FROM produtos;

SELECT *
FROM produtos2;

UPDATE produtos2
SET preco_lista = 8;

DELETE FROM produtos2;

#############################
# TRANSAÇÕES
#############################

START TRANSACTION;

SELECT *
FROM vendedores;

UPDATE vendedores
SET comissao = comissao * 1.15;

SELECT *
FROM vendedores;

ROLLBACK;

START TRANSACTION;

UPDATE vendedores
SET comissao = comissao * 1.15;

SELECT *
FROM vendedores;

COMMIT;

SELECT *
FROM vendedores;