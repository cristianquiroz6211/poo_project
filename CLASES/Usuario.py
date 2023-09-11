class Usuario:
    """
    Attributos:
        id (int): Identificador del usuario.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        numerocontacto (str): Número de contacto del usuario.
        RolUsuario (Rol): Rol del usuario.
    """

    def __init__(self, id, nombre, apellido, numerocontacto, RolUsuario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.numerocontacto = numerocontacto
        self.RolUsuario = RolUsuario


