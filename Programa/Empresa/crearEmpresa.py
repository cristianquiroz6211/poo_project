
class GestionEmpresas:
    def __init__(self, conexion):
        self.conexion = conexion

    # Método para crear una empresa
    def crear_empresa(self, id_empresa, nombre_empresa, identificacion, id_local):
        try:
            # Inserta una nueva empresa en la base de datos.
            sql = "INSERT INTO empresas (id_empresa, nombre_empresa, identificacion, id_local) VALUES (%s, %s, %s, %s);"
            self.conexion.cursor.execute(sql, (id_empresa, nombre_empresa, identificacion, id_local))
            self.conexion.conn.commit()
            return True
        except Exception as e:
            self.conexion.conn.rollback()
            print(f"Error al crear la empresa: {str(e)}")
            return False
