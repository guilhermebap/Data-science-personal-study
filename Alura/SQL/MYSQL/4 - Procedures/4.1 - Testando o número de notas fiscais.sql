USE sucos_vendas;

SELECT *
FROM notas_fiscais;

DROP PROCEDURE IF EXISTS `Testa_Numero_Notas`;
DELIMITER $$

CREATE PROCEDURE `Testa_Numero_Notas`(vDate DATE)
BEGIN
	DECLARE num_notas INT;
    
    SELECT COUNT(numero) INTO num_notas
    FROM notas_fiscais
    WHERE data_venda = vDate;
    
    IF num_notas > 70 THEN
		SELECT 'Muita Nota', num_notas AS 'Numero de Notas';
	ELSE
		SELECT 'Pouca Nota', num_notas AS 'Numero de Notas';    
    END IF;
END $$
DELIMITER ;

CALL Testa_Numero_Notas('2015-01-01')