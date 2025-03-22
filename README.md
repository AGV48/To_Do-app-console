# Proyecto To-Do en Python
## Descripción del Proyecto
Este proyecto es una aplicación de gestión de tareas (To-Do) desarrollada en Python. Permite a los usuarios crear, administrar y organizar tareas pendientes de manera eficiente. La aplicación utiliza una base de datos PostgreSQL para almacenar y gestionar la información de los usuarios y sus tareas.

## Autores
* Alejandro Gutiérrez Vallejo
* Tomás Ramírez Agudelo

## Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

- Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde `python.org`.

- Poetry: Este proyecto utiliza Poetry para la gestión de dependencias. Instálalo siguiendo las instrucciones en poetry's official website.

- PostgreSQL: Necesitarás una base de datos PostgreSQL. Puedes configurar una localmente o utilizar un servicio en la nube como Neon.tech.

## Configuración del Proyecto
1. Clonar el Repositorio
Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/AGV48/To_Do-app-console
```

2. Configurar la Base de Datos
Crear una Base de Datos en Neon.tech
Visita Neon.tech y crea una cuenta o inicia sesión.

- Crea un nuevo proyecto y dentro de él, una nueva base de datos.

- En la sección Dashboard, selecciona la opción Connect.

- Copia las credenciales de conexión (host, nombre de la base de datos, usuario, contraseña y puerto).

- Configurar SecretConfig.py
En la carpeta controladores, encuentra el archivo Secret_Config-sample.py.

- Renombra el archivo a SecretConfig.py.

- Abre el archivo y reemplaza los valores de las variables con las credenciales de tu base de datos:
```Python
    PGHOST = ' '  # Cambia ' ' por la dirección del host de tu base de datos.
    PGDATABASE = ' '  # Cambia ' ' por el nombre de tu base de datos.
    PGUSER = ' '  # Cambia ' ' por tu nombre de usuario de la base de datos.
    PGPASSWORD = ' '  # Cambia ' ' por tu contraseña de la base de datos.
    PGPORT = '5432'  # Normalmente es '5432' pero si en tu base de datos cambia, pegar el nuevo
```
3. Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias del proyecto:

```bash
poetry install
```
Ejecutar el Proyecto
Una vez configurado todo, puedes ejecutar la aplicación desde la consola, Navegando a la raíz del proyecto y ejecutando:

```bash
poetry run python app.py
```

## Estructura del Proyecto
El proyecto sigue una estructura modular y organizada para facilitar su mantenimiento y escalabilidad:

* controladores: Contiene la lógica para la conexión a la base de datos y las consultas SQL.

* model: Define los modelos de datos, como usuarios y tareas.

* consolas: Implementa la interfaz de usuario por consola para interactuar con la aplicación.