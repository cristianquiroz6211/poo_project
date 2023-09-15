from BaseDeDatos.ValidarConexion import *

class CRUDUsuario():  
    def crearUsuarios():
        nombre = input("Ingrese el nombre: ")
        usuarioN = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        telefono = input("Ingrese el telefono: ")
        print("Tipos de usuario: \n1. AdministradorGeneral  \n2. Administradorlocal \n3. Cocinero \n4. Mesero")
        idRol = input("Ingrese el tipo de usuario: ")
        idEmpresa = input("Ingrese el id de la empresa: ")
        estado = True
        usuario.crearUsuarios(conexion.Conectar(),nombre,usuarioN,contrasena,telefono,estado,idRol,idEmpresa)

    #Metodo desactivar usuarios
    def desactivarUsuarios():
        usuarioN = input("Ingrese el usuario: ")
        estado = False
        if (usuario.desactivarUsuario(conexion.Conectar(),usuarioN,estado)):
            print("Usuario desactivado")
        else:
            print("Error al desactivar usuario")

    #Metodo para Activar usuarios
    def activarUsuarios():
        usuarioN = input("Ingrese el usuario: ")
        estado = True
        if (usuario.activarUsuario(conexion.Conectar(),usuarioN,estado)):
            print("Usuario activado")
        else:
            print("Error al activar usuario")
    
    #Metodo para mostrar usuarios
    def mostrarUsuarios():
        estado = True
        print("Nombre--Usuario--Telefono--Rol--Empresa")
        usuario.mostrarUsuarios(conexion.Conectar(),estado)

