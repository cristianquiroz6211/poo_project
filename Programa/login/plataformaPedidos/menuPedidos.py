import psycopg2
from BaseDeDatos.conexionDB import *
from BaseDeDatos.Consultas import *
from BaseDeDatos.ValidarConexion import *

def mostrarMeserosYmesasActivos(conexion):    
    try:
        with conexion.cursor() as cursor:
            consulta = 'SELECT * FROM "Usuarios" WHERE "IdRol" = 4 AND "Estado" = True;'
            cursor.execute(consulta)
            registros = cursor.fetchall()
            mesasConsulta = 'SELECT * FROM "Mesas";'
            cursor.execute(mesasConsulta)
            registrosMesas = cursor.fetchall()
# Print meseros
            print("Meseros activos:")
            for mesero in registros:
                print(mesero[1])

            # Print mesas
            print("Mesas disponibles:")
            for mesa in registrosMesas:
                print(mesa[1])

            # Prompt user to choose mesero and mesa
            mesero_elegido = input("Ingrese el nombre del mesero que tomara la mesa: ")
            mesa_elegida = input("Ingrese el número de mesa que va a tomar: ")

            return (mesero_elegido, mesa_elegida)
    except psycopg2.Error as e:
        print('Error al mostrar usuarios ', e)
        return False
