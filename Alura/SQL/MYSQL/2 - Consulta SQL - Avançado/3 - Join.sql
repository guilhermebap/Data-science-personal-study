# https://cursos.alura.com.br/course/mysql-consultas-sql
# Juntando tabelas - JOIN, UNION, sub consultas, views

USE sucos_vendas;

SELECT * 
FROM tabela_de_vendedores;

SELECT *
FROM notas_fiscais;

#########################################################################################
# Utilizando o INNER JOIN

SELECT *
FROM tabela_de_vendedores A
INNER JOIN notas_fiscais B
ON A.matricula = B.matricula;

SELECT *
FROM tabela_de_vendedores A
INNER JOIN notas_fiscais B
ON A.matricula = B.matricula;

# Metodo 01 - Mais atual e mais organizado
SELECT A.matricula, A.nome, COUNT(*)
FROM tabela_de_vendedores A
INNER JOIN notas_fiscais B
ON A.matricula = B.matricula
GROUP BY A.MATRICULA;

# Metodo 02 - Antigo e menos utilizado hoje em dia
SELECT A.matricula, A.nome, COUNT(*)
FROM tabela_de_vendedores A, notas_fiscais B
WHERE A.matricula = B.matricula
GROUP BY A.MATRICULA; 

SELECT *
FROM itens_notas_fiscais;

SELECT *
FROM notas_fiscais;

SELECT DISTINCT YEAR(data_venda)
FROM notas_fiscais ;

SELECT A.numero, data_venda, quantidade, preco
FROM notas_fiscais A
INNER JOIN itens_notas_fiscais B
ON A.numero = B.numero;

SELECT YEAR(data_venda), SUM(quantidade * preco) AS faturamento
FROM notas_fiscais A
INNER JOIN itens_notas_fiscais B
ON A.numero = B.numero
GROUP BY YEAR(data_venda);

#########################################################################################
# Utilizando o LEFT e o RIGHT JOIN

SELECT COUNT(*)
FROM tabela_de_clientes;

SELECT CPF, COUNT(*)
FROM notas_fiscais
GROUP BY CPF;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM tabela_de_clientes A 
INNER JOIN notas_fiscais B
ON A.CPF = B.CPF;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM tabela_de_clientes A 
INNER JOIN notas_fiscais B
ON A.CPF = B.CPF;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM tabela_de_clientes A 
LEFT JOIN notas_fiscais B
ON A.CPF = B.CPF;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM tabela_de_clientes A 
LEFT JOIN notas_fiscais B
ON A.CPF = B.CPF
WHERE B.CPF IS NULL;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM tabela_de_clientes A 
LEFT JOIN notas_fiscais B
ON A.CPF = B.CPF
WHERE B.CPF IS NULL;

SELECT DISTINCT A.CPF AS CPF_cliente, nome, B.CPF AS CPF_nota_fiscal
FROM notas_fiscais B
RIGHT JOIN tabela_de_clientes A
ON A.CPF = B.CPF
WHERE B.CPF IS NULL;

#########################################################################################
# Utilizando o CROSS JOIN
# O FULL JOIN não é suportada completamente pelo mysql, porém é possível resolver com UNION

SELECT nome, bairro
FROM tabela_de_vendedores;

SELECT nome, bairro
FROM tabela_de_clientes;

SELECT A.nome, A.bairro, B.nome, B.bairro
FROM tabela_de_vendedores A, tabela_de_clientes B;

#########################################################################################
# Utilizando o UNION

SELECT nome, bairro
FROM tabela_de_vendedores
UNION
SELECT nome, bairro
FROM tabela_de_clientes;

SELECT nome, bairro, 'Vendedores' AS tipo
FROM tabela_de_vendedores
UNION
SELECT nome, bairro, 'Clientes' AS tipo
FROM tabela_de_clientes;

SELECT nome, bairro, 'Vendedores' AS tipo, matricula as CPF
FROM tabela_de_vendedores
UNION
SELECT nome, bairro, 'Clientes' AS tipo, cpf
FROM tabela_de_clientes;

#########################################################################################
# Utilizando o FULL JOIN

SELECT A.bairro, A.nome, de_ferias, B.bairro, B.nome
FROM tabela_de_vendedores A 
LEFT JOIN tabela_de_clientes B
ON A.bairro = B.bairro;

SELECT A.bairro, A.nome, B.nome, B.bairro
FROM tabela_de_vendedores A 
RIGHT JOIN tabela_de_clientes B
ON A.bairro = B.bairro;

SELECT A.bairro, A.nome, de_ferias, B.bairro, B.nome
FROM tabela_de_vendedores A 
LEFT JOIN tabela_de_clientes B
ON A.bairro = B.bairro
UNION
SELECT A.bairro, A.nome, de_ferias, B.bairro, B.nome
FROM tabela_de_vendedores A 
RIGHT JOIN tabela_de_clientes B
ON A.bairro = B.bairro;

#########################################################################################
# Utilizando sub consultas

SELECT DISTINCT bairro
FROM tabela_de_vendedores;

SELECT * 
FROM tabela_de_clientes
WHERE bairro in (SELECT DISTINCT bairro FROM tabela_de_vendedores);

SELECT embalagem, MAX(PRECO_DE_LISTA) AS preco_maximo
FROM tabela_de_produtos 
GROUP BY EMBALAGEM; 

SELECT Z.embalagem, Z.preco_maximo
FROM (SELECT embalagem, MAX(PRECO_DE_LISTA) AS preco_maximo FROM tabela_de_produtos GROUP BY EMBALAGEM) Z
WHERE Z.preco_maximo >= 10;

##########################################################################################
# Utilizando views

SELECT X.embalagem, X.preco_maximo
FROM vw_maiores_embalagens X
WHERE X.preco_maximo > 10;

SELECT A.nome_do_produto, A.embalagem, A.preco_de_lista, X.preco_maximo
FROM tabela_de_produtos A
INNER JOIN vw_maiores_embalagens X
on A.embalagem = X.embalagem;

SELECT A.nome_do_produto, A.embalagem, A.preco_de_lista, X.preco_maximo,
(A.preco_de_lista / X.preco_maximo) * 100 AS Percentual
FROM tabela_de_produtos A
INNER JOIN vw_maiores_embalagens X
on A.embalagem = X.embalagem;

SELECT A.nome_do_produto, A.embalagem, A.preco_de_lista, X.preco_maximo,
((A.preco_de_lista / X.preco_maximo) -1) * 100 AS Percentual
FROM tabela_de_produtos A
INNER JOIN vw_maiores_embalagens X
on A.embalagem = X.embalagem;