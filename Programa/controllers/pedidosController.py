import sys
import os
from PyQt5 import QtWidgets

# Obtener la ruta al directorio del proyecto
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)
from models.pedidosModel import Pedidos

class ControladorRestaurante:
    def __init__(self):
        self.modelo = Pedidos(dbname="poo", user="postgres", password="0000", host="localhost", port=5432)

    def obtener_restaurantes(self):
        return self.modelo.obtener_restaurantes()
    def obtener_platos_por_empresa(self, id_empresa):
        return self.modelo.obtener_platos_por_empresa(id_empresa)

