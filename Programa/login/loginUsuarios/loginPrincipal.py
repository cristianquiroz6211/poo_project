from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from AdminGeneral.IndexAG import *
from AdminLocal.IndexAL import *
from BaseDeDatos.ValidarConexion import *
def login():
    usuarioN = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    estado = True
    if usuario.consultarCredenciales(conexion.Conectar(),usuarioN,contrasena,estado):
        usuario.idRol = usuario.consultarRol(conexion.Conectar(),usuarioN,contrasena)
        if usuario.idRol == 1:
            limpiarPantalla()
            loginAdminGeneral()
        elif usuario.idRol == 2:
            limpiarPantalla()
            loginAdminLocal()
    else:
        print("Usuario o contraseña incorrecta")
