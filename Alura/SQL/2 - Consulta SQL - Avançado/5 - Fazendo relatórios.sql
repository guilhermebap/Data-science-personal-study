# https://cursos.alura.com.br/course/mysql-consultas-sql
# Relatório

USE sucos_vendas;

SELECT *
FROM notas_fiscais;

SELECT *
FROM itens_notas_fiscais;

SELECT *
FROM tabela_de_clientes;

SELECT  tc.NOME, DATE_FORMAT(nf.data_venda, '%Y-%m') AS MES_ANO, 
		SUM(nf.quantidade) AS QUANTIDADE_VENDAS, 
        tc.VOLUME_DE_COMPRA AS QUANTIDADE_LIMITE
FROM tabela_de_clientes tc
INNER JOIN (SELECT inf.quantidade, nf.data_venda, nf.CPF 
			FROM notas_fiscais nf
            INNER JOIN itens_notas_fiscais inf
            on nf.numero = inf.numero) nf
ON nf.CPF = tc.CPF
GROUP BY tc.cpf, MES_ANO; 

SELECT X.CPF, X.nome, X.MES_ANO, X.QUANTIDADE_VENDAS, X.QUANTIDADE_LIMITE,
	   CASE
			WHEN (X.QUANTIDADE_LIMITE - X.QUANTIDADE_VENDAS) < 0 THEN 'INVÁLIDO'
            ELSE 'VÁLIDO'
		END AS 'STATUS_VENDA'
FROM (
SELECT  tc.NOME, tc.CPF, DATE_FORMAT(nf.data_venda, '%Y-%m') AS MES_ANO, 
		SUM(nf.quantidade) AS QUANTIDADE_VENDAS, 
        tc.VOLUME_DE_COMPRA AS QUANTIDADE_LIMITE
FROM tabela_de_clientes tc
INNER JOIN (SELECT inf.quantidade, nf.data_venda, nf.CPF 
			FROM notas_fiscais nf
            INNER JOIN itens_notas_fiscais inf
            on nf.numero = inf.numero) nf
ON nf.CPF = tc.CPF
GROUP BY tc.cpf, MES_ANO) X;

SELECT X.CPF, X.nome, X.MES_ANO, X.QUANTIDADE_VENDAS, X.QUANTIDADE_LIMITE,
	   CASE
			WHEN (X.QUANTIDADE_LIMITE - X.QUANTIDADE_VENDAS) < 0 THEN 'INVÁLIDO'
            ELSE 'VÁLIDO'
		END AS STATUS_VENDA,
        (X.QUANTIDADE_LIMITE - X.QUANTIDADE_VENDAS) AS DIFERENÇA,
        ROUND((1 - (X.QUANTIDADE_LIMITE / X.QUANTIDADE_VENDAS)) * 100, 3) AS DIFERENÇA_PORCENTAGEM
FROM (
SELECT  tc.NOME, tc.CPF, DATE_FORMAT(nf.data_venda, '%Y-%m') AS MES_ANO, 
		SUM(nf.quantidade) AS QUANTIDADE_VENDAS, 
        tc.VOLUME_DE_COMPRA AS QUANTIDADE_LIMITE
FROM tabela_de_clientes tc
INNER JOIN (SELECT inf.quantidade, nf.data_venda, nf.CPF 
			FROM notas_fiscais nf
            INNER JOIN itens_notas_fiscais inf
            on nf.numero = inf.numero) nf
ON nf.CPF = tc.CPF
GROUP BY tc.cpf, MES_ANO) X
HAVING (X.QUANTIDADE_LIMITE - X.QUANTIDADE_VENDAS) < 0;