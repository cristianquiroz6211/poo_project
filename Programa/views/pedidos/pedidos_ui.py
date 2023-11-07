import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '...'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)
#cOREGIR CANBIOS

from controllers.pedidosController import ControladorRestaurante
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pedidos(object):
    def setupUi(self, pedidos):
        pedidos.setObjectName("pedidos")
        pedidos.resize(817, 523)
        pedidos.setMinimumSize(QtCore.QSize(817, 523))
        self.centralwidget = QtWidgets.QWidget(pedidos)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background:white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views/pedidos\\../imagen fondo-01_Mesa de trabajo 1.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("#titulo{\n"
"font-size:30px;\n"
"font-weight:600;\n"
"}\n"
"#subtitulo{\n"
"font-size:19px;\n"
"font-weight:500;\n"
"padding:0px;\n"
"}\n"
"#subtitulo2{\n"
"font-size:15px;\n"
"padding:0px;\n"
"}\n"
"#frame{\n"
"padding:30px;\n"
"}\n"
"#submit,#agregar{\n"
"height:40px;\n"
"background:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FE59A8, stop:1 #FEA11B);\n"
"border: transparent;\n"
"color:white;\n"
"border-radius: 20px;\n"
"font-size: 17px;\n"
"}\n"
"\n"
"#agregar{\n"
"font-size:15px;\n"
"border-bottom:2px solid #FE59A8 ;\n"
"margin-right:100px;\n"
"margin-left:100px;\n"
"border-radius:0px;\n"
"background:none;\n"
"color: #FE59A8;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        self.titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.subtitulo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitulo.sizePolicy().hasHeightForWidth())
        self.subtitulo.setSizePolicy(sizePolicy)
        self.subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo.setObjectName("subtitulo")
        self.verticalLayout.addWidget(self.subtitulo)
        self.subtitulo2 = QtWidgets.QLabel(self.frame)
        self.subtitulo2.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo2.setObjectName("subtitulo2")
        self.verticalLayout.addWidget(self.subtitulo2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("#frame_3{\n"
"background:none;\n"
"}\n"
"QFrame\n"
"{\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 89, 168, 0.15), stop:1 rgba(254, 161, 27, 0.15));\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("QLineEdit,QComboBox{\n"
    "border: 0px solid transparent;\n"
    "border-bottom: 2px solid #FE59A8;\n"
    "border-left: 2px solid #FE59A8;\n"
    "background:white;\n"
    "font-size:15px;\n"
    "padding:0px 0px 3px 3px;\n"
    "\n"
    "}\n"
    "QLineEdit:hover,QComboBox:hover{\n"
    "border-bottom: 2px solid #FEA11B;\n"
    "border-left: 2px solid #FEA11B;\n"
    "}\n"
    "QLabel{\n"
    "background:none;\n"
    "}")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 470, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.contenedor_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        
        self.contador =0
        self.agregar_contenedor()        
       
        
        
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_3)
        self.agregar = QtWidgets.QPushButton(self.frame)
        self.agregar.setObjectName("agregar")
        self.agregar.clicked.connect(self.agregar_contenedor)
        self.verticalLayout.addWidget(self.agregar)
        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)
        self.horizontalLayout.addWidget(self.frame)
        pedidos.setCentralWidget(self.centralwidget)

        self.retranslateUi(pedidos)
        QtCore.QMetaObject.connectSlotsByName(pedidos)

    def retranslateUi(self, pedidos):
        _translate = QtCore.QCoreApplication.translate
        pedidos.setWindowTitle(_translate("pedidos", "MainWindow"))
        self.titulo.setText(_translate("pedidos", "Ingrese Pedido"))
        self.subtitulo.setText(_translate("pedidos", "¡Brilla en cada pedido que realices,"))
        self.subtitulo2.setText(_translate("pedidos", " cuidado y atención transforman cada experiencia!"))
        self.agregar.setText(_translate("pedidos", "Agregar Nuevo Pedido"))
        self.submit.setText(_translate("pedidos", "Enviar Pedido"))

    def agregar_contenedor(self):
        contenedor = Contenedor(self.contador)
        self.contenedor_layout.addWidget(contenedor)
        self.contador += 1

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pedidos = QtWidgets.QMainWindow()
    ui = Ui_pedidos()
    ui.setupUi(pedidos)
    pedidos.show()
    sys.exit(app.exec_())
