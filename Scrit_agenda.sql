-- CRIANDO UM BANCO DE DADOS
CREATE DATABASE AGENDA;
-- SELECIONADO UM BANCO DE DADOS
USE AGENDA;
-- CRIANDO TABELA NO BANCO DE DADOS
CREATE TABLE TB_PESSOAS(
COD INT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(30)NOT NULL UNIQUE,
ENDERECO VARCHAR(100),
TELEFONE VARCHAR(11) NOT NULL UNIQUE,
EMAIL VARCHAR(35)
);
-- MOSTRANDO AS TABELAS NO BANCO DE DADOS
SHOW TABLES;
-- DESCREVENDO A TABELA;
DESCRIBE TB_PESSOAS;
-- INSERINDO DASOS NA TABELA
INSERT INTO TB_PESSOAS (NOME,ENDERECO,TELEFONE,EMAIL) VALUES(
'PATRICIA',
'RUA ITAPIRANGA N412 C IPUTINGA RECIFE-PE',
'81999992222',
'patricia@gmail.com'
);
-- DELETANDO UMA TABELA
DROP TABLE TB_PESSOAS;
-- EXIBINDO DADOS DA TABELA
SELECT * FROM TB_PESSOAS;










