Proyecto de Workana de Aplicacion de Ventas

Para correr necesita: python3.10, poetry, un mysql funcionando.
Primer Paso:
    - en el directorio aplicacion_ventas debe correrse 'poetry install'

    - luego hay que copiar el archivo env.sample y renombrarlo con .env
    - Cambiar el contenido de .env por las variables correspondientes del mysql
    -- para el caso de MYSQL_DATABASE debe apuntar a una database vacia
    -- para el caso del usuario y password debe tener todos los permisos necesarios
    ---por ejemplo: GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD, INDEX ON *.* TO 'app'@'localhost'
    -- para el caso de SECRET_KEY una clave secreta de alta entropia para validar los tokes
    - luego debe correrse 'poetry shell' para entrar al entorno virtual (esto debe repetirse cada vez)
    - luego correrse 'export PYTHONPATH=src' para seleccionar el pythonpath adecuado
    - luego correr 'alembic upgrade head' desde la carpeta src para crear las tablas en la base de datos
    -- en ubuntu puede ser necesario correr sudo apt-get install python3-pymysql si se tienen problemas
    - se puede ejecutar 'mypy .' para realizar el análisis estatico del proyecto
    - se puede ejecutar pytest para realizar los test unitarios
    - se puede ejecutar pre-commit para asegurar la consistencia con ruff
    - se puede correr python src.app.py para correr la aplicacion en localhost
    - se puede crear un usuario con python src/create_superuser.py
    - la documentacion se encuentra en /users/docs y /workers/docs con la app corriendo
    -- en .env es posible cambiar el puerto y el host en el que se corre la app
