from os import system
import sys
from datetime import datetime

# Importamos los módulos necesarios
from todo_app.controladores.Controlador_Usuarios import Controlador_Usuarios
from todo_app.model.Tarea import Tarea

class Aplicacion:
    """
    Clase que contiene los métodos para crear, ver y eliminar tareas
    """
    def Pagina_Principal(usuario):
        while True:
            print("---------------------------------------------------------------------")
            print("                     To Do                 ")
            print(f"Bienvenid@ {usuario}")
            print("1. Crear tarea")
            print("2. Ver tareas")
            print("3. Eliminar tarea")
            print("4. Salir")
            print("-------------------------------------------------------------------------")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Aplicacion.crear_tarea(usuario)
            if opcion == "2":
                Aplicacion.ver_tareas(usuario)
            if opcion == "3":
                Aplicacion.eliminar_tarea(usuario)
            elif opcion == "4":
                print("¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida, por favor intente de nuevo.")

    # Método para crear una tarea
    def crear_tarea(usuario):
        # Recolección de datos para la tarea
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        
        # Validación y captura de la fecha límite
        while True:
            fecha_limite_str = input("Ingrese la fecha límite (YYYY-MM-DD): ")
            try:
                fecha_limite = datetime.strptime(fecha_limite_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Fecha inválida, intente de nuevo.")
        
        # Captura de la prioridad
        prioridad = input("Ingrese la prioridad de la tarea (Alta, Media, Baja): ")
        prioridad = prioridad.title()
        # Creación de la instancia de Tarea
        tarea = Tarea(titulo, descripcion, fecha_limite, prioridad)
        Controlador_Usuarios.Insertar_Tarea(tarea, usuario)
        print("\nTarea creada exitosamente:\n", tarea)

    # Método para ver las tareas
    def ver_tareas(usuario):
        system("clear")
        print("---------------------------------------------------------------------")
        print(f"                     TAREAS DE {usuario}                 ")
        tareas = Controlador_Usuarios.Listar_Tareas(usuario)
        print("Tareas:")
        for tarea in tareas:
            print(tarea)

    # Método para eliminar una tarea
    def eliminar_tarea(usuario):
        system("clear")
        tarea = input("Ingrese el título de la tarea que desea eliminar: ")
        Controlador_Usuarios.Eliminar_Tarea(tarea, usuario)