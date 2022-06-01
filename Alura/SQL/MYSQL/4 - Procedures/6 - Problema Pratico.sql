USE sucos_vendas;

DROP FUNCTION IF EXISTS `f_numero_aleatorio`;
DELIMITER $$

CREATE FUNCTION `f_numero_aleatorio` (vMin INT, vMax INT)
RETURNS INTEGER
BEGIN
	RETURN (SELECT FLOOR(RAND() * (vMax - vMin + 1) + vMin));
END $$
DELIMITER ;

SELECT f_numero_aleatorio(0, 100);

#############################################################################################

USE sucos_vendas;
DROP FUNCTION IF EXISTS `f_cliente_aleatorio`;
DELIMITER $$

CREATE FUNCTION `f_cliente_aleatorio` ()
RETURNS VARCHAR(11)
BEGIN
	DECLARE num_max_tabela INT DEFAULT (SELECT COUNT(*) FROM tabela_de_clientes);
    DECLARE num_aleatorio INT;
    SET num_aleatorio =  f_numero_aleatorio(1, num_max_tabela) - 1;
    RETURN (SELECT cpf 
			FROM  tabela_de_clientes
            LIMIT num_aleatorio, 1);
END $$
DELIMITER ;

SELECT * 
FROM tabela_de_clientes;

SELECT f_cliente_aleatorio();


#######################################################################################
# CRIANDO PROCEDURE PARA ADICIONAR VENDAS ALEATORIAS AO DB

USE sucos_vendas;
DROP PROCEDURE IF EXISTS `sp_inserir_vendas`;
DELIMITER $$

CREATE PROCEDURE `sp_inserir_vendas`(vData DATE, maxItens INT, maxQuantidade INT)
BEGIN
	DECLARE vNumeroNota INT DEFAULT ((SELECT MAX(numero) FROM notas_fiscais) + 1);
    DECLARE vProduto VARCHAR(10);
    DECLARE vQuantidade INT;
    DECLARE vPreco FLOAT;
    DECLARE totalItens INT;
    DECLARE contador INT DEFAULT 1;
    DECLARE itensNotas INT;
    
    INSERT INTO notas_fiscais (CPF, matricula, data_venda, numero, imposto)
    VALUES (f_cliente_aleatorio(), f_vendedor_aleatorio(), vData, vNumeroNota, 0.18);
    
    SET totalItens = f_numero_aleatorio(1, maxItens);
	WHILE contador <= totalItens
	DO
		SET vProduto = f_produto_aleatorio();
        SELECT COUNT(*) INTO itensNotas FROM itens_notas_fiscais WHERE numero = vNumeroNota AND CODIGO_DO_PRODUTO = vProduto;
        IF itensNotas = 0 THEN
			SET vQuantidade = f_numero_aleatorio(10, maxQuantidade);
            
            SELECT preco_de_lista INTO vPreco
            FROM tabela_de_produtos
            WHERE CODIGO_DO_PRODUTO = vProduto;
            
            INSERT INTO itens_notas_fiscais (numero, codigo_do_produto, quantidade, preco)
            VALUES (vNumeroNota, vProduto, vQuantidade, vPreco);
        END IF;
        SET contador = contador + 1;        
	END WHILE;
END $$
DELIMITER ;

CALL sp_inserir_vendas('20190517', 10, 100);

SELECT * 
FROM notas_fiscais
WHERE DATA_VENDA = '20190517';

SELECT *
FROM notas_fiscais AS nf
INNER JOIN itens_notas_fiscais AS inf
ON nf.numero = inf.numero
WHERE nf.numero = '87982';

SELECT *
FROM TAB_FATURAMENTO
WHERE data_venda = 20190517;


#######################################################################################
# MELHORANDOS AS TRIGGERS COM PROCEDURES
USE sucos_vendas;
CREATE TABLE TAB_FATURAMENTO (DATA_VENDA DATE NULL, TOTAL_VENDA FLOAT);

DROP PROCEDURE IF EXISTS `sp_calcula_faturamento`;
DELIMITER $$

CREATE PROCEDURE `sp_calcula_faturamento`()
BEGIN
  DELETE FROM TAB_FATURAMENTO;
  INSERT INTO TAB_FATURAMENTO
  SELECT A.DATA_VENDA, SUM(B.QUANTIDADE * B.PRECO) AS TOTAL_VENDA FROM
  NOTAS_FISCAIS A INNER JOIN ITENS_NOTAS_FISCAIS B
  ON A.NUMERO = B.NUMERO
  GROUP BY A.DATA_VENDA;
END $$

CREATE TRIGGER TG_CALCULA_FATURAMENTO_INSERT AFTER INSERT ON ITENS_NOTAS_FISCAIS
FOR EACH ROW BEGIN
	CALL sp_calcula_faturamento();
END $$

CREATE TRIGGER TG_CALCULA_FATURAMENTO_UPDATE AFTER UPDATE ON ITENS_NOTAS_FISCAIS
FOR EACH ROW BEGIN
	CALL sp_calcula_faturamento();
END $$

CREATE TRIGGER TG_CALCULA_FATURAMENTO_DELETE AFTER DELETE ON ITENS_NOTAS_FISCAIS
FOR EACH ROW BEGIN
	CALL sp_calcula_faturamento();
END $$
DELIMITER ;

SELECT *
FROM TAB_FATURAMENTO
WHERE 20190517;

############################################################################################

SELECT COUNT(CITY) INTO totalCity
FROM STATION;


SELECT COUNT(DISTINCT CITY) INTO totalDistinctCity
FROM STATION;

SELECT totalCity - totalCity;