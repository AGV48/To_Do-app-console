class Tarea:
    """
    Representa una tarea del software
    """

    def __init__(self, titulo, descripcion, fecha_limite, prioridad):
        """
        Constructor de la clase Tarea

        Entradas:
            titulo (str): Título de la tarea
            descripcion (str): Descripción de la tarea
            fecha_limite (str): Fecha límite de la tarea
            prioridad (str): Prioridad de la tarea
        """
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad

    def __str__(self):
        """
        Método para retornar los datos de la tarea
        """
        return f"Tarea: {self.titulo}\nDescripción: {self.descripcion}\nFecha límite: {self.fecha_limite}\nPrioridad: {self.prioridad}\n"