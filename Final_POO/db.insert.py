import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Libro'

titulo_libro = 'Cien años de soledad'
autor_libro = 'Gabriel Garcia'
ano_publicacion = '1985/05/20'


try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()


    insert_query = """INSERT INTO libros (titulo_libro, autor_libro, ano_publicacion)
                      VALUES (%s, %s, %s)"""

    li_data = (titulo_libro, autor_libro, ano_publicacion)

    cursor.execute(insert_query, li_data)

    # Confirmar la transacción
    conexion.commit()

    print("Nuevo empleado insertado correctamente.")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()