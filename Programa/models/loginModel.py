import psycopg2

class LoginModel:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def authenticate(self, username, password,estado):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'SELECT "Usuario","Contrasena","Estado" FROM "Usuarios" WHERE "Usuario"=%s AND "Contrasena"=%s AND "Estado"=%s;',
                (username, password,estado)
            )
            user_data = cursor.fetchone()
            cursor.close()
            if user_data:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al autenticar: {e}")
            return False
