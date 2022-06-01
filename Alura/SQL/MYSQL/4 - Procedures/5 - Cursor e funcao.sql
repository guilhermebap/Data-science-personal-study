USE sucos_vendas;

SET GLOBAL LOG_BIN_TRUST_FUNCTION_CREATORS = 1;


DROP procedure IF EXISTS cursor_primeiro_contato;
DELIMITER $$

CREATE PROCEDURE `cursor_primeiro_contato` ()
BEGIN
  DECLARE vNome VARCHAR(50);
  DECLARE c CURSOR FOR SELECT NOME FROM tabela_de_clientes limit 4;
  OPEN c;
  FETCH c INTO vNome;
  SELECT vNome;
  FETCH c INTO vNome;
  SELECT vNome;
  FETCH c INTO vNome;
  SELECT vNome;
  FETCH c INTO vNome;
  SELECT vNome;
  CLOSE c;
END$$
DELIMITER ;

call cursor_primeiro_contato;

#################################################################

DROP procedure IF EXISTS cursor_looping;
DELIMITER $$

CREATE PROCEDURE `cursor_looping` ()
BEGIN
   DECLARE fim_do_cursor INT DEFAULT 0;
   DECLARE vNome VARCHAR(50);
   DECLARE c CURSOR FOR SELECT NOME FROM tabela_de_clientes;
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET fim_do_cursor = 1;
   
   OPEN c;
   WHILE fim_do_cursor = 0
   DO
       FETCH c INTO vNome;
       IF fim_do_cursor = 0 THEN
          SELECT vNome;
       END IF;
   END WHILE;
   CLOSE c;
END$$
DELIMITER ;

call cursor_looping;

################################################################

DROP procedure IF EXISTS looping_cursor_multiplas_colunas;
DELIMITER $$

USE sucos_vendas$$

CREATE PROCEDURE `looping_cursor_multiplas_colunas` ()
BEGIN
  DECLARE fim_do_cursor INT DEFAULT 0;
  DECLARE vCidade, vEstado, vCep VARCHAR(50);
  DECLARE vNome, vEndereco VARCHAR(150);
  DECLARE c CURSOR FOR
  SELECT nome, endereco_1, cidade, estado, cep FROM tabela_de_clientes;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET fim_do_cursor = 1;

  OPEN c;
  WHILE fim_do_cursor = 0
  DO
     FETCH c INTO vNome, vEndereco, vCidade, vEstado, vCep;
     IF fim_do_cursor = 0 THEN
        SELECT CONCAT(vNome, ' Endereço: ',
        vEndereco, ', ', vCidade , ' - ', vEstado, ' CEP: ' , vCep);
     END IF;
  END WHILE;
  CLOSE c;
END$$
DELIMITER ;

call looping_cursor_multiplas_colunas;

######################################################################

DROP FUNCTION IF EXISTS `f_acha_tipo_sabor`;
DELIMITER $$
USE sucos_vendas $$

CREATE FUNCTION `f_acha_tipo_sabor`(vSabor VARCHAR(50)) RETURNS varchar(20) CHARSET utf8mb4
BEGIN
  DECLARE vRetorno VARCHAR(20) default "";
  CASE vSabor
  WHEN 'Lima/Limão' THEN SET vRetorno = 'Cítrico';
  WHEN 'Laranja' THEN SET vRetorno = 'Cítrico';
  WHEN 'Morango/Limão' THEN SET vRetorno = 'Cítrico';
  WHEN 'Uva' THEN SET vRetorno = 'Neutro';
  WHEN 'Morango' THEN SET vRetorno = 'Neutro';
  ELSE SET vRetorno = 'Ácidos';
  END CASE;
  RETURN vRetorno;
END $$
DELIMITER ;

SELECT f_acha_tipo_sabor ("Laranja");

SELECT NOME_DO_PRODUTO, SABOR, f_acha_tipo_sabor (SABOR) as TIPO
FROM tabela_de_produtos;