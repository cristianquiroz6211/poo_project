#Se debe imprimir los meseros, estos son en la base de batos de usuarios con el codigo 4.
import psycopg2
def mostrarMeserosDisponibles(conexion):
    try:
        with conexion.cursor() as cursor:
            consulta = 'SELECT * FROM "Usuarios" WHERE "IdRol" = 4;'
            cursor.execute(consulta)
            registros = cursor.fetchall()
            for registro in registros:
                #Imprimir solo el nombre 
                print(registro[1])
        return registros
    except psycopg2.Error as e:
        print("Error al mostrar usuarios ", e)
        return False
    
#Se debe imprimir los meseros disponibles, estos son en la base de batos de usuarios con el codigo 4. y se debe escoger cual será el usuario que tome el pedido