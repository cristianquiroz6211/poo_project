import os
from login.loginUsuarios.loginPrincipal import *
from login.plataformaPedidos.menuPedidos import *


# Funcion para limpiar la pantalla

def limpiarPantalla():
    os.system("cls")

# Funcion para mostrar el menu de login

def menuLogin():
    limpiarPantalla()
    print("****************************************")
    print("*                                      *")
    print("*             LOGIN                    *")
    print("*                                      *")
    print("****************************************")
    print("* 1. Ingresar Usuario y Contraseña     *")
    print("* 2.Ingresar a la plataforma de pedidos*")
    print("* 3. Salir                             *")
    print("****************************************")

# Funcion para validar el usuario y la contraseña

menuLogin()
opcion = int(input("Ingrese una opcion: "))
while opcion != 3:
    if opcion == 1:
        login()
    if opcion == 2:
         mostrarMeserosYmesasActivos(conexion.Conectar())
    elif opcion == 3:
        print("Adios")
        break
    else:
        print("Opcion incorrecta")

    input("Presione una tecla para continuar...")
    menuLogin()
    opcion = int(input("Ingrese una opcion: "))
