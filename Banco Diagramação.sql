CREATE DATABASE Diagramar;
USE Diagramar;

CREATE TABLE tbl_paginas (
id_pag INT auto_increment primary key,
soma_pag INT NOT NULL,
data_reg VARCHAR(50)
);

CREATE TABLE tbl_pagamento_mensal (
id_paga_mes INT AUTO_INCREMENT PRIMARY KEY,
valor_mes DECIMAL(10,2),
mes_paga VARCHAR(50)
);

CREATE TABLE tbl_pagamento_diario (
id_paga_dia INT AUTO_INCREMENT PRIMARY KEY,
valor_dia DECIMAL(10,2),
data_dia VARCHAR(50),
id_mensal INT,
FOREIGN KEY (id_mensal) REFERENCES tbl_pagamento_mensal(id_paga_mes)
);