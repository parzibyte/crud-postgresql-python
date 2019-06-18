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

        consulta = "DELETE FROM mascotas WHERE edad < %s;"
        # También podría ser sin where
        #consulta = "DELETE FROM mascotas"
        edad = 2
        cursor.execute(consulta, (edad,))

    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
except psycopg2.Error as e:
    print("Error eliminando: ", e)
finally:
    conexion.close()
