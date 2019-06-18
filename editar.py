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

        consulta = "UPDATE mascotas SET edad = %s WHERE id = %s;"
        nueva_edad = 5
        id_editar = 17
        cursor.execute(consulta, (nueva_edad, id_editar))

    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
except psycopg2.Error as e:
    print("Ocurrió un error al editar: ", e)
finally:
    conexion.close()
