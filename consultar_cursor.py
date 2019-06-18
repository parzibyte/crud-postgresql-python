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
        # Hacer un while, mientras fetchone no regrese None
        mascota = cursor.fetchone()
        while mascota:
            print(mascota)
            mascota = cursor.fetchone()
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
