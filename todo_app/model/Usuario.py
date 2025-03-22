class Usuario:
    """
    Representa a un usuario del software
    """

    def __init__(self, nombre, contrasena):
        """
        Constructor de la clase Usuario
        
        Entradas:
        nombre (str): Nombre del usuario
        contrasena (str): Contraseña del usuario
        """
        self.nombre = nombre
        self.contrasena = contrasena

    def __repr__(self):
        """
        Método para retornar los datos del usuario
        """
        return str(self.nombre)

    def es_Igual(self, comparar_con):
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert(self.nombre == comparar_con.nombre)
        assert(self.contrasena == comparar_con.contrasena)