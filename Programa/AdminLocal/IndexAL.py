from Cocinero.crearcocinero import *
from BaseDeDatos.ValidarConexion import *

# Funcion para mostrar el menu del administrador local
def menuAL():
    print("************************************")
    print("*                                  *")
    print("*        ADMINISTRADOR LOCAL       *")
    print("*                                  *")
    print("************************************")
    print("*                                  *")
    print("* 1. Crear cocineros               *")
    print("* 2. Eliminar Cocineros            *")
    print("* 3. Crear productos               *")
    print("* 4. Historial de Ventas           *")
    print("* 5. Salir                         *")
    print("*                                  *")
    print("************************************")

def loginAdminLocal():
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
        elif opcion == 5:
            print("Adios")
            break
        else:
            print("Opcion incorrecta")
        input("Presione una tecla para continuar...")
        menuAL()
        opcion = int(input("Ingrese una opcion: "))