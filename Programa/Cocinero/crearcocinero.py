class Cocinero:
    def __init__(self, conexion):
        self.conexion = conexion

    def crear_cocinero(self, nombre, usuarioN, contrasena, telefono, idEmpresa):
        try:
            idRol = 3  
            estado = True  

            # Llama a la función para crear el cocinero en la base de datos
            sql = "INSERT INTO usuarios (nombre, usuario, contrasena, telefono, estado, id_rol, id_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;"
            self.conexion.cursor.execute(sql, (nombre, usuarioN, contrasena, telefono, estado, idRol, idEmpresa))
            id_cocinero = self.conexion.cursor.fetchone()[0]
            self.conexion.conn.commit()
            return id_cocinero
        except Exception as e:
            self.conexion.conn.rollback()
            print(f"Error al crear cocinero: {str(e)}")
            return None
