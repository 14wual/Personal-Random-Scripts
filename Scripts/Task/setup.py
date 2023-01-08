"""
import sqlite3

# Conecta con la base de datos
conn = sqlite3.connect("ddbb/task.db")

# Crea un cursor
cursor = conn.cursor()

# Crea la tabla
cursor.execute("CREATE TABLE ntasks (fecha TEXT, name TEXT(50), num TEXT, description TEXT(255))")

# Guarda los cambios
conn.commit()

# Cierra la conexión con la base de datos
conn.close()

"""

import sqlite3

# Conecta a la base de datos
conn = sqlite3.connect("ddbb/task.db")

# Crea un cursor para ejecutar consultas
cursor = conn.cursor()

# Define una lista con las tareas y sus datos
tasks = [
    ("8/1/2023", "Limpiar el jardín", "1", "Barrer las hojas secas y recoger la basura del jardín."),
    ("9/1/2023", "Ir al supermercado", "2", "Comprar los productos de la lista de la compra y hacer una parada en la panadería."),
    ("10/1/2023", "Lavar la ropa", "3", "Separar la ropa por colores y cargar la lavadora."),
    ("11/1/2023", "Pintar el salón", "4", "Preparar el salón para pintar y elegir el color adecuado para las paredes."),
    ("12/1/2023", "Llamar a la abuela", "5", "Llamar a la abuela para preguntarle cómo está y contarle cómo va todo."),
    ("13/1/2023", "Hacer ejercicio", "6", "Hacer una sesión de ejercicios en el gimnasio o salir a correr al aire libre."),
    ("14/1/2023", "Cocinar la cena", "7", "Preparar una cena saludable y equilibrada siguiendo una receta elegida."),
    ("15/1/2023", "Estudiar para el examen", "8", "Repasar los apuntes y hacer ejercicios para preparar el examen de la semana siguiente."),
    ("16/1/2023", "Hacer la compra online", "9", "Hacer la compra semanal por internet y elegir un día de entrega conveniente."),
    ("17/1/2023", "Organizar el armario", "10", "Vaciar el armario, doblar la ropa y colocarla de nuevo de forma ordenada."),
]

# Recorre la lista de tareas y las agrega a la tabla
for task in tasks:
    cursor.execute("INSERT INTO ntasks (fecha, name, num, description) VALUES (?, ?, ?, ?)", task)

# Guarda los cambios en la base de datos
conn.commit()

# Cierra la conexión con la base de datos
conn.close()
