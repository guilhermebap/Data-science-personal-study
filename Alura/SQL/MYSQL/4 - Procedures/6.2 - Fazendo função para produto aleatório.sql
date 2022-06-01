USE sucos_vendas;

DROP FUNCTION IF EXISTS `f_produto_aleatorio`;
DELIMITER $$

CREATE FUNCTION `f_produto_aleatorio` ()
RETURNS VARCHAR(10)
BEGIN
	DECLARE num_max_tabela INT DEFAULT (SELECT COUNT(*) FROM tabela_de_Produtos);
    DECLARE num_aleatorio INT;
    SET num_aleatorio = f_numero_aleatorio(1, num_max_tabela) - 1;
    
    RETURN (SELECT codigo_do_produto
			FROM tabela_de_produtos
            LIMIT num_aleatorio, 1);
END $$
DELIMITER ;

SELECT *
FROM tabela_de_produtos;

SELECT f_produto_aleatorio();