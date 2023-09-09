import psycopg2

class BaseDatos():
    #Atributos
    URL = ""
    port = 5432
    user = ""
    password = ""
    database = ""

    #Metodo constructor
    def __init__(self,URL,port,user,password,database):
        self.URL = URL
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    #Metodo Conectar
    def Conectar(self):
        try:
            credenciales = {
                "dbname": self.database,
                "user": self.user,
                "password": self.password,
                "host": self.URL,
                "port": self.port
                }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("conexión establecida con la base de datos.")
            return conexion
        except psycopg2.Error as e:
            print("Error al conectar con la base de datos: ". e)
            return False
