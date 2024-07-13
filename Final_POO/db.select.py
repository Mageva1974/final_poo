import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Libro'

try:

    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()

    select_query = "SELECT * FROM libros"
    cursor.execute(select_query)

    libros = cursor.fetchall()

    for libro in libros:
        print(libro)

except mysql.connector.Error as error:
    print("Error al obtener los empleados:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
