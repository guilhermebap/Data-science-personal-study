USE sucos_vendas;

DROP PROCEDURE IF EXISTS `Limite_Creditos`;
DELIMITER $$

CREATE PROCEDURE `Limite_Creditos` ()
BEGIN
	DECLARE lim_credito FLOAT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE c CURSOR FOR SELECT limite_de_credito FROM tabela_de_clientes;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN c;    
    WHILE done = FALSE
    DO
    FETCH c INTO lim_credito;
    IF done = FALSE THEN
		SELECT lim_credito;
	END IF;
    END WHILE;   
    
    CLOSE c;
END $$
DELIMITER ;

SELECT *
FROM tabela_de_clientes;

CALL Limite_Creditos();