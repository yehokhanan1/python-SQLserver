import pyodbc
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=KHANAN\SQLEXPRESS;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = int(input("Qual ID da venda?\nR:"))
cliente = str(input("Qual nome do cliente?\nR: "))
produto = str(input("Qual nome do produto?\nR: "))
data = str(input("Qual data de venda?\nR: "))
preco = float(input("Qual preço do produto?\nR: "))
quantidade = int(input("Qual quantidade?\nR: "))

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""
tabela = pd.read_sql('select cliente from vendas', conexao)
print(tabela)

cursor.execute(comando)
cursor.commit()