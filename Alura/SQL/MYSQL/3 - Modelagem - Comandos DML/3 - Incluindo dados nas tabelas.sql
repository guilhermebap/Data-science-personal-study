USE vendas_sucos;

INSERT INTO PRODUTOS (CODIGO, DESCRITOR, SABOR, TAMANHO, EMBALAGEM, PRECO_LISTA)
VALUES ('1040107', 'Light - 350 ml - Melância', 'Melância', '350 ml', 'Lata', 4.56);

SELECT *
FROM PRODUTOS;

INSERT INTO PRODUTOS (CODIGO, DESCRITOR, SABOR, TAMANHO, EMBALAGEM, PRECO_LISTA)
VALUES ('1040108', 'Light - 350 ml - Graviola', 'Graviola', '350 ml', 'Lata', 4.00);

INSERT INTO PRODUTOS
VALUES ('1040109', 'Light - 350 ml - Açai', 'Açai', '350 ml', 'Lata', 5.60);

INSERT INTO PRODUTOS
VALUES ('1040110', 'Light - 350 ml - Jaca', 'Jaca', '350 ml', 'Lata', 6.00),
('1040111', 'Light - 350 ml - Manga', 'Manga', '350 ml', 'Lata', 3.50);

INSERT INTO CLIENTES 
(CPF, NOME, ENDERECO,  BAIRRO, CIDADE, ESTADO, CEP, DATA_NASCIMENTO, IDADE, SEXO, LIMITE_CREDITO, VOLUME_COMPRA, PRIMEIRA_COMPRA)
VALUES
('1471156710','Érica Carvalho','R. Iriquitia','Jardins','São Paulo','SP','80012212','19900901',27,'F',170000,24500,0),
('19290992743','Fernando Cavalcante','R. Dois de Fevereiro','Água Santa','Rio de Janeiro','RJ','22000000','20000212',18,'M',100000,20000,1),
('2600586709','César Teixeira','Rua Conde de Bonfim','Tijuca','Rio de Janeiro','RJ','22020001','20000312',18,'M',120000,22000,0);

SELECT *
FROM CLIENTES;


################################################
# IMPORTANDO DADOS DE UM OUTRO BANCO DE DADOS
################################################

USE vendas_sucos;

SELECT codigo_do_produto AS codigo_produto, nome_do_produto AS descritor, sabor, tamanho, embalagem, preco_de_lista AS preco_lista
FROM sucos_vendas.tabela_de_produtos
WHERE codigo_do_produto NOT IN (SELECT codigo FROM vendas_sucos.produtos);

SELECT *
FROM produtos;

INSERT INTO vendas_sucos.produtos
SELECT codigo_do_produto AS codigo_produto, nome_do_produto AS descritor, sabor, tamanho, embalagem, preco_de_lista AS preco_lista
FROM sucos_vendas.tabela_de_produtos
WHERE codigo_do_produto NOT IN (SELECT codigo FROM vendas_sucos.produtos);

SELECT *
FROM produtos;

SELECT CPF, nome, endereco_1 AS endereco, bairro, cidade, estado, CEP, data_de_nascimento AS data_nascimento, idade, sexo,
limite_de_credito AS limite_credito, volume_de_compra AS volume_compra, primeira_compra
FROM sucos_vendas.tabela_de_clientes
WHERE CPF NOT IN (SELECT CPF FROM vendas_sucos.clientes);

SELECT *
FROM vendas_sucos.clientes;

INSERT INTO vendas_sucos.clientes (CPF,NOME,ENDERECO,BAIRRO,CIDADE,ESTADO,CEP,DATA_NASCIMENTO,IDADE,SEXO,LIMITE_CREDITO,VOLUME_COMPRA,PRIMEIRA_COMPRA)
SELECT CPF, nome, endereco_1 AS endereco, bairro, cidade, estado, CEP, data_de_nascimento AS data_nascimento, idade, sexo,
limite_de_credito AS limite_credito, volume_de_compra AS volume_compra, primeira_compra
FROM sucos_vendas.tabela_de_clientes
WHERE CPF NOT IN (SELECT CPF FROM vendas_sucos.clientes);

SELECT *
FROM vendas_Sucos.clientes;

USE vendas_sucos;

SELECT * 
FROM vendas_sucos.vendedores;