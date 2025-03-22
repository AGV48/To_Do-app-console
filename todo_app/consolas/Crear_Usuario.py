# Lo importamos para ir limpiando la consola mientras el software se ejecuta
from os import system

# Se importa el modulo donde se realizarán los procesos
from todo_app.controladores.Controlador_Usuarios import Controlador_Usuarios
from todo_app.model.Usuario import Usuario

class Crear_Usuario:
    """
    Clase que contiene el método para registrar un usuario
    """
    # Metodo donde se realizará todo el proceso de registro
    def Registrar_Usuario():
        print("---------------------------------------------------------------------")
        print("                     To Do                 ")
        print("DATOS PERSONALES")
        # Se obtienen los datos de entrada
        nombre = str(input("Por favor ingrese su nombre de usuario: "))
        contrasena = str(input("Por favor ingrese su contraseña: "))
        print("-------------------------------------------------------------------------")
        # Se limpia la consola para que todo se vea organizado
        system("clear")

        #Se crea la instancia del usuario
        usuario = Usuario(nombre, contrasena)

        #Se crea el usuario en la base de datos
        Controlador_Usuarios.Insertar_Usuario(usuario)
        # Se llama nuevamente al metodo de Bienvenida para reiniciar el proceso
        return