from BaseDeDatos.ValidarConexion import *
import os

# Mostar el menu de administrador general con las funciones que puede realizar:
# 1. Crear usuario
# 2. Modificar usuario
# 3. Eliminar usuario
# 4. Crear empresa
# 5. Modificar empresa
# 6. Eliminar empresa
# 7. Salir

# Funcion para limpiar la pantalla
def limpiarPantalla():
    os.system("cls")

# Funcion para mostrar el menu de administrador general
def menuAG():
    limpiarPantalla()
    print("************************************")
    print("*                                  *")
    print("*        ADMINISTRADOR GENERAL     *")
    print("*                                  *")
    print("************************************")
    print("*                                  *")
    print("* 1. Crear Usuario                 *")
    print("* 2. Modificar Usuario             *")
    print("* 3. Eliminar Usuario              *")
    print("* 4. Crear Empresa                 *")
    print("* 5. Modificar Empresa             *")
    print("* 6. Eliminar Empresa              *")
    print("* 7. Salir                         *")
    print("*                                  *")
    print("************************************")

# Iniciar el programa
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
    else:
        print("Opcion incorrecta")
    input("Presione una tecla para continuar...")
    menuAG()
    opcion = int(input("Ingrese una opcion: "))
