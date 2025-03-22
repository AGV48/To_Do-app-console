# Lo importamos para ir limpiando la consola mientras el software se ejecuta
from os import system

# Se importa el modulo donde se realizarán los procesos
from todo_app.controladores.Controlador_Usuarios import Controlador_Usuarios
from todo_app.model.Usuario import Usuario

class Cambiar_Contrasena:
    # Metodo donde se realizará todo el proceso de cambio de contraseña
    def Asignar_Nueva_Contrasena():
        print("---------------------------------------------------------------------")
        print("                     To Do                 ")
        print("CAMBIO DE CONTRASEÑA")
        # Se obtienen los datos de entrada
        nombre = str(input("Por favor ingrese su nombre de usuario: "))
        contrasena = str(input("Por favor ingrese su nueva contraseña: "))
        print("-------------------------------------------------------------------------")
        # Se limpia la consola para que todo se vea organizado
        system("clear")

        #Se crea la instancia del usuario
        usuario = Usuario(nombre, contrasena)

        #Se cambia la contraseña del usuario en la base de datos
        Controlador_Usuarios.Actualizar_Usuario(nombre, usuario)
        # Se llama nuevamente al metodo de Bienvenida para reiniciar el proceso
        return