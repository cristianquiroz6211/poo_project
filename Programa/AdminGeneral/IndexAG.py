
from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from BaseDeDatos.ValidarConexion import *
from Usuario.CRUDusuario import CRUDUsuario
from Empresa.crearEmpresa import GestionEmpresas 

def menuAG():
    print("************************************")
    print("*                                  *")
    print("*        ADMINISTRADOR GENERAL     *")
    print("*                                  *")
    print("************************************")
    print("*                                  *")
    print("* 1. Crear Usuario                 *")
    print("* 2. Desactivar Usuario            *")
    print("* 3. Activar Usuario               *")
    print("* 4. Mostrar Usuarios              *")
    print("* 5. Crear Empresa                 *")
    print("* 6. Desactivar Empresa            *")
    print("* 7. Activar Empresa               *")
    print("* 8. Mostrar Empresa               *")
    print("* 9. Salir                         *")
    print("*                                  *")
    print("************************************")

def loginAdminGeneral():
    print("Bienvenido AdministradorGeneral ")
    menuAG()
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 7:
        if opcion == 1:
            CRUDUsuario.crearUsuarios()
        elif opcion == 2:
            CRUDUsuario.desactivarUsuarios()
        elif opcion == 3:
            CRUDUsuario.activarUsuarios()
        elif opcion == 4:
            CRUDUsuario.mostrarUsuarios()
        elif opcion == 5:
            GestionEmpresas.crearEmpresas()
        elif opcion == 6:
            GestionEmpresas.desactivarEmpresas()
        elif opcion == 7:
            GestionEmpresas.activarEmpresas()
        elif opcion == 8:
            GestionEmpresas.mostrarEmpresas()
        elif opcion == 9:
            print("Adios")
            break
        else:
            print("Opcion incorrecta")
        input("Presione una tecla para continuar...")
        menuAG()
        opcion = int(input("Ingrese una opcion: "))