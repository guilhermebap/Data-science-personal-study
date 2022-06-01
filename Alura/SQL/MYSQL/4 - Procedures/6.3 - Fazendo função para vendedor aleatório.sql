USE sucos_vendas;

DROP FUNCTION IF EXISTS `f_vendedor_aleatorio`;
DELIMITER $$

CREATE FUNCTION `f_vendedor_aleatorio`()
RETURNS VARCHAR(11)
BEGIN
	DECLARE num_max_tabela INT DEFAULT (SELECT COUNT(*) FROM tabela_de_vendedores);
    DECLARE num_aleatorio INT;
    SET num_aleatorio = f_numero_aleatorio(1, num_max_tabela) - 1;
    
    RETURN (SELECT matricula
			FROM tabela_de_vendedores
            LIMIT num_aleatorio, 1);
END $$
DELIMITER ;

SELECT *
FROM tabela_de_vendedores;

SELECT f_vendedor_aleatorio();