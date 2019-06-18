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
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT id, nombre, edad FROM mascotas;")

        # Con fetchall traemos todas las filas
        mascotas = cursor.fetchall()

        # Recorrer e imprimir
        for mascota in mascotas:
            print(mascota)
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
