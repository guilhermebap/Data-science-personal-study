USE sucos_vendas;

DROP PROCEDURE IF EXISTS`Comparativo_Vendas`;
DELIMITER $$

CREATE PROCEDURE `Comparativo_Vendas` (vDate1 DATE, vDate2 DATE)
BEGIN
	DECLARE faturamento_vendas1 FLOAT;
    DECLARE faturamento_vendas2 FLOAT;
    DECLARE variacao_percentual FLOAT;
    
    SELECT SUM(B.QUANTIDADE * B.PRECO) INTO faturamento_vendas1
    FROM NOTAS_FISCAIS A INNER JOIN ITENS_NOTAS_FISCAIS B
	ON A.NUMERO = B.NUMERO
	WHERE A.DATA_VENDA = vDate1;
    
    SELECT SUM(B.QUANTIDADE * B.PRECO) INTO faturamento_vendas2
    FROM NOTAS_FISCAIS A INNER JOIN ITENS_NOTAS_FISCAIS B
	ON A.NUMERO = B.NUMERO
	WHERE A.DATA_VENDA = vDate2;
    
    SET variacao_percentual = ((faturamento_vendas2 / faturamento_vendas1) - 1) * 100;
    
    IF variacao_percentual > 10 THEN
		SELECT 'Verde', variacao_percentual AS 'Variação percentual';
	ELSEIF variacao_percentual >= -10 AND variacao_percentual <= 10 THEN
		SELECT 'Amarela', variacao_percentual AS 'Variação percentual';
	ELSE
		SELECT 'Vermelho', variacao_percentual AS 'Variação percentual';
	END IF;
END $$
DELIMITER ;

SELECT *
FROM notas_fiscais;

CALL Comparativo_Vendas('2015-01-05', '2015-01-01');