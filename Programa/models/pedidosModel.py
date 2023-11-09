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

    def obtener_meseros(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "Nombre" FROM "Usuarios" WHERE "IdRol" = 4')
            user_data = cursor.fetchall()
            meseros = [row[0] for row in user_data]
            cursor.close()
            return meseros
        except Exception as e:
            print(f"Error al obtener meseros: {e}")
            return False
    def obtener_mesas(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "Mesas" FROM "Mesas"')
            mesas = cursor.fetchall()
            mesas = [str(row[0]) for row in mesas]  # Convertir a cadena
            cursor.close()
            return mesas
        except Exception as e:
            print(f"Error al obtener mesas: {e}")
            return False

    def obtener_precios(self, plato):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "Precio" FROM "Platos" WHERE "NombrePlato" = %s', (plato,))
            precio = cursor.fetchone()[0]
            cursor.close()
            return precio
        except Exception as e:
            print(f"Error al obtener precio: {e}")
            return False
        
    def obtener_id_mesero(self, mesero):   
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "IdUsuario" FROM "Usuarios" WHERE "Nombre" = %s', (mesero,))
            id_mesero = cursor.fetchone()[0]
            cursor.close()
            return id_mesero
        except Exception as e:
            print(f"Error al obtener id: {e}")
            return False
   
    def registrar_pedido(self, precio, id_mesa,fecha, id_mesero):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO "Pedidos" ("Precio", "IdMesa","FechaYHora","IdMesero") VALUES (%s, %s,%s,%s) ', (precio, id_mesa,fecha, id_mesero,))
            self.conn.commit()  # Realiza el commit de la transacción
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al registrar pedido: {e}")
            return False
    
    def obtener_id_pedido(self, idmesa):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "IdPedido" FROM "Pedidos" WHERE "IdMesa" = %s AND  "IdEstado"=1', (idmesa,))
            id_pedido = cursor.fetchone()[0]
            cursor.close()
            return id_pedido
        except Exception as e:
            print(f"Error al obtener id: {e}")
            return False
    def obtener_id_producto(self, plato):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT "IdPlato" FROM "Platos" WHERE "NombrePlato" = %s', (plato,))
            id_plato = cursor.fetchone()[0]
            cursor.close()
            return id_plato        
        except Exception as e:
            print(f"Error al obtener id: {e}")
            return False
        
        
        
        
        
        
        
    def realizar_subpedido(self, id_pedido, id_plato, nota):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO "SubPedido" ("IdPedido", "IdPlato", "Notas") VALUES (%s, %s, %s)', (id_pedido, id_plato, nota))
            self.conn.commit()  # Realiza el commit de la transacción
            cursor.close()
            return True
        except Exception as e:
            print(f"Error al registrar subpedido: {e}")
            return False