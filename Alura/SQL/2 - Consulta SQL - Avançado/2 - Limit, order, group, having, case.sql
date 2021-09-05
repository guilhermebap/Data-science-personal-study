# https://cursos.alura.com.br/course/mysql-consultas-sql
# Utilização de filtros avançados
# DISTINCT, LIMIT, ORDER BY, GROUP BY, Having, CASE

# Aggregate functions - https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html

USE sucos_vendas;

SELECT *
FROM tabela_de_produtos;

SELECT embalagem, tamanho
FROM tabela_de_produtos;

#########################################################################################
# Utilizando o DISTINCT

SELECT DISTINCT embalagem, tamanho
FROM tabela_de_produtos;

SELECT DISTINCT embalagem, tamanho
FROM tabela_de_produtos
WHERE sabor = 'Maça';

SELECT DISTINCT embalagem, tamanho, sabor
FROM tabela_de_produtos;

SELECT DISTINCT bairro
FROM tabela_de_clientes
WHERE cidade = 'Rio de Janeiro';

#########################################################################################
# Utilizando o LIMIT

SELECT DISTINCT bairro
FROM tabela_de_clientes
WHERE cidade = 'Rio de Janeiro'
LIMIT 3;

SELECT DISTINCT bairro
FROM tabela_de_clientes
WHERE cidade = 'Rio de Janeiro'
LIMIT 2,2;

SELECT DISTINCT bairro
FROM tabela_de_clientes
WHERE cidade = 'Rio de Janeiro'
LIMIT 0,4;

SELECT DISTINCT bairro
FROM tabela_de_clientes
WHERE cidade = 'Rio de Janeiro'
LIMIT 1,4;

SELECT *
FROM notas_fiscais
WHERE data_venda = '2017-01-01'
LIMIT 10;

#########################################################################################
# Utilizando o ORDER BY

SELECT * 
FROM tabela_de_produtos;

SELECT * 
FROM tabela_de_produtos
ORDER BY PRECO_DE_LISTA;

SELECT * 
FROM tabela_de_produtos
ORDER BY PRECO_DE_LISTA DESC;

SELECT * 
FROM tabela_de_produtos
ORDER BY nome_do_produto;

SELECT * 
FROM tabela_de_produtos
ORDER BY embalagem ASC, preco_de_lista DESC;

SELECT * 
FROM tabela_de_produtos
ORDER BY embalagem ASC, preco_de_lista DESC;

SELECT CODIGO_DO_PRODUTO
FROM tabela_de_produtos
WHERE nome_do_produto = 'Linha Refrescante - 1 Litro - Morango/Limão';

SELECT *
FROM itens_notas_fiscais; 

SELECT DISTINCT quantidade
FROM itens_notas_fiscais
WHERE CODIGO_DO_PRODUTO = (SELECT CODIGO_DO_PRODUTO FROM tabela_de_produtos WHERE nome_do_produto = 'Linha Refrescante - 1 Litro - Morango/Limão')
ORDER BY quantidade DESC;

#########################################################################################
# Utilizando GROUP BY

SELECT estado, limite_de_credito
FROM tabela_de_clientes;

SELECT estado, SUM(limite_de_credito) as limite_total
FROM tabela_de_clientes
GROUP BY estado;

SELECT embalagem, preco_de_lista
FROM tabela_de_produtos;

SELECT embalagem, MAX(preco_de_lista) as 'Maior Preço'
FROM tabela_de_produtos
GROUP BY embalagem;

SELECT embalagem, COUNT(*) as 'Contador'
FROM tabela_de_produtos
GROUP BY embalagem;

SELECT bairro, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY bairro;

SELECT bairro, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
WHERE cidade = 'rio de janeiro'
GROUP BY bairro;

SELECT bairro, estado, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY bairro;

SELECT bairro, estado, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY bairro
ORDER BY limite DESC;

SELECT estado, bairro, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY estado, bairro;

SELECT estado, bairro, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY estado, bairro
ORDER BY estado, bairro;

SELECT estado, bairro, SUM(limite_de_Credito) as Limite
FROM tabela_de_clientes
GROUP BY estado, bairro
ORDER BY limite DESC;

SELECT codigo_do_produto, quantidade, COUNT(quantidade) as Contador_quantidade
FROM itens_notas_fiscais
WHERE codigo_do_produto = '1101035'
GROUP BY quantidade
ORDER BY quantidade DESC
LIMIT 1;

#########################################################################################
# Utilizando o HAVING
# Having é um filtro que se aplica ao resultado de uma agregação

SELECT estado, SUM(limite_de_credito) as soma_limite
FROM tabela_de_clientes
GROUP BY estado;

SELECT estado, SUM(limite_de_credito) as soma_limite
FROM tabela_de_clientes
GROUP BY estado
HAVING soma_limite > 900000;

SELECT embalagem, MAX(preco_de_lista) AS maior_preco, MIN(preco_de_lista) AS menor_preco
FROM tabela_de_produtos
GROUP BY embalagem;

SELECT embalagem, MAX(preco_de_lista) AS maior_preco, MIN(preco_de_lista) AS menor_preco
FROM tabela_de_produtos
GROUP BY embalagem
HAVING SUM(preco_de_lista) <= 80;

SELECT embalagem, MAX(preco_de_lista) AS maior_preco, MIN(preco_de_lista) AS menor_preco
FROM tabela_de_produtos
GROUP BY embalagem
HAVING SUM(preco_de_lista) <= 80 AND MAX(PRECO_DE_LISTA) > 5;

#########################################################################################
# Utilizando CASE - CASE/WHEN/THEN e CASE/ELSE

SELECT  *
FROM tabela_de_produtos;

SELECT nome_do_produto, preco_de_lista,
CASE
	WHEN preco_de_lista >= 12 THEN 'Produto caro'
    WHEN preco_de_lista >=7 THEN 'Produto em conta'
    ELSE 'Produto barato'
END AS 'Status_preco'
FROM tabela_de_produtos;

SELECT embalagem,
CASE
	WHEN preco_de_lista >= 12 THEN 'Produto caro'
    WHEN preco_de_lista >=7 THEN 'Produto em conta'
    ELSE 'Produto barato'
END AS 'Status_preco', AVG(PRECO_DE_LISTA) as 'preco_medio'
FROM tabela_de_produtos
GROUP BY embalagem,
CASE
	WHEN preco_de_lista >= 12 THEN 'Produto caro'
    WHEN preco_de_lista >=7 THEN 'Produto em conta'
    ELSE 'Produto barato'
END;

SELECT nome,
CASE
	WHEN YEAR(data_de_nascimento) < 1990 THEN 'Velhos'
    WHEN YEAR(data_de_nascimento) < 1995 THEN 'Jovens'
    ELSE 'Crianças'
END AS 'classificacao_idade'
FROM tabela_de_clientes;

SELECT nome,
CASE
	WHEN YEAR(data_de_nascimento) < 1990 THEN 'Velhos'
    WHEN YEAR(data_de_nascimento) < 1995 THEN 'Jovens'
    ELSE 'Crianças'
END AS 'classificacao_idade'
FROM tabela_de_clientes
ORDER BY classificacao_idade DESC;