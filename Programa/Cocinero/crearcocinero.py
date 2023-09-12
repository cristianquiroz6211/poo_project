import psycopg2

def crear_cocinero(conexion):
    nombre = input("Ingrese el nombre del cocinero: ")
    usuarioN = input("Ingrese el nombre de usuario del cocinero: ")
    contrasena = input("Ingrese la contraseña del cocinero: ")
    telefono = input("Ingrese el número de teléfono del cocinero: ")
    idEmpresa = input("Ingrese el ID de la empresa del cocinero: ")
    
    try:
        with conexion.cursor() as cursor:
            idRol = 3
            estado = True
            
            # Llama a la función para crear el cocinero en la base de datos
            sql = 'INSERT INTO "Usuarios" ("Nombre","Usuario","Contrasena","Telefono","Estado","IdRol","IdEmpresa") VALUES(%s,%s,%s,%s,%s,%s,%s);'
            cursor.execute(sql, (nombre, usuarioN, contrasena, telefono, estado, idRol, idEmpresa))
            
        conexion.commit()
        print("Cocinero creado exitosamente")
        return  # Regresa al punto de llamada de la función

    except psycopg2.Error as e:
        print(f"Error al crear cocinero: {str(e)}")
        return False
    
def DesactivarCocinero(conexion,usuario,estado):
    try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Usuarios" SET "Estado"=%s WHERE "Usuario"=%s;'
                cursor.execute(consulta,(estado,usuario))
            conexion.commit()
            print("Usuario desactivado")
            return True
    except psycopg2.Error as e:
        print("Error al desactivar usuario ", e)
        return False
