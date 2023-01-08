import sqlite3

# Conecta con la base de datos
conn = sqlite3.connect("ddbb/task.db")

# Crea un cursor
cursor = conn.cursor()

# Ejecuta una consulta a la tabla "mi_tabla"
cursor.execute("SELECT * FROM mi_tabla")

# Recupera todos los resultados de la consulta
resultados = cursor.fetchall()

# Muestra los resultados
for fila in resultados:
    print(fila)

# Cierra la conexión con la base de datos
conn
