import psycopg2

class Usuario():
    id = ""
    nombre = ""
    apellido = ""
    docummento = ""

    def __init__(self,nombre,apellido,docummento):
        self.nombre = nombre
        self.apellido =apellido
        self.docummento = docummento

    #Metodo crearUsuario
    def crearUsuarios(self, conexion, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                consulta = 'INSERT INTO "Usuario" ("Nombre","Apellido") VALUES(%s,%s);'
                cursor.execute(consulta,(nombre,apellido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al crear usuario ", e)
            return False

    #Metodo EliminarUsuario
    def EliminarUsuarios(self, conexion, id):
        try:
            with conexion.cursor() as cursor:
                consulta = 'DELETE FROM "Usuario" WHERE "Id" = %s;'
                cursor.execute(consulta,(id))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al eliminar usuario ", e)
            return False
    
    #Metodo Consultar
    def consulta(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM "Usuario";'
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                print(resultado)
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al eliminar usuario ", e)
            return False
    
        
    #Metodo Actualizar
    def ActualizarUsario(self, conexion, id, nombre, apellido):
        try:
            with conexion.cursor() as cursor:
                consulta = 'UPDATE "Usuario" SET "Nombre" = %s, "Apellido" = %s WHERE "Id" = %s;'
                cursor.execute(consulta,(nombre,apellido,id))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error al actualizar usuario ", e)
            return False

