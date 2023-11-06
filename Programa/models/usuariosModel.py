#Modelo Para Los Usuarios
import psycopg2

class UsuariosModel():
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    #Metodo para obtener los usuarios por Usuario
    def obtener_usuarios_por_usuario(self, usuario):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM "Usuarios" WHERE "Usuario" = %s', (usuario,))
            user_data = cursor.fetchone()
            usuarios = [{"IdUsuario": row[0], "Nombre": row[1], "Usuario": row[2], "Contrasena": row[3], "Telefono": row[4], "Estado": row[5], "IdRol": row[6], "IdEmpresa": row[7]} for row in user_data]
            return usuarios
            cursor.close()
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return False
    
    #Metodo para obtener los usuarios por IdUsuario
    def obtener_usuarios_por_idusuario(self, idusuario):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM "Usuarios" WHERE "IdUsuario" = %s', (idusuario,))
            user_data = cursor.fetchone()
            usuarios = [{"IdUsuario": row[0], "Nombre": row[1], "Usuario": row[2], "Contrasena": row[3], "Telefono": row[4], "Estado": row[5], "IdRol": row[6], "IdEmpresa": row[7]} for row in user_data]
            return usuarios
            cursor.close()
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return False

    #Metodo para obtener el rol de un usuario
    def obtener_rol_por_usuario(self, usuario):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "IdRol" FROM "Usuarios" WHERE "Usuario" = %s', (usuario,))
            user_data = cursor.fetchone()
            rol = user_data[0]
            return rol
            cursor.close()
        except Exception as e:
            print(f"Error al obtener rol: {e}")
            return False
