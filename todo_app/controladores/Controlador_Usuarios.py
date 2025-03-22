# Lo importamos para ir limpiando la consola mientras el software se ejecuta
from os import system

# Lo importamos para poder realizar las consultas en la base de datos
import psycopg2

# Se importa el modulo donde se realizarán los procesos
from todo_app.controladores import Secret_Config
from todo_app.model.Usuario import Usuario
from todo_app.model.Tarea import Tarea


class Controlador_Usuarios:

    # Todas las consultas se realizan mediante un cursor, por lo que se crea un método para obtenerlo
    def Obtener_Cursor():
        """
        Crea la conexión a la base de datos y retorna un cursor para ejecutar instrucciones
        """
        DATABASE = Secret_Config.PGDATABASE
        USER = Secret_Config.PGUSER
        PASSWORD = Secret_Config.PGPASSWORD
        HOST = Secret_Config.PGHOST
        PORT = Secret_Config.PGPORT
        #Se realiza la conexión con la base de datos
        connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

        # Se crea la variable donde se guardará el cursor que ejecutara las consultas
        cursor = connection.cursor()
        return cursor
    
    # Método para crear la tabla usuarios en la base de datos
    def Crear_Tabla_Usuarios():
        """ 
        Crea la tabla de usuarios en la BD 
        """
        try:
            #Se obtiene el cursor para tener la conexión con la base de datos
            cursor = Controlador_Usuarios.Obtener_Cursor()

            #Se ejecuta el query para crear la tabla en la base de datos
            cursor.execute("""create table usuarios (usuario varchar(50) not null primary key, 
                            contrasena varchar(30) not null)""")
            
            # Confirma los cambios realizados en la base de datos
            # Si no se llama, los cambios no quedan aplicados
            cursor.connection.commit()
            return
        except:
            #Si llega aquí es porque la tabla ya existe y no se pudo crear
            cursor.connection.rollback()
            return "Tabla Existente"
    
    # Método para crear la tabla de Tareas en la base de datos
    def Crear_Tabla_Tareas():
        """ 
        Crea la tabla de tareas en la BD 
        """
        try:
            #Se obtiene el cursor para tener la conexión con la base de datos
            cursor = Controlador_Usuarios.Obtener_Cursor()

            #Se ejecuta el query para crear la tabla en la base de datos
            cursor.execute("""
                    CREATE TABLE tareas (
                    titulo VARCHAR(100) NOT NULL,
                    descripcion VARCHAR(200) NOT NULL,
                    fecha_limite DATE NOT NULL,
                    prioridad prioridades NOT NULL,
                    usuario VARCHAR(50) REFERENCES usuarios(usuario) ON DELETE CASCADE,
                    PRIMARY KEY (titulo, usuario)
                           )""")
            
            # Confirma los cambios realizados en la base de datos
            # Si no se llama, los cambios no quedan aplicados
            cursor.connection.commit()
            return
        except:
            #Si llega aquí es porque la tabla ya existe y no se pudo crear
            cursor.connection.rollback()
            return "Tabla Existente"

    # Método para crear el tipo de prioridades en la base de datos
    def Crear_Prioridades():
        """ 
        Crea el tipo de prioridades en la base de datos 
        """
        try:
            # Se obtiene el cursor para tener la conexión con la base de datos
            cursor = Controlador_Usuarios.Obtener_Cursor()

            cursor.execute("""create type prioridades as enum('Alta', 'Media', 'Baja')""")

            cursor.connection.commit()
        except Exception as e:
            # Si ocurre algún error, revierte la transacción y devuelve un mensaje
            cursor.connection.rollback()
            return f"Error al crear el tipo de prioridades: {e}"

        return "Tipo Creado"

    # Método para insertar un usuario en la base de datos
    def Insertar_Usuario( usuario : Usuario ):
        """ 
        Inserta un usuario en la tabla de usuarios

        Entradas:
            usuario : Usuario -> Objeto de la clase Usuario con los datos del usuario a insertar
        """
        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        # Se realizan las verificaciones de que todos los campos ingresados sean correctos
        Controlador_Usuarios.verificarValores_vacios(usuario.nombre, usuario.contrasena)
        Controlador_Usuarios.verificarContrasena(str(usuario.contrasena))
        Controlador_Usuarios.verificarExistenciaUsuario_Insercion(usuario.nombre)
        
        # Si todas las verificaciones fueron exitosas, se inserta en usuario en la base de datos
        cursor.execute(f"""insert into usuarios (usuario, contrasena) values ('{usuario.nombre}', '{usuario.contrasena}')""")

        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

        # Se limpia la consola para que todo se vea organizado
        system("clear")
        print("USUARIO CREADO CORRECTAMENTE")
        print("\n")
    
    # Método para buscar usuarios en la base de datos y ver si existen
    def Buscar_Usuario( usuario_buscado ):
        """ 
        Trae un usuario de la tabla de usuarios por el nombre

        Entradas:
            usuario_buscado : str -> Nombre del usuario a buscar
        """
        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        #Se ejecuta el query para buscar el usuario por su cédula
        cursor.execute(f"""select usuario from usuarios where usuario = '{usuario_buscado}'""" )

        # Condicionar para validar si el usuario se encontró en la base de datos
        if cursor.fetchone() ==  None:
            # Si el usuario no existe, retorna FALSE
            return False
        else:
            # Si el usuario si existe, retorna TRUE
            return True

    # Método para actualizar la contraseña de un usuario
    def Actualizar_Usuario( usuario_buscado, datos_actualizar: Usuario ):
        """ 
        Trae un usuario de la tabla de usuarios y actualiza sus valores

        Entradas:
            usuario_buscado : str -> Nombre del usuario a buscar
            datos_actualizar : Usuario -> Objeto de la clase Usuario con los datos a actualizar
        """
        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()
        
        # Se realizan las verificaciones de que todos los campos ingresados sean correctos
        Controlador_Usuarios.verificarValores_vacios(datos_actualizar.nombre, datos_actualizar.contrasena)
        Controlador_Usuarios.verificarContrasena(datos_actualizar.contrasena)
        Controlador_Usuarios.verificarExistenciaUsuario_Actualizacion(usuario_buscado)
        
        # Si todas las verificaciones fueron exitosas, se inserta en usuario en la base de datos
        cursor.execute(f"""update usuarios set contrasena = '{datos_actualizar.contrasena}' where usuario = '{usuario_buscado}'""")

        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

        # Se limpia la consola para que todo se vea organizado
        system("clear")
        print("CONTRASEÑA ACTUALIZADA CORRECTAMENTE")

    # Método para iniciar sesión en el software
    def Iniciar_Sesión(usuario):
        """
        Inicia sesión en el software si el usuario y la contraseña son correctos

        Entradas:
            usuario : Usuario -> Objeto de la clase Usuario con los datos del usuario a iniciar sesión
        """
        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        # Se realizan las verificaciones de que todos los campos ingresados sean correctos
        Controlador_Usuarios.verificarValores_vacios(usuario.nombre, usuario.contrasena)

        #Se ejecuta el query para buscar el usuario y la contraseña en la base de datos
        cursor.execute(f"""select usuario, contrasena from usuarios where usuario = '{usuario.nombre}' and contrasena = '{usuario.contrasena}'""" )

        # Condicionar para validar si el usuario y la contraseña son correctos y están en la base de datos
        if cursor.fetchone() ==  None:
            # Si estos datos son incorrectos, retorma un TRUE
            return True
        else:
            # Si estos datos son correctos, retorma un FALSE
            return False

    # Método para insertar una tarea en la base de datos
    def Insertar_Tarea(tarea, usuario):
        """
        Inserta una tarea en la base de datos
        
        Entradas:
            tarea : Tarea -> Objeto de la clase Tarea con los datos de la tarea a insertar
            usuario : str -> Nombre del usuario al que pertenece la tarea
        """
        # Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        try:
            # Inserta la tarea con la categoría especificada o 'General'
            cursor.execute(
                f"""INSERT INTO tareas (titulo, descripcion, fecha_limite, prioridad, usuario) 
                    VALUES ('{tarea.titulo}', '{tarea.descripcion}', '{tarea.fecha_limite}', '{tarea.prioridad}', '{usuario}')"""
            )

            # Confirma los cambios realizados en la base de datos
            cursor.connection.commit()
            print("Tarea creada exitosamente")

        except Exception as e:
            cursor.connection.rollback()
            print(f"Error al crear la tarea: {e}")

    # Método para listar todas las tareas de un usuario
    def Listar_Tareas(usuario: Usuario):
        """ 
        Devuelve todas las tareas creadas por un usuario específico

        Entradas:
            usuario : Usuario -> Objeto de la clase Usuario con los datos del usuario a buscar
        """

        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        # Se ejecuta el query para traer todas las tareas de un usuario
        cursor.execute(f"SELECT titulo, descripcion, fecha_limite, prioridad FROM tareas WHERE usuario = '{usuario.nombre}'")

        # Se guardan todas las tareas en una variable
        tareas = cursor.fetchall()

        # Se retorna la lista de tareas
        return tareas

    # Método para eliminar una tarea de la base de datos
    def Eliminar_Tarea(titulo, usuario: Usuario):
        """
        Elimina una tarea de la base de datos
        
        Entradas:
            titulo : str -> Título de la tarea a eliminar
            usuario : Usuario -> Objeto de la clase Usuario con los datos del usuario a buscar
        """

        #Se obtiene el cursor para tener la conexión con la base de datos
        cursor = Controlador_Usuarios.Obtener_Cursor()

        try:
            # Elimina la tarea solo si pertenece al usuario indicado
            cursor.execute(f"DELETE FROM tareas WHERE titulo = '{titulo}' AND usuario = '{usuario.nombre}'")

            # Confirma los cambios realizados en la base de datos
            cursor.connection.commit()
            print(f"TAREA '{titulo}' ELIMINADA CORRECTAMENTE")

        except Exception as e:
            # En caso de error, revierte la transacción
            cursor.connection.rollback()
            print(f"Error al eliminar la tarea: {e}")

    # Verifica que ningún campo haya quedado vació
    def verificarValores_vacios(nombre, contrasena):
        if nombre == "" or contrasena == "":
            raise Exception("ERROR: No pueden haber campos vacios")
    
    # Verifica que la contraseña cumpla con la cantidad minima de caracteres
    def verificarContrasena(contrasena):
        if len(contrasena) < 8:
            raise Exception("ERROR: La contraseña debe tener minimo 8 caracteres")
        
    # Verifica que el usuario no exista en la base de datos para poder insertarlo
    def verificarExistenciaUsuario_Insercion(nombre):
        usuario_existe = Controlador_Usuarios.Buscar_Usuario(nombre)
        if usuario_existe:
            raise Exception("ERROR: Ya existe un usuario con ese nombre")
        
    # Verifica que el usuario exista en la base de datos para poder cambiar su contraseña
    def verificarExistenciaUsuario_Actualizacion(nombre):
        usuario_existe = Controlador_Usuarios.Buscar_Usuario(nombre)
        if not usuario_existe:
            raise Exception("ERROR: El usuario buscado no existe")