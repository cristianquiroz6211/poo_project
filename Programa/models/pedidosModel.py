# modelo_restaurante.py
import psycopg2
class Pedidos:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    def obtener_restaurantes(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "Empresa" FROM "Empresas"')
            user_data = cursor.fetchall()
            empresas = [row[0] for row in user_data]
            return empresas
            cursor.close()
        except Exception as e:
            print(f"Error al autenticar: {e}")
            return False
    def obtener_platos_por_empresa(self, id_empresa):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "IdPlato", "NombrePlato" FROM "Platos" WHERE "IdEmpresa" = %s', (id_empresa,))
            user_data = cursor.fetchall()
            platos = [{"id": row[0], "nombre": row[1]} for row in user_data]
            
            return platos
            cursor.close()
        except Exception as e:
            print(f"Error al obtener platos: {e}")
            return False
