#####################################
# AUTO INCREMENT
#####################################

CREATE TABLE tab_identity (ID INT AUTO_INCREMENT, DESCRITOR VARCHAR(20), PRIMARY KEY(ID));

INSERT INTO tab_identity (DESCRITOR) 
VALUES ('Cliente1');

INSERT INTO tab_identity (DESCRITOR) 
VALUES ('Cliente2');

INSERT INTO tab_identity (DESCRITOR) 
VALUES ('Cliente3');

INSERT INTO tab_identity (ID, DESCRITOR) 
VALUES (NULL, 'Cliente4');

SELECT *
FROM tab_identity;

DELETE FROM tab_identity 
WHERE ID = 3;

SELECT *
FROM tab_identity;

INSERT INTO tab_identity (ID, DESCRITOR) 
VALUES (NULL, 'Cliente6');

INSERT INTO tab_identity (ID, DESCRITOR) 
VALUES (NULL, 'Cliente7');

DELETE FROM tab_identity 
WHERE ID = 2;

SELECT *
FROM tab_identity;

DROP TABLE IF EXISTS tab_identity;

#############################################
# DEFININDO PADRÕES DE CAMPO
#############################################

CREATE TABLE tab_padrao(
id INT AUTO_INCREMENT,
descritor VARCHAR(20),
endereco VARCHAR(100) NULL,
cidade VARCHAR(50) DEFAULT 'Rio de Janeiro',
data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
PRIMARY KEY(ID));

SELECT *
FROM tab_padrao;

INSERT INTO tab_padrao (descritor, endereco, cidade, data_criacao)
VALUES('Cliente X', 'Rua projetada A', 'São Paulo', '2019-01-01'); 

SELECT *
FROM tab_padrao;

INSERT INTO tab_padrao (descritor)
VALUES('Cliente Y');

SELECT *
FROM tab_padrao;

DROP TABLE tab_padrao;

DROP TABLE produtos2;