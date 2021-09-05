USE sucos;

# Inserindo valores na tabela 
INSERT INTO tabela_de_vendedores
(matricula, nome, percentual_comissao)
VALUES
('00235', 'Márcio Almeida da Silva', '8');

INSERT INTO tabela_de_vendedores
(matricula, nome, percentual_comissao)
VALUES
('00236', 'Cláudia Morais', '8');

# Alterando valores já cadastrados na tabela
UPDATE tabela_de_vendedores 
SET percentual_comissao = 11
WHERE matricula = '00236';

UPDATE tabela_de_vendedores 
SET nome = 'José Geraldo da Fonseca Junior'
WHERE matricula = '00233';

# Deletando dados na tabela
DELETE FROM tabela_de_vendedores
WHERE matricula = '00233'; 

# Adicionando uma chave primária
ALTER TABLE tabela_de_vendedores ADD PRIMARY KEY (matricula);

# Adicionando campos a uma tabela
ALTER TABLE tabela_de_vendedores ADD COLUMN (data_admissao DATE, de_ferias bit(1));

INSERT INTO tabela_de_vendedores 
(matricula, nome, percentual_comissao, data_admissao, de_ferias)
VALUES
('00237', 'Roberta Martins', 11, '2017-03-18', 1),
('00238', 'Péricles Alves', 11, '2016-08-21', 0);

UPDATE tabela_de_vendedores 
SET data_admissao = '2014-08-15', de_ferias=0
WHERE matricula = '00235';

UPDATE tabela_de_vendedores 
SET data_admissao = '2013-09-17', de_ferias=1, percentual_comissao=8
WHERE matricula = '00236';

# Selecionando com filtro
SELECT *
FROM tabela_de_vendedores
WHERE percentual_comissao >10;

# Filtrando datas
SELECT * 
FROM tabela_de_vendedores
WHERE YEAR(data_admissao) >= 2016;

# Filtro composto
SELECT *
FROM tabela_de_vendedores
WHERE de_ferias = 1 AND YEAR(data_admissao) < 2016;

SELECT * FROM tabela_de_vendedores;