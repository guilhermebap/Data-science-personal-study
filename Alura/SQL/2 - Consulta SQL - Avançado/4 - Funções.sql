# https://cursos.alura.com.br/course/mysql-consultas-sql
# Funções

USE sucos_vendas;

#########################################################################################
# Funções de string

SELECT LTRIM('         Olá') AS resultado;

SELECT RTRIM('Olá               ') AS resultado;

SELECT TRIM('             Olá              ') AS resultado;

SELECT CONCAT('Olá', ' ', 'tudo bem', '?') AS resultado;

SELECT LOWER('OLÁ, TUDO BEM?') AS resultado;

SELECT UPPER('olá, tudo bem?') AS resultado;

SELECT SUBSTRING('Olá, tudo bem?', 6) AS resultado;

SELECT SUBSTRING('Olá, tudo bem?', 1, 3) AS resultado;

SELECT SUBSTRING('Olá, tudo bem?', 6, 4) AS resultado;

SELECT CONCAT(nome, ' (', CPF, ')') AS resultado
FROM tabela_de_clientes;

SELECT Nome, CONCAT(endereco_1, ' ', endereco_2, ' - ', ' Bairro: ', bairro, ' Cidade: ', cidade, '/', estado) AS 'Endereço Completo'
FROM tabela_de_clientes;

#########################################################################################
# Funções de datas

SELECT CURDATE() AS Resultado;

SELECT CURRENT_DATE() AS Resultado;

SELECT CURRENT_TIME() AS Resultado;

SELECT CURRENT_TIMESTAMP() AS Resultado;

SELECT YEAR(CURRENT_TIMESTAMP()) AS Resultado;

SELECT DAY(CURRENT_TIMESTAMP()) AS Resultado;

SELECT MONTH(CURRENT_TIMESTAMP()) AS Resultado;

SELECT MONTHNAME(CURRENT_TIMESTAMP()) AS Resultado;

SELECT DAYNAME(CURRENT_TIMESTAMP()) AS Resultado;

SELECT DATEDIFF(CURRENT_TIMESTAMP(), '1990-01-30') AS Resultado;

SELECT DATEDIFF(CURRENT_TIMESTAMP(), '1990-01-30')/365 AS Resultado;

SELECT DATE_SUB(CURRENT_TIMESTAMP(), INTERVAL 10 DAY) AS Resultado;

SELECT DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) AS Resultado;

SELECT Nome, CEIL(DATEDIFF(CURRENT_DATE(), data_de_nascimento)/365) AS Idade
FROM tabela_de_clientes;

SELECT NOME, TIMESTAMPDIFF (YEAR, DATA_DE_NASCIMENTO, CURDATE()) AS    IDADE
FROM  tabela_de_clientes;

#########################################################################################
# Funções matemáticas

SELECT A.nome_do_produto, A.embalagem, ROUND(A.preco_de_lista, 2), ROUND(X.preco_maximo, 2),
ROUND(((A.preco_de_lista / X.preco_maximo) -1) * 100, 2) AS Percentual
FROM tabela_de_produtos A
INNER JOIN vw_maiores_embalagens X
on A.embalagem = X.embalagem;

SELECT *
FROM notas_fiscais;

SELECT *
FROM itens_notas_fiscais;

SELECT YEAR(data_venda), FLOOR(SUM(preco * quantidade * imposto)) as Imposto_total
FROM notas_fiscais nf
INNER JOIN itens_notas_fiscais inf
ON nf.numero = inf.numero
WHERE YEAR(data_venda) = 2016;

#########################################################################################
# Conversão de dados

SELECT CURRENT_TIMESTAMP() AS Resultado;

SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), '%d/%m/%y') AS Resultado;

SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), '%d/%m/%Y') AS Resultado;

SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), '%H:%i %d/%m/%Y') AS Resultado;

SELECT CONVERT(23.3, CHAR) AS Resultado;

SELECT SUBSTRING(CONVERT(23.3, CHAR), 1, 1) AS Resultado;

SELECT *
FROM tabela_de_clientes;

SELECT * 
FROM notas_fiscais;

SELECT *
FROM itens_notas_fiscais;

SELECT  CONCAT(' O cliente ', tc.nome, ' faturou R$ ', CONVERT(ROUND(SUM(nf.quantidade * nf.preco), 2), CHAR), 
			   ' no ano de ', CONVERT(YEAR(nf.data_venda), CHAR)) AS Resultado
FROM tabela_de_clientes tc
INNER JOIN (SELECT inf.quantidade, inf.preco, nf.data_venda, nf.CPF 
			FROM notas_fiscais nf
            INNER JOIN itens_notas_fiscais inf
            on nf.numero = inf.numero) nf
ON nf.CPF = tc.CPF
WHERE YEAR(data_venda) = 2016
GROUP BY tc.nome;