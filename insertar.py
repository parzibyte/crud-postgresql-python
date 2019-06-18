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
        consulta = "INSERT INTO mascotas(nombre, edad) VALUES (%s, %s);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Maggie", 3))
        cursor.execute(consulta, ("Capuchina", 2))
        cursor.execute(consulta, ("Guayaba", 2))
        cursor.execute(consulta, ("Panqué", 1))
        cursor.execute(consulta, ("Snowball", 1))
    conexion.commit()  # Si no haces commit, los cambios no se guardan

except psycopg2.Error as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()
