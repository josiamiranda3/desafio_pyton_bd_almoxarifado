CREATE DATABASE db_almoxarifado;

USE db_almoxarifado;

drop database db_almoxarifado;

CREATE TABLE Grupo (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    codigo_grupo VARCHAR(50) NOT NULL,
    denominacao_grupo VARCHAR(100) NOT NULL
);

CREATE TABLE ItemAlmoxarifado (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    codigo_item VARCHAR(50) NOT NULL,
    denominacao_item VARCHAR(1000) NOT NULL,
    unidade_medida VARCHAR(1000) NOT NULL,
    id_grupo INT,
    FOREIGN KEY (id_grupo) REFERENCES Grupo(id_grupo)
);

SELECT * FROM Grupo;

SELECT * FROM ItemAlmoxarifado;

