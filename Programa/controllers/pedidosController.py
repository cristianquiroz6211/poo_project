import sys
import os
from PyQt5 import QtWidgets
from datetime import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now()
fecha_formateada = fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')

# Obtener la ruta al directorio del proyecto
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)
from models.pedidosModel import Pedidos

class ControladorPedidos:
    def __init__(self):
        self.modelo = Pedidos(dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432)

    def obtener_restaurantes(self):
        return self.modelo.obtener_restaurantes()
    
    def obtener_platos_por_empresa(self, id_empresa):
        return self.modelo.obtener_platos_por_empresa(id_empresa)
    
    def obtener_meseros(self):
        return self.modelo.obtener_meseros()
    def obtener_mesas(self):
        
        return self.modelo.obtener_mesas()
    
    def procesar_pedidos(self, restaurantes, productos, notas, mesas, meseros):
        # Aquí puedes poner la lógica para procesar los pedidos
        total=0
        id_producto=[]
        for producto in productos:
            id_producto.append(self.modelo.obtener_id_producto(producto.currentText()))
            precio=self.modelo.obtener_precios(producto.currentText())
            if precio is not False:  # Asegúrate de que la consulta fue exitosa
             total += precio
        id_mesero=self.modelo.obtener_id_mesero(meseros)
        self.modelo.registrar_pedido(total, mesas,fecha_formateada, id_mesero)
        id_pedido=self.modelo.obtener_id_pedido(mesas)
        
        for restaurante, idprod, nota in zip(restaurantes, id_producto, notas):
            restaurante_seleccionado = restaurante.currentText()
            #producto_seleccionado = producto.currentText()
            nota_ingresada = nota.text()
            self.modelo.realizar_subpedido(id_pedido, idprod, nota_ingresada)
            print(f"Restaurante seleccionado: {restaurante_seleccionado}, Producto seleccionado: {idprod}, Nota: {nota_ingresada}")  
            

