# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'users'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

# No create table do MySQL não é necessário uilizar commit pois depois de
# executado não há como voltar atrás.
# IF NOT EXISTS é utilizado para não dar erro por tentar criar uma tabela
# que já exista
# PODE-SE ABRIR VÁRIOS CURSORES MAS NÃO VÁRIAS CONEXÕES
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY(id) '
            ') '
        )
        
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    
#-----------------------------------------------------------------------------
    # Começo a manipular dados a partir daqui
    # Inserindo valores
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            # PlaceHolders para precaver SQL Injection
            'VALUES (%s, %s) '
        )
        data = ('Gabriel', 30)
        cursor.execute(sql, data)
    connection.commit()
    
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            # PlaceHolders para dicionários (precave SQL Injection)
            'VALUES (%(name)s, %(age)s) '
        )
        # Com dicionário a ordem de entrada não faz diferença.
        # Nesse caso é utilizada a referência da tabela
        data2 = {
            "age": 27,
            "name": "Maria",
        }
        cursor.execute(sql, data2)
    connection.commit()
    
# ----------------------------------------------------------------------------
    # Criando vários registros de uma vez
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            # PlaceHolders para dicionários (precave SQL Injection)
            'VALUES (%(name)s, %(age)s) '
        )
        # Com dicionário a ordem de entrada não faz diferença.
        # Nesse caso é utilizada a referência da tabela
        data3 = (
            {"name": "Karina", "age": 32},
            {"name": "Samara", "age": 35},
            {"name": "João", "age": 40},
        )
        cursor.executemany(sql, data3)
    connection.commit()
    
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            # PlaceHolders para tuplas (precave SQL Injection)
            'VALUES (%s, %s) '
        )
        # Tupla de Tuplas
        data4 = (
            ("Siri", 12, ),
            ("Cortana", 15, ),
        )
        cursor.executemany(sql, data4)
    connection.commit()
    
 #----------------------------------------------------------------------------   
    # Ler valores da base de dados com SELECT
    with connection.cursor() as cursor:
        # SQL
        # lowest_id = int(input('Digite o menor id: '))
        # biggest_id = int(input('Digite o maior id: '))
        lowest_id = 2
        biggest_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (lowest_id, biggest_id))   
        # Colocando em uma variável é possível reutilizar quantas vezes quiser
        # Se usar o fetchall direto no for o iterator é esgotado     
        data5 = cursor.fetchall()
        
        # for row in data5:
        #     print(row)

#-----------------------------------------------------------------------------
    # Excluir valores da base de dados com DELETE e WHERE
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (4, ))
        connection.commit()
        
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')   
        
        # for row in cursor.fetchall():
        #     print(row)

#-----------------------------------------------------------------------------
    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        # SQL
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
        )
        cursor.execute(sql, ("José", 50, 6))
        connection.commit()
        
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        
        data6 = cursor.fetchall()
        
        # print('For 1: ')
        for row in data6:
            print(row)
        
        # Para consulta de detalhes de consultas executadas (Aula 416)
        print('resultFromSelect: ', resultFromSelect)
        print('len: ', len(data6))
        print('Row COunt: ', cursor.rowcount)
        print('Row Number: ', cursor.rownumber)

        # print()
        # print('For 2: ')
        # # cursor.scroll(3, 'absolute')
        # # cursor.scroll(-4)
        # # cursor.scroll(2)
        # for row in cursor.fetchall():
        #     print(row)
        
'''
Para mais informações sobre SSCursor e SSDictCursor, aula 415 da udemy
são usados para uma quantidade grande de dados, é um cursor que necessita
de menos memória pois ele não guarda as informações na memória e é possível
utilizar para dividir a quantidade de dados.
'''
