from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '...'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)
#cOREGIR CANBIOS

from controllers.pedidosController import ControladorRestaurante
class Contenedor(QtWidgets.QFrame):
    def __init__(self, identificador):
        super().__init__()

        self.identificador = identificador

        #self.setStyleSheet("QFrame{background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 89, 168, 0.15), stop:1 rgba(254, 161, 27, 0.15));}")

        self.layout = QtWidgets.QGridLayout(self)

        # Label "Seleccione Restaurante"
        label_restaurante = QtWidgets.QLabel("Seleccione Restaurante")
        self.layout.addWidget(label_restaurante, 0, 0)

        # Columna 1: ComboBox de Restaurante
        self.restaurante = QtWidgets.QComboBox()
        self.controlador_restaurante = ControladorRestaurante()
        restaurantes = self.controlador_restaurante.obtener_restaurantes()
        self.restaurante.addItems(restaurantes)
        self.layout.addWidget(self.restaurante, 1, 0)

        # Label "Seleccione Producto"
        label_producto = QtWidgets.QLabel("Seleccione Producto")
        self.layout.addWidget(label_producto, 0, 1)

        # Columna 2: ComboBox de Producto
        self.restaurante.currentIndexChanged.connect(self.actualizar_platos)
        self.producto = QtWidgets.QComboBox()
        self.layout.addWidget(self.producto, 1, 1)

        # Line Edit para Notas
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Notas")
        self.layout.addWidget(self.line_edit, 2, 0, 1, 2)

    def actualizar_platos(self):
       # Obtiene el índice de la empresa seleccionada
        index = self.restaurante.currentIndex()+1
       
        # Obtiene los platos correspondientes
        platos = self.controlador_restaurante.obtener_platos_por_empresa(index)
        # Limpia el ComboBox de productos
        self.producto.clear()

        # Llena el ComboBox de productos con los platos
        for plato in platos:
                self.producto.addItem(plato["nombre"], userData=plato["id"])
