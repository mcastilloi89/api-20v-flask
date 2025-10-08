# api-20v-flask

1. `virtualenv .venv`
2. `source .venv/Scripts/activate`
3. `pip install -r requirements.txt`



api-20v-flask

Este proyecto es una aplicación Flask desarrollada a partir del repositorio base de jorgeav527/api-20v-flask.
La aplicación fue refactorizada para cumplir con todos los puntos solicitados en el enunciado del curso.

Instrucciones para ejecutar el proyecto

Crear el entorno virtual:
python -m venv .venv

Activar el entorno virtual:
..venv\Scripts\Activate.ps1

Instalar las dependencias:
pip install -r requirements.txt

Crear la base de datos (solo la primera vez):
python crear_tabla.py

Ejecutar la aplicación:
python main.py

Abrir en el navegador:
http://127.0.0.1:5000

Descripción general

La aplicación permite crear, listar, ver, editar y eliminar publicaciones (posts).
Está desarrollada en Flask con base de datos SQLite.
Se organizó el código en módulos para que sea más claro y fácil de mantener.

Estructura del proyecto

main.py → lógica principal de la aplicación Flask
post.py → contiene todas las funciones CRUD (crear, leer, actualizar, eliminar)
database.py → define una única función de conexión a la base de datos y su cierre
crear_tabla.py → script para crear la tabla “posts” en la base de datos
templates/ → contiene las vistas HTML
static/ → archivos CSS o imágenes
database.db → base de datos local que se genera automáticamente

Cumplimiento del enunciado

main.py no tiene código SQL directo.

Todas las consultas se hacen desde post.py.

Se valida que los campos title y content no estén vacíos.

Se devuelven mensajes claros al usuario usando flash().

Se agregó soporte JSON para los endpoints usando ?format=json.

Se mantienen los templates originales del proyecto base.

Modo JSON (opcional)

Para ver todos los posts en formato JSON:
curl "http://127.0.0.1:5000/posts?format=json
"

Para crear un post con JSON:
curl -X POST "http://127.0.0.1:5000/posts?format=json
" -H "Content-Type: application/json" -d "{"title":"Hola","content":"Este es un post de ejemplo"}"