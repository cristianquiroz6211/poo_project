from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *

#conexion con la base de datos
conexion = BaseDatos("localhost",5432,"postgres","0000","FoodAlfa")

#Variables de las consultas de la base de datos
nombre = ""
usuarioN = ""
contrasena = ""
telefono = ""
idRol = ""
idEmpresa = ""
estado = True

#Objeto de la clase Consulta
usuario = Consulta(nombre,usuarioN,contrasena,telefono,estado,idRol,idEmpresa)

#Metodo para crear usuarios
def crearUsuarios():
    nombre = input("Ingrese el nombre: ")
    usuarioN = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    telefono = input("Ingrese el telefono: ")
    print("Tipos de usuario: \n1. AdministradorLocal \n2. Mesero \n3. Cocinero \n4. AdministradorGeneral")
    idRol = input("Ingrese el tipo de usuario: ")
    idEmpresa = input("Ingrese el id de la empresa: ")
    estado = True
    usuario.crearUsuarios(conexion.Conectar(),nombre,usuarioN,contrasena,telefono,estado,idRol,idEmpresa)


#Metodo para consultar credenciales
def login():
    usuarioN = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if usuario.consultarCredenciales(conexion.Conectar(),usuarioN,contrasena):
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrecta")

#Metodo Eliminar usuarios
def eliminarUsuarios():
    pass

#Metodo Crear Empresa
def crearEmpresa():
    nombre = input("Ingrese el nombre de la empresa: ")
    direccion = input("Ingrese la direccion de la empresa: ")
    telefono = input("Ingrese el telefono de la empresa: ")
    usuario.crearEmpresa(conexion.Conectar(),nombre,direccion,telefono)

#Metodo Eliminar Empresa
def eliminarEmpresa():
    pass





    
