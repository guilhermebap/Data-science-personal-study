USE vendas_sucos;
DROP PROCEDURE IF EXISTS sp_Exerc01;

DELIMITER $$
USE vendas_sucos$$
CREATE PROCEDURE `sp_Exerc01`()
BEGIN
	DECLARE Cliente VARCHAR(10) DEFAULT 'João';
    DECLARE Idade INTEGER DEFAULT 10;
    DECLARE DataNascimento DATE DEFAULT '2007-01-10';
    DECLARE Custo DECIMAL(4,2) DEFAULT 10.23;
    
    SELECT Cliente;
    SELECT Idade;
    SELECT DataNascimento;
    SELECT Custo;
END$$

DELIMITER ;

CALL sp_Exerc01;

DROP PROCEDURE IF EXISTS hello_world;
DELIMITER $$

CREATE PROCEDURE `hello_world`()
BEGIN
	DECLARE texto VARCHAR(20) DEFAULT 'Hello World!';
    SELECT texto;
    SET texto = 'Olá Mundo!!!!!';
    SELECT texto;
END$$
DELIMITER ;

CALL hello_world;

DROP PROCEDURE IF EXISTS data_hoje;

DELIMITER $$
CREATE PROCEDURE `data_hoje`()
/* Função de mostra a data de hoje */
-- O comando utilizado é o LOCALTIMESTAMP
BEGIN
	DECLARE data_de_hoje DATE DEFAULT LOCALTIMESTAMP();
    SELECT data_de_hoje;
END$$
DELIMITER ;

CALL data_hoje;

