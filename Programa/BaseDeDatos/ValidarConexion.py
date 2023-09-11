import os
from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from AdminGeneral.IndexAG import menuAG
from AdminLocal.IndexAL import menuAL
from Cocinero.IndexC import menuC
from Mesero.IndexM import menuM
from Cocinero.crearcocinero import Cocinero


#conexion con la base de datos
conexion = BaseDatos("localhost",5432,"postgres","0000","FoodAlfa.V2")

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

#Funcion para limpiar la pantalla
def limpiarPantalla():
    os.system("cls")

#Metodo para consultar credenciales
def login():
    usuarioN = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if usuario.consultarCredenciales(conexion.Conectar(),usuarioN,contrasena):
        usuario.idRol = usuario.consultarRol(conexion.Conectar(),usuarioN,contrasena)
        if usuario.idRol == 1:
            limpiarPantalla()
            print("Bienvenido AdministradorGeneral ")
            menuAG()
            opcion = int(input("Ingrese una opcion: "))
            while opcion != 4:
                if opcion == 1:
                    crearUsuarios()
                elif opcion == 2:
                    eliminarUsuarios()
                elif opcion == 3:
                    crearEmpresa()
                elif opcion == 4:
                    eliminarEmpresa()
                elif opcion == 5:
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
                    crearCocineros()
                elif opcion == 2:
                    eliminarUsuarios()
                elif opcion == 3:
                    crearProductos()
                elif opcion == 4:
                    HistorialVentasLocal()
                elif opcion == 5:
                    print("Adios")
                    break
                else:
                    print("Opcion incorrecta")
                input("Presione una tecla para continuar...")
                menuAL()
                opcion = int(input("Ingrese una opcion: "))
        elif usuario.idRol == 3:
            limpiarPantalla()
            print("Bienvenido Cocinero")
            menuC()
            opcion = int(input("Ingrese una opcion: "))
            while opcion != 3:
                if opcion == 1:
                    verPedidos()
                elif opcion == 2:
                    confirmarPedidos()
                elif opcion == 3:
                    print("Adios")
                    break
                else:
                    print("Opcion incorrecta")
                input("Presione una tecla para continuar...")
                menuC()
                opcion = int(input("Ingrese una opcion: "))
        elif usuario.idRol == 4:
            limpiarPantalla()
            print("Bienvenido Mesero")
            menuM()
            opcion = int(input("Ingrese una opcion: "))
            while opcion != 4:
                if opcion == 1:
                    tomarPedidos()
                elif opcion == 2:
                    confirmarPedidos()
                elif opcion == 3:
                    pagarPedidos()
                elif opcion == 4:
                    print("Adios")
                    break
                else:
                    print("Opcion incorrecta")
                input("Presione una tecla para continuar...")
                menuM()
                opcion = int(input("Ingrese una opcion: "))

    else:
        print("Usuario o contraseña incorrecta")

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

#Metodo Eliminar usuarios
def eliminarUsuarios():
    pass

#Metodo Crear Empresa
def crearEmpresa():
    pass

#Metodo Eliminar Empresa
def eliminarEmpresa():
    pass

#Metodo Crear Cocineros
def crearCocineros():
    #Se llama a la clase cocinero 
    cocinero = Cocinero()
    cocinero.crear_cocinero()
    

    
#Metodo Crear Productos
def crearProductos():
    pass

#Metodo Historial de ventas local
def HistorialVentasLocal():
    pass

#Metodo Ver pedidos
def verPedidos():
    pass

#Metodo Confirmar pedidos
def confirmarPedidos():
    pass

#Metodo Tomar pedidos
def tomarPedidos():
    pass

#Metodo Pagar pedidos
def pagarPedidos():
    pass