def inactivo(conexion, usuario_id):  #los usuarios no se eliminan, quedan inactivos
    try:
        # Actualiza el estado del usuario a inactivo en la base de datos.
        sql = "UPDATE usuarios SET estado = False WHERE id = %s;"
        conexion.cursor.execute(sql, (usuario_id,))
        conexion.conn.commit()
        return True
    except Exception as e:
        conexion.conn.rollback()
        print(f"Error al cambiar estado del usuario: {str(e)}")
        return False