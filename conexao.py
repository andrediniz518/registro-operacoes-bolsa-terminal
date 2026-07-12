import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sua_senha',
            database='seu_database'
        )
        if conexao.is_connected():
            #print('Conectado ao MySQL com sucesso!')
            return conexao
    except Error as erro:
        print(f'Erro ao conectar ao MySQL: {erro}')
        return None
