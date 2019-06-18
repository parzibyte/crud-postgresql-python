"""
    Conexión a PostgreSQL con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author parzibyte

    Más tutoriales en:
                        parzibyte.me/blog
"""
import psycopg2
from bd import conexion
try:
    with conexion.cursor() as cursor:

        consulta = "SELECT id, nombre, edad FROM mascotas WHERE edad > %s;"
        cursor.execute(consulta, (1,))

        # Con fetchall traemos todas las filas
        mascotas = cursor.fetchall()

        # Recorrer e imprimir
        for mascota in mascotas:
            print(mascota)
except psycopg2.Error as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexion.close()
