import psycopg2
from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from BaseDeDatos.ValidarConexion import *

class GestionEmpresas:
    def crearEmpresas():
        nombre = input("Ingrese el nombre de la empresa: ")
        identificacion = input("Ingrese la identificacion de la empresa: ")
        idLocal = input("Ingrese el id del local: ")
        estado = True
        if (usuario.crearEmpresa(conexion.Conectar(),nombre,identificacion,idLocal,estado)):
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


