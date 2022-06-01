USE vendas_sucos;

CREATE TABLE tb_faturamento(
data_venda DATE NULL,
total_venda float);

SELECT *
FROM tb_faturamento;

DELIMITER //
CREATE TRIGGER tg_calcula_faturamento_insert AFTER INSERT ON itens_notas
FOR EACH ROW BEGIN
	DELETE FROM tb_faturamento;
    INSERT INTO tb_faturamento
    SELECT A.data_venda, SUM(B.quantidade * B.preco) AS total_venda
    FROM notas AS A
    INNER JOIN itens_notas AS B
    ON A.numero = B.numero
    GROUP BY A.data_venda;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER tg_calcula_faturamento_delete AFTER DELETE ON itens_notas
FOR EACH ROW BEGIN
	DELETE FROM tb_faturamento;
    INSERT INTO tb_faturamento
    SELECT A.data_venda, SUM(B.quantidade * B.preco) AS total_venda
    FROM notas AS A
    INNER JOIN itens_notas AS B
    ON A.numero = B.numero
    GROUP BY A.data_venda;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER tg_calcula_faturamento_update AFTER UPDATE ON itens_notas
FOR EACH ROW BEGIN
	DELETE FROM tb_faturamento;
    INSERT INTO tb_faturamento
    SELECT A.data_venda, SUM(B.quantidade * B.preco) AS total_venda
    FROM notas AS A
    INNER JOIN itens_notas AS B
    ON A.numero = B.numero
    GROUP BY A.data_venda;
END//
DELIMITER ;

INSERT INTO NOTAS (NUMERO, DATA_VENDA, CPF, MATRICULA, IMPOSTO)
VALUES ('0100', '2019-05-08', '1471156710' , '235', 0.10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0100', '1000889', 100, 10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0100', '1002334', 100, 10);


INSERT INTO NOTAS (NUMERO, DATA_VENDA, CPF, MATRICULA, IMPOSTO)
VALUES ('0101', '2019-05-08', '1471156710' , '235', 0.10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0101', '1000889', 100, 10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0101', '1002334', 100, 10);


INSERT INTO NOTAS (NUMERO, DATA_VENDA, CPF, MATRICULA, IMPOSTO)
VALUES ('0103', '2019-05-08', '1471156710' , '235', 0.10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0103', '1000889', 100, 10);

INSERT INTO ITENS_NOTAS (NUMERO, CODIGO, QUANTIDADE, PRECO)
VALUES ('0103', '1002334', 100, 10);

SELECT *
FROM itens_notas;

UPDATE itens_notas
SET quantidade = 300, preco = 20
WHERE numero = 0101 AND codigo=1000889;

UPDATE itens_notas
SET quantidade = 2000
WHERE numero = 0100 AND codigo=1000889;

SELECT *
FROM tb_faturamento;

