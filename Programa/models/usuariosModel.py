#Modelo Para Los Usuarios
import psycopg2

class UsuariosModel():
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432        )
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
    
        #Metodo que me traiga todos los pedidos que ya estan finalizados
    def obtener_pedidos_finalizados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM "Pedidos" WHERE "IdEstado" = %s', (4,))
            pedidos_data = cursor.fetchall()
            pedidos = [{"IdPedido": row[0],"Precio": row[1], "FechaYHora":row[2]} for row in pedidos_data]
            return pedidos
            cursor.close()
        except Exception as e:
            print(f"Error al obtener pedidos: {e}")
            return False
    
    #Metodo para insertar un nuevo usuario
    def insertar_usuario(self, nombre, usuario, contrasena, telefono, estado, idrol, idempresa):
        try:
            #pasar de string a int
            idrol = int(idrol)
            idempresa = int(idempresa)
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO "Usuarios" ("Nombre","Usuario","Contrasena","Telefono","Estado","IdRol","IdEmpresa") VALUES(%s,%s,%s,%s,%s,%s,%s)', (nombre, usuario, contrasena, telefono, estado, idrol, idempresa))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            return False

    def crear_cocinero(self):
        nombre = input("Ingrese el nombre del cocinero: ")
        usuarioN = input("Ingrese el nombre de usuario del cocinero: ")
        contrasena = input("Ingrese la contraseña del cocinero: ")
        telefono = input("Ingrese el número de teléfono del cocinero: ")
        idEmpresa = input("Ingrese el ID de la empresa del cocinero: ")
        
        try:
            with self.conn.cursor() as cursor:
                idRol = 3
                estado = True
                
                # Llama a la función para crear el cocinero en la base de datos
                sql = 'INSERT INTO "Usuarios" ("Nombre","Usuario","Contrasena","Telefono","Estado","IdRol","IdEmpresa") VALUES(%s,%s,%s,%s,%s,%s,%s);'
                cursor.execute(sql, (nombre, usuarioN, contrasena, telefono, estado, idRol, idEmpresa))
                
            self.conn.commit()
            print("Cocinero creado exitosamente")
            return  # Regresa al punto de llamada de la función

        except psycopg2.Error as e:
            print(f"Error al crear cocinero: {str(e)}")
            return False
        
