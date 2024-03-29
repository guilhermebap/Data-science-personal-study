USE sucos_vendas;

SET GLOBAL LOG_BIN_TRUST_FUNCTION_CREATORS = 1;

DROP FUNCTION IF EXISTS `NumeroNotas`;
DELIMITER $$

CREATE FUNCTION `NumeroNotas` (vData DATE)
RETURNS INTEGER
BEGIN
    RETURN (SELECT COUNT(*) FROM notas_fiscais WHERE data_venda = vData);
END $$
DELIMITER ;

SELECT *
FROM notas_fiscais;

SELECT NumeroNotas('2015-01-04');

