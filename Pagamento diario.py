import mysql.connector
from datetime import datetime

# --- 1. CONECTAR AO BANCO DE DADOS ---
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="diagramar"
)

cursor = conexao.cursor()

# --- 2. PEGAR NÚMEROS DO USUÁRIO ---
numeros = []

print("Digite os números que deseja somar (digite 'fim' para encerrar):")

while True:
    entrada = input("Número: ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Valor inválido, tente novamente.")

# --- 3. CALCULAR A SOMA ---
soma_total = sum(numeros)

print(f"\nVocê digitou {len(numeros)} números.")
print(f"A soma total é: {soma_total}")

# --- 4. CALCULAR O PAGAMENTO DIARIO ---
dia_reg = datetime.now().strftime("%Y-%m-%d")

if soma_total >= 15000 and soma_total <= 16500:
    pagamento_diario = soma_total * 0.12
else:
    pagamento_diario = soma_total * 0.10

# --- 7. SALVAR NO BANCO ---

sql_diaria = "INSERT INTO tbl_pagamento_diario (data_dia, valor_dia) VALUES (%s, %s)"
cursor.execute(sql_diaria, (dia_reg, pagamento_diario))
conexao.commit()

print(f"Soma dos pagamentos diários de {dia_reg}: R${pagamento_diario:.2f}")

sql_paginas = "INSERT INTO tbl_paginas (soma_pag, data_reg) VALUES (%s, %s)"
valores = (soma_total,dia_reg,)

cursor.execute(sql_paginas, valores)
conexao.commit()

print("\nResultado salvo no banco de dados com sucesso!")

# --- 8. FECHAR CONEXÃO ---
cursor.close()
conexao.close() 
