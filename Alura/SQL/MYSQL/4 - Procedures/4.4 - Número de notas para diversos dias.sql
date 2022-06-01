USE sucos_vendas;

DROP PROCEDURE IF EXISTS `Soma_Dias_Notas`;
DELIMITER $$

CREATE PROCEDURE `Soma_Dias_Notas` (data_inicio DATE, data_final DATE)
BEGIN
	DECLARE num_notas INT;
    
    WHILE data_final >= data_inicio DO
		SELECT COUNT(numero) INTO num_notas
		FROM notas_fiscais
		WHERE data_venda = data_inicio;
        
        SELECT CONCAT(DATE_FORMAT(data_inicio, "%d/%m/%Y"),  ' - ', CAST(num_notas AS CHAR(5))) AS 'Vendas por Dia';
        SET data_inicio = (ADDDATE(data_inicio, INTERVAL 1 DAY));      
    END WHILE;
END $$
DELIMITER ;

SELECT *
FROM notas_fiscais;

CALL Soma_Dias_Notas('2015-01-01', '2015-01-10');