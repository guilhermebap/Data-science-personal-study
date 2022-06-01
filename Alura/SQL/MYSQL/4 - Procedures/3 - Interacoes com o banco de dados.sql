## Manipulando dados de banco de dados com Procedures

USE `sucos_vendas`;
DROP procedure IF EXISTS `manipulacao_dados`;
DELIMITER $$

USE `sucos_vendas`$$
CREATE PROCEDURE `manipulacao_dados` ()
BEGIN
	INSERT INTO tabela_de_produtos (CODIGO_DO_PRODUTO,NOME_DO_PRODUTO,SABOR,TAMANHO,EMBALAGEM,PRECO_DE_LISTA)
     VALUES ('2001001','Sabor da Serra 700 ml - Manga','Manga','700 ml','Garrafa',7.50),
         ('2001000','Sabor da Serra  700 ml - Melão','Melão','700 ml','Garrafa',7.50),
         ('2001002','Sabor da Serra  700 ml - Graviola','Graviola','700 ml','Garrafa',7.50),
         ('2001003','Sabor da Serra  700 ml - Tangerina','Tangerina','700 ml','Garrafa',7.50),
         ('2001004','Sabor da Serra  700 ml - Abacate','Abacate','700 ml','Garrafa',7.50),
         ('2001005','Sabor da Serra  700 ml - Açai','Açai','700 ml','Garrafa',7.50),
         ('2001006','Sabor da Serra  1 Litro - Manga','Manga','1 Litro','Garrafa',7.50),
         ('2001007','Sabor da Serra  1 Litro - Melão','Melão','1 Litro','Garrafa',7.50),
         ('2001008','Sabor da Serra  1 Litro - Graviola','Graviola','1 Litro','Garrafa',7.50),
         ('2001009','Sabor da Serra  1 Litro - Tangerina','Tangerina','1 Litro','Garrafa',7.50),
         ('2001010','Sabor da Serra  1 Litro - Abacate','Abacate','1 Litro','Garrafa',7.50),
         ('2001011','Sabor da Serra  1 Litro - Açai','Açai','1 Litro','Garrafa',7.50);

         SELECT * FROM tabela_de_produtos WHERE NOME_DO_PRODUTO LIKE 'Sabor da Serra%';
         UPDATE tabela_de_produtos SET PRECO_DE_LISTA = 8 WHERE NOME_DO_PRODUTO LIKE 'Sabor da Serra%';

         SELECT * FROM tabela_de_produtos WHERE NOME_DO_PRODUTO LIKE 'Sabor da Serra%';
         DELETE FROM tabela_de_produtos WHERE NOME_DO_PRODUTO LIKE 'Sabor da Serra%';

         SELECT * FROM tabela_de_produtos WHERE NOME_DO_PRODUTO LIKE 'Sabor da Serra%';
END$$
DELIMITER ;

Call manipulacao_dados;

####################################################################################
## Declarando variaveis dentro das procedures

USE `sucos_vendas`;
DROP procedure IF EXISTS `inclui_novo_produto`;
DELIMITER $$

USE `sucos_vendas`$$
CREATE PROCEDURE `inclui_novo_produto` ()
BEGIN
	DECLARE vCodigo varchar(50) DEFAULT '3000001';
	DECLARE vNome varchar(50) DEFAULT 'Sabor do Mar 700 ml - Manga';
	DECLARE vSabor varchar(50) DEFAULT 'Manga';
	DECLARE vTamanho varchar(50) DEFAULT '700 ml';
	DECLARE vEmbalagem varchar(50) DEFAULT 'Garrafa';
	DECLARE vPreco DECIMAL(10,2) DEFAULT 9.25;
	INSERT INTO tabela_de_produtos
	(CODIGO_DO_PRODUTO,NOME_DO_PRODUTO,SABOR,TAMANHO,EMBALAGEM,PRECO_DE_LISTA)
		 VALUES (vCodigo,
		 vNome,
		 vSabor,
		 vTamanho,
		 vEmbalagem,
		 vPreco);
END$$
DELIMITER ;

Call inclui_novo_produto;

####################################################################################
## Passando parametros para procedures e incluindo dados no bd

USE `sucos_vendas`;
DROP procedure IF EXISTS `inclui_novo_produto_parametro`;
DELIMITER $$

USE `sucos_vendas`$$
CREATE PROCEDURE `inclui_novo_produto_parametro`(vCodigo varchar(50),
vNome varchar(50), vSabor varchar(50), vTamanho varchar(50),
vEmbalagem varchar(50), vPreco DECIMAL(10,2))
BEGIN
	INSERT INTO tabela_de_produtos
	(CODIGO_DO_PRODUTO,NOME_DO_PRODUTO,SABOR,TAMANHO,EMBALAGEM,PRECO_DE_LISTA)
		 VALUES (vCodigo,
		 vNome,
		 vSabor,
		 vTamanho,
		 vEmbalagem,
		 vPreco);
END$$
DELIMITER ;

Call inclui_novo_produto_parametro('4000001', 'Sabor do Pantanal 1 Litro - Melancia',
'Melancia', '1 Litro', 'PET', 4.76);

####################################################################################
## Tratando erros

USE `sucos_vendas`;
DROP procedure IF EXISTS `inclui_novo_produto_parametro_2`;
DELIMITER $$

USE `sucos_vendas`$$
CREATE PROCEDURE `inclui_novo_produto_parametro_2`(vCodigo varchar(50),
vNome varchar(50), vSabor varchar(50), vTamanho varchar(50),
vEmbalagem varchar(50), vPreco DECIMAL(10,2))
BEGIN
	DECLARE mensagem VARCHAR(40);
	DECLARE EXIT HANDLER FOR 1062
	BEGIN
	   SET mensagem = 'Problema de Chave Primária !!!';
	   SELECT mensagem;
	END;

	INSERT INTO tabela_de_produtos
	(CODIGO_DO_PRODUTO,NOME_DO_PRODUTO,SABOR,TAMANHO,EMBALAGEM,PRECO_DE_LISTA)
		 VALUES (vCodigo,
		 vNome,
		 vSabor,
		 vTamanho,
		 vEmbalagem,
		 vPreco);
	SET mensagem = 'Produto incluido com sucesso !!!';
	SELECT mensagem;
END$$
DELIMITER ;

Call inclui_novo_produto_parametro_2('4000004', 'Sabor do Pantanal 1 Litro - Melancia',
'Melancia', '1 Litro', 'PET', 4.76);

####################################################################################
## Atribuindo valores a variaveis com o comando SELECT

USE `sucos_vendas`;
DROP procedure IF EXISTS `acha_sabor_produto`;
DELIMITER $$

USE `sucos_vendas`$$
CREATE PROCEDURE `acha_sabor_produto`(vProduto VARCHAR(50))
BEGIN
   DECLARE vSabor VARCHAR(50);
   SELECT SABOR INTO vSabor FROM tabela_de_produtos WHERE codigo_do_produto = vProduto;
   SELECT vSabor;
END$$
DELIMITER ;

Call acha_sabor_produto('1013793');

DROP PROCEDURE IF EXISTS Calcula_Idade;

DELIMITER $$
CREATE PROCEDURE `Calcula_Idade`()
BEGIN 
	DECLARE data_de_nascimento DATE DEFAULT '1990-01-30';
    SELECT TIMESTAMPDIFF(YEAR, data_de_nascimento, NOW()) AS Idade;
END$$
DELIMITER ;

CALL Calcula_idade;

DROP PROCEDURE IF EXISTS Reajuste_Comissao;
DELIMITER $$
CREATE PROCEDURE `Reajuste_Comissao`(vComissao FLOAT)
BEGIN
	UPDATE vendedores SET comissao =  comissao * (1 + vComissao);
END$$
DELIMITER ;



DROP PROCEDURE IF EXISTS Quantidade_Notas;

DELIMITER $$
CREATE PROCEDURE `Quantidade_Notas`(vData DATE)
BEGIN
	DECLARE numnotas INT;
    
    SELECT COUNT(*) INTO numnotas 
    FROM notas
    WHERE data_venda = vData;
    
    SELECT numnotas;
END$$
DELIMITER ;
	
CALL Quantidade_notas('2017-01-01');


