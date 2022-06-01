# https://cursos.alura.com.br/course/mysql-consultas-sql
# Utilização de filtros avançados
# SELECT, LIKE, IN, AS, BETWEEN e o simbolo %

USE sucos_vendas;

SELECT *
FROM itens_notas_fiscais;

SELECT *
FROM tabela_de_produtos;

SELECT *
FROM tabela_de_produtos
WHERE sabor IN ('maça', 'uva');

SELECT *
FROM tabela_de_produtos
WHERE preco_de_lista BETWEEN 8 AND 12;

SELECT *
FROM tabela_de_produtos
WHERE sabor LIKE '%maça%' OR sabor LIKE '%Limão%';

SELECT *
FROM tabela_de_produtos
WHERE sabor LIKE '%maça%' OR sabor = 'maracujá';

SELECT *
FROM tabela_de_clientes;

SELECT CPF , nome AS 'Nome do Cliente', Cidade
FROM tabela_de_clientes;

SELECT *
FROM tabela_de_clientes
WHERE nome LIKE '%Mattos%';

SELECT *
FROM tabela_de_clientes
WHERE nome LIKE '%Mattos';

