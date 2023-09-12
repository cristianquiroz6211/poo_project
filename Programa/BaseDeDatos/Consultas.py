import psycopg2

#Clase ConsultaUsuario
class ConsultaUsuario():
    id = ""
    nombre = ""
    usuario = ""
    contrasena = ""
    telefono = ""
    estado = True
    idRol = ""
    idEmpresa = ""
    Identificacion = ""
    idLocal = ""

    def __init__(self,nombre,usuario,contrasena,telefono,estado,idRol,idEmpresa,Identificacion,idLocal):
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.telefono = telefono
        self.estado = estado
        self.idRol = idRol
        self.idEmpresa = idEmpresa
        self.Identificacion = Identificacion
        self.idLocal = idLocal

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

    #Metodo consultarCredenciales
    def consultarCredenciales(self,conexion,usuario,contrasena,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "Usuario","Contrasena","Estado" FROM "Usuarios" WHERE "Usuario"=%s AND "Contrasena"=%s AND "Estado"=%s;'
                cursor.execute(consulta,(usuario,contrasena,estado))
                if cursor.rowcount > 0:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("Error al consultar credenciales ", e)
            return False

    #Metodo consultarRol
    def consultarRol(sel,conexion, usuario,contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "IdRol" FROM "Usuarios" WHERE "Usuario"=%s AND "Contrasena"=%s;'
                cursor.execute(consulta,(usuario,contrasena))
                if cursor.rowcount > 0:
                    for rol in cursor.fetchall():
                        return rol[0]
                else:
                    print("No hay registros")
        except psycopg2.Error as e:
            print("Error al consultar rol ", e)
            return False

    #Metodo consultarInformacion
    def consultarInformacion(self,conexion,usuario,contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "IdUsuario","Nombre","Usuario","Contrasena","Telefono","Estado","IdRol","IdEmpresa" FROM "Usuarios" WHERE "Usuario"=%s AND "Contrasena"=%s;'
                cursor.execute(consulta,(usuario,contrasena))
                if cursor.rowcount > 0:
                    for usuario in cursor.fetchall():
                        return usuario
                else:
                    print("No hay registros")
        except psycopg2.Error as e:
            print("Error al consultar informacion ", e)
            return False

    #Metodo DesactivarUsuario
    def desactivarUsuario(self,conexion,usuario,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Usuarios" SET "Estado"=%s WHERE "Usuario"=%s;'
                cursor.execute(consulta,(estado,usuario))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al desactivar usuario ", e)
            return False
    
    #Metodo ActivarUsuario
    def activarUsuario(self,conexion,usuario,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Usuarios" SET "Estado"=%s WHERE "Usuario"=%s;'
                cursor.execute(consulta,(estado,usuario))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al activar usuario ", e)
            return False
    
    #Metodo CrearEmpresa
    def crearEmpresa(self,conexion,empresa,identificacion,estado,IdLocal):
        try:
            with conexion.cursor() as cursor:
                consulta = 'INSERT INTO "Empresas" ("Empresa","Identificacion","Estado","IdLocal") VALUES(%s,%s,%s,%s);'
                cursor.execute(consulta,(empresa,identificacion,estado,IdLocal))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al crear empresa ", e)
            return False
    #Metodo desactivarEmpresa
    def desactivarEmpresa(self,conexion,empresa,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Empresas" SET "Estado"=%s WHERE "Empresa"=%s;'
                cursor.execute(consulta,(estado,empresa))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al desactivar empresa ", e)
            return False
    
    #Metodo activarEmpresa
    def activarEmpresa(self,conexion,empresa,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Empresas" SET "Estado"=%s WHERE "Empresa"=%s;'
                cursor.execute(consulta,(estado,empresa))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al activar empresa ", e)
            return False
    
    #Metodo MostrarEmpresas
    def mostrarEmpresas(self,conexion,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "Empresa","IdLocal" FROM "Empresas" WHERE "Estado"=%s;'
                cursor.execute(consulta,(estado,))
                if cursor.rowcount > 0:
                    for empresa in cursor.fetchall():
                        print(empresa)
                else:
                    print("No hay registros")
        except psycopg2.Error as e:
            print("Error al mostrar empresas ", e)
            return False
    
    #Metodo MostarUsuarios
    def mostrarUsuarios(self,conexion,estado):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT "Nombre","Usuario","Telefono","IdRol","IdEmpresa" FROM "Usuarios" WHERE "Estado"=%s;'
                cursor.execute(consulta,(estado,))
                if cursor.rowcount > 0:
                    for usuario in cursor.fetchall():
                        print(usuario)
                else:
                    print("No hay registros")
        except psycopg2.Error as e:
            print("Error al mostrar usuarios ", e)
            return False