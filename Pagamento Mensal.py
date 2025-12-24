import mysql.connector
from datetime import datetime

# --- 1. CONECTAR AO BANCO DE DADOS ---
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="seu_banco"
)

cursor = conexao.cursor()

mes_atual = datetime.now().strftime("%Y-%m")
ano, mes = mes_atual.split('-')
mes_anterior = int(mes) - 1 if int(mes) > 1 else 12
ano_anterior = int(ano) if int(mes) > 1 else int(ano) - 1
mes_fechar = f"{ano_anterior}-{mes_anterior:02d}"

print(f"Fechando o mês: {mes_fechar}")

# --- BUSCAR PAGAMENTOS DIÁRIOS ---

sql_soma = "SELECT SUM(valor_dia) FROM tbl_pagamento_diario WHERE DATE_FORMAT(data_dia, '%Y-%m') = %s AND id_mensal IS NULL"
cursor.execute(sql_soma, (mes_fechar,))
resultado = cursor.fetchone()[0] or 0

print(f"Soma dos pagamentos diários de {mes_fechar}: R${resultado:.2f}")

# --- INSERIR NA TABELA MENSAL ---

sql_insert = "INSERT INTO tbl_pagamento_mensal (mes_paga, valor_mes) VALUES (%s, %s)"
cursor.execute(sql_insert, (mes_fechar, resultado))
conexao.commit()

id_mensal = cursor.lastrowid

print(f"Pagamento mensal criado com ID {id_mensal}")

# LIGAR TODOS OS DIÁRIOS DO MÊS A ESSE ID

sql_update = "UPDATE tbl_pagamento_diario SET id_mensal = %s WHERE DATE_FORMAT(data_dia, '%Y-%m') = %s"
cursor.execute(sql_update, (id_mensal, mes_fechar))
conexao.commit()

print(f"Pagamentos diários de {mes_fechar} vinculados ao mensal ID {id_mensal}")

cursor.close()
conexao.close() 
