import os
from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from Cocinero.crearcocinero import *

#conexion con la base de datos
conexion = BaseDatos("localhost",5432,"postgres","0000","FoodAlfa.V3")

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

