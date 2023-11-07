import os
from BD.conexionDB import *
from BD.Consultas import *
from AdminGeneral.IndexAG import menuAG
from AdminLocal.IndexAL import menuAL
from Cocinero.IndexC import menuC
from Mesero.IndexM import menuM
from Cocinero.crearcocinero import *
from Empresa.crearEmpresa  import GestionEmpresas
from Usuario.dasactivarUsuario  import inactivo 
from plataformaPedidos.menuPedidos import *


#conexion con la base de datos
conexion = BaseDatos("localhost",5432,"postgres","2919","FoodAlfa.V4")

#Variables de las consultas de la base de datos
id = ""
nombre = ""
usuarioN = ""
contrasena = ""
telefono = ""
idRol = ""
idEmpresa = ""
identificacion = ""
estado = True
idLocal = ""

#Objeto de la clase Consulta
usuario = ConsultaUsuario(nombre,usuarioN,contrasena,telefono,estado,idRol,idEmpresa,identificacion,idLocal)

#Funcion para limpiar la pantalla
def limpiarPantalla():
    os.system("cls")

#Metodo para consultar credenciales
def login():
    usuarioN = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    estado = True
    if usuario.consultarCredenciales(conexion.Conectar(),usuarioN,contrasena,estado):
        usuario.idRol = usuario.consultarRol(conexion.Conectar(),usuarioN,contrasena)
        if usuario.idRol == 1:
            limpiarPantalla()
            print("Bienvenido AdministradorGeneral ")
            menuAG()
            opcion = int(input("Ingrese una opcion: "))
            while opcion != 7:
                if opcion == 1:
                    crearUsuarios()
                elif opcion == 2:
                    desactivarUsuarios()
                elif opcion == 3:
                    activarUsuarios()
                elif opcion == 4:
                    mostrarUsuarios()
                elif opcion == 5:
                    crearEmpresas()
                elif opcion == 6:
                    desactivarEmpresas()
                elif opcion == 7:
                    activarEmpresas()
                elif opcion == 8:
                    mostrarEmpresas()
                elif opcion == 9:
                    print("Adios")
                    break
                else:
                    print("Opcion incorrecta")
                input("Presione una tecla para continuar...")
                menuAG()
                opcion = int(input("Ingrese una opcion: "))
        elif usuario.idRol == 2:
            limpiarPantalla()
            print("Bienvenido AdministradorLocal")
            menuAL()
            opcion = int(input("Ingrese una opcion: "))
            while opcion != 5:
                if opcion == 1:
                    crear_cocinero(conexion.Conectar())
                    break
                elif opcion == 2:
                    usuarioN = input("Ingrese el usuario: ")
                    estado = False
                    DesactivarCocinero(conexion.Conectar(),usuarioN,estado)
                    break
                elif opcion == 3:
                   pass
                elif opcion == 4:
                    pass

        elif usuario.idRol == 4:
            limpiarPantalla()
            print("Bienvenido Mesero")
            menuM()
    else:
        print("Usuario o contraseña incorrecta")

def mostrarmeseros():
    mostrarMeserosDisponibles(conexion.Conectar())

#Metodo para crear usuarios
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

#Metodo para crear empresas
def crearEmpresas():
    nombre = input("Ingrese el nombre de la empresa: ")
    identificacion = input("Ingrese la identificacion de la empresa: ")
    idLocal = input("Ingrese el id del local: ")
    estado = True
    if (usuario.crearEmpresa(conexion.Conectar(),nombre,identificacion,estado,idLocal)):
        print("Empresa creada")
    else:
        print("Error al crear empresa")

#Metodo para eliminar empresas
def desactivarEmpresas():
    nombre = input("Ingrese el nombre de la empresa: ")
    estado = False
    if (usuario.desactivarEmpresa(conexion.Conectar(),nombre,estado)):
        print("Empresa eliminada")
    else:
        print("Error al eliminar empresa")

#Metodo para Activar empresas
def activarEmpresas():
    nombre = input("Ingrese el nombre de la empresa: ")
    estado = True
    if (usuario.activarEmpresa(conexion.Conectar(),nombre,estado)):
        print("Empresa activada")
    else:
        print("Error al activar empresa")

#Metodo Mostrar Empresas
def mostrarEmpresas():
    estado = True
    print("Nombre--Identificacion--Local")
    usuario.mostrarEmpresas(conexion.Conectar(),estado)

#Metodo Mostrar Usuarios
def mostrarUsuarios():
    estado = True
    print("Nombre--Usuario--Telefono--Rol--Empresa")
    usuario.mostrarUsuarios(conexion.Conectar(),estado)
