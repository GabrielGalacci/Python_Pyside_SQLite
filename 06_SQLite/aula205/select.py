import sqlite3

from main import DB_FILE, TABLE_NAME

# Iniciando conexão
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 5') # LIMIT limita a quantidade de registros

# fetchone traz 1 registro, fetchmany tras varios registros
for row in cursor.fetchall():
    print('ROW TUPLE: ', row)
    _id, name, weight = row
    print(f'ID:  {_id}, Name:  {name}, Weight: {weight}')


# Quando executamos uma ação em um cursor ele é esgotado
# Por isso criamos um novo select
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

row = cursor.fetchone()
print('ROW TUPLE: ', row)
_id, name, weight = row
print(f'ID:  {_id}, Name:  {name}, Weight: {weight}')

# Desligar tudo após utilizar (MUITISSIMO IMPORTANTE)
cursor.close()
connection.close()
