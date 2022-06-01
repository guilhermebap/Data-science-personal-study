USE sucos_vendas;

DROP PROCEDURE IF EXISTS `Mais_Um_Campo`;
DELIMITER $$

CREATE PROCEDURE `Mais_Um_Campo`(vMes INT, vAno INT)
BEGIN
	DECLARE quantidade INT;
    DECLARE preco FLOAT;
    DECLARE faturamento FLOAT DEFAULT 0;
    DECLARE done INT DEFAULT 0;
    DECLARE c CURSOR FOR (SELECT inf.quantidade, inf.preco
						  FROM notas_fiscais AS nf
                          INNER JOIN itens_notas_fiscais AS inf
                          ON nf.numero = inf.numero
                          WHERE MONTH(nf.data_venda) = vMes AND YEAR(nf.data_venda) = vAno);
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    OPEN c;
	WHILE done = 0
    DO
		FETCH c INTO quantidade, preco;
        IF done = 0 THEN
			SET faturamento = faturamento + (quantidade * preco);
        END IF;
    END WHILE;
    CLOSE c;
    SELECT faturamento;    
END $$
DELIMITER ;

SELECT *
FROM notas_fiscais;

SELECT *
FROM itens_notas_fiscais;

CALL Mais_Um_Campo(4, 2015);


