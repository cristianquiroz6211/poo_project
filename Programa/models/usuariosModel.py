#Modelo Para Los Usuarios
import psycopg2

class UsuariosModel():
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432        )
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

    def obtener_Empresas(self):
        # Muestra la empresa y su identificación
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "Empresa","Identificacion" FROM "Empresas"')
            user_data = cursor.fetchall()
            empresas = [{"Empresa": row[0], "Identificacion": row[1]} for row in user_data]
            cursor.close()
            return empresas
        except Exception as e:
            print(f"Error al obtener empresas: {e}")
            return False

    #Metodo que me traiga todos los pedidos que ya estan finalizados = 4 ."Pedidos" ("Precio", "FechaYHora", "IdMesa", "IdEstado", "IdMesero")
    def obtener_pedidos_finalizados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM "Pedidos" WHERE "IdEstado" = 4')
            user_data = cursor.fetchall()
            pedidos = [{"IdPedido": row[0], "Precio": row[1], "FechaYHora": row[2], "IdMesa": row[3], "IdEstado": row[4], "IdMesero": row[5]} for row in user_data]
            cursor.close()
            return pedidos
        except Exception as e:
            print(f"Error al obtener pedidos: {e}")
            return False
