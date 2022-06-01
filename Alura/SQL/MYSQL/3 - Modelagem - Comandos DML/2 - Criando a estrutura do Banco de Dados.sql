CREATE DATABASE IF NOT EXISTS vendas_sucos;

USE vendas_sucos;

CREATE TABLE IF NOT EXISTS produtos (
codigo VARCHAR(10) NOT NULL,
descritor VARCHAR(100) NULL,
sabor VARCHAR(50) NULL,
tamanho VARCHAR(50) NULL,
embalagem VARCHAR(50) NULL,
preco_lista FLOAT NULL,
PRIMARY KEY(codigo));

DROP TABLE IF EXISTS vendedores;

CREATE TABLE IF NOT EXISTS vendedores (
matricula VARCHAR(5) NOT NULL,
nome VARCHAR(100) NULL,
bairro VARCHAR(50) NULL,
comissao FLOAT NULL,
data_adimissao DATE NULL,
ferias BIT(1) NULL,
PRIMARY KEY(matricula));

ALTER TABLE vendedores RENAME COLUMN data_adimissao TO data_admissao;

CREATE TABLE IF NOT EXISTS clientes(
CPF VARCHAR(11) NOT NULL,
nome VARCHAR(100) NOT NULL,
endereco VARCHAR(150) NULL,
bairro VARCHAR(50) NULL,
cidade VARCHAR(50) NULL,
estado VARCHAR(50) NULL,
CEP VARCHAR(8) NULL,
data_nascimento DATE NULL,
idade INT NULL,
sexo VARCHAR(1) NULL,
limite_credito FLOAT NULL,
volume_compra FLOAT NULL,
primeira_compra BIT(1) NULL,
PRIMARY KEY(CPF));

CREATE TABLE IF NOT EXISTS itens_notas(
numero VARCHAR(5) NOT NULL,
codigo VARCHAR(10) NOT NULL,
quantidade INT,
preco FLOAT,
PRIMARY KEY(numero, codigo));

CREATE TABLE IF NOT EXISTS vendas(
numero VARCHAR(5) NOT NULL,
data_venda DATE NULL,
CPF VARCHAR(11) NOT NULL,
matricula VARCHAR(5) NOT NULL,
imposto FLOAT NULL,
PRIMARY KEY(numero));

ALTER TABLE vendas ADD CONSTRAINT FK_clientes
FOREIGN KEY (CPF) 
REFERENCES clientes(CPF);

ALTER TABLE vendas ADD CONSTRAINT FK_vendedores
FOREIGN KEY (matricula) 
REFERENCES vendedores(matricula);

ALTER TABLE vendas RENAME notas;

ALTER TABLE itens_notas ADD CONSTRAINT FK_notas
FOREIGN KEY (numero) 
REFERENCES notas(numero);

ALTER TABLE itens_notas ADD CONSTRAINT FK_produtos
FOREIGN KEY (codigo) 
REFERENCES produtos(codigo);

