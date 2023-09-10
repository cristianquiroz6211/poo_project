import psycopg2

class Consulta():
    id = ""
    nombre = ""
    usuario = ""
    contrasena = ""
    telefono = ""
    estado = True
    idRol = ""
    idEmpresa = ""

    def __init__(self,nombre,usuario,contrasena,telefono,estado,idRol,idEmpresa):
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.telefono = telefono
        self.estado = estado
        self.idRol = idRol
        self.idEmpresa = idEmpresa

    #Metodo crearUsuario

    def crearUsuarios(self, conexion, nombre,usuario,contrasena,telefono,estado,idRol,idEmpresa):
        try:
            with conexion.cursor() as cursor:
                consulta = 'INSERT INTO "Usuarios" ("Nombre","Usuario","Contrasena","Telefono","Estado","IdRol","IdEmpresa") VALUES(%s,%s,%s,%s,%s,%s,%s);'
                cursor.execute(consulta,(nombre,usuario,contrasena,telefono,estado,idRol,idEmpresa))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al crear usuario ", e)
            return False


    def consultarCredenciales(self,conexion,usuario,contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "Usuario","Contrasena" FROM "Usuarios" WHERE "Usuario"=%s AND "Contrasena"=%s;'
                cursor.execute(consulta,(usuario,contrasena))
                if cursor.rowcount > 0:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("Error al consultar usuario ", e)
            return False