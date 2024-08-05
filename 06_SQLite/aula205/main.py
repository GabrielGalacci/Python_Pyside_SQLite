import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Iniciando conexão
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD significa: Create  Read  Update Delete
# SQL:            INSERT SELECT UPDATE DELETE

# CUIDADO: Fazendo delete sem where, apaga toda a tabela, mas mantém os IDs
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Deleta a sequência de IDs, fazendo início do primeiro ID novamente.
# Delete cuidadoso, mas cuidado pra não utilizar um WHERE errado.
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


# SQL
# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# Cuidado: sql injection, o usuário que mecher na base de dados,
# poderia obter informações e mecher na tabela.
# cursor.executemany('') # Insere vários valores
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight) '
    'VALUES'
    '(:name, :weight)'
)
# cursor.execute(sql, ['Gabriel', 80]) # Executa apenas 1 comando
# cursor.executemany(sql, (('Gabriel', 80), ('Luiz', 68.9))) # Executa mais de um comando
# cursor.execute(sql, {'name': 'Gabriel', 'weight': 80})
cursor.executemany(sql, (
    {'name': 'Sem Nome', 'weight': 100},
    {'name': 'Gabriel', 'weight': 80},
    {'name': 'Julia', 'weight': 75},
    {'name': 'Marcio', 'weight': 90},
    {'name': 'Cristina', 'weight': 65}
))
# Toda vez que executar uma ação comitar as coisas para ficar tudo certo
connection.commit()


if __name__ == '__main__':
    print(sql)    
    
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"' # Integer não precisaria de aspas, por conveniência mantém
    )
    connection.commit()
    
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=60.65 '
        'WHERE id = "2"' # Integer não precisaria de aspas, por conveniência mantém
    )
    connection.commit()
    
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        print('ROW TUPLE: ', row)
        _id, name, weight = row
        print(f'ID:  {_id}, Name:  {name}, Weight: {weight}')
    
    # Desligar tudo após utilizar (MUITISSIMO IMPORTANTE)
    cursor.close()
    connection.close()
    