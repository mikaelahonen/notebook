import sqlite3
connection = sqlite3.connect('database.sqlite')
cursor = connection.cursor()
cursor.execute('CREATE TABLE data (key text, value text)')
cursor.execute('''INSERT INTO data VALUES ('key', 'value')''')
connection.commit()
connection.close()