
# Python y PostgreSQL: ejemplo de conexión y CRUD
Mira el tutorial en: [https://parzibyte.me/blog/2019/06/17/python-postgresql-ejemplo-conexion-crud/](https://parzibyte.me/blog/2019/06/17/python-postgresql-ejemplo-conexion-crud/)
## Requisitos y recomendaciones

Recuerda instalar Python y PIP en  [Linux](https://parzibyte.me/blog/2019/06/06/renombrar-python3-python-linux-ubuntu/)  o  [Windows](https://parzibyte.me/blog/2017/11/19/instalar-configurar-python-3-windows-10/), y también PostgreSQL en  [Windows](https://parzibyte.me/blog/2019/04/05/instalar-postgresql-11-windows/)  o  [Linux](https://parzibyte.me/blog/2019/06/05/instalar-postgresql-linux-ubuntu/).

Recomiendo  [crear un usuario y base de datos](https://parzibyte.me/blog/2019/06/17/agregar-usuario-base-de-datos-conceder-permisos-postgresql/)  para este ejercicio, o tener credenciales a la mano.

Una vez que tengas PIP, ejecuta lo siguiente para instalar  **Psycopg2**:

`pip install psycopg2`

Dentro del código vamos a encontrar el archivo  **credenciales_ejemplo.json**, el cual debemos copiar y renombrar a  **credenciales.json**  y dentro del mismo debemos poner los datos de acceso.

De esta manera puedes compartir tu código sin necesidad de pasar tus contraseñas y usuarios.