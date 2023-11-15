import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '...'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)
#cOREGIR CANBIOS
from contenedor import Contenedor
from controllers.pedidosController import ControladorPedidos
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pedidos(object):
    def setupUi(self, pedidos):
        
        
        self.restaurantes = []  # Lista para almacenar los restaurantes seleccionados
        self.productos = []    # Lista para almacenar los productos seleccionados
        self.notas = []        # Lista para almacenar las notas ingresadas
        self.contenedores = []
        
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
        
        self.mesa_label = QtWidgets.QLabel("Mesa:")
        self.mesa_combobox = QtWidgets.QComboBox()
        self.obtenermesas = ControladorPedidos()
        mesas = self.obtenermesas.obtener_mesas()
        self.mesa_combobox.addItems(mesas)

        self.mesero_label = QtWidgets.QLabel("Mesero:")
        self.mesero_combobox = QtWidgets.QComboBox()
        self.obtenermeseros = ControladorPedidos()
        meseros = self.obtenermeseros.obtener_meseros()
        self.mesero_combobox.addItems(meseros)

        self.verticalLayout_2.addWidget(self.mesa_label)
        self.verticalLayout_2.addWidget(self.mesa_combobox)
        self.verticalLayout_2.addWidget(self.mesero_label)
        self.verticalLayout_2.addWidget(self.mesero_combobox)
               
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
        self.submit.clicked.connect(self.enviar_pedido)
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
        self.contenedores.append(contenedor) 
        self.contador += 1
        
        self.restaurantes.append(contenedor.restaurante)
        self.productos.append(contenedor.producto)
        self.notas.append(contenedor.line_edit)
    def enviar_pedido(self):
            try:
                # Lógica para procesar el pedido
                controlador_pedidos = ControladorPedidos()
                controlador_pedidos.procesar_pedidos(
                    self.restaurantes, self.productos, self.notas,
                    self.mesa_combobox.currentText(), self.mesero_combobox.currentText()
                )

                # Reiniciar la pantalla después de procesar el pedido
                self.reiniciar_pantalla()

            except Exception as e:
                # Manejar excepciones según sea necesario
                print(f"Error al procesar el pedido: {e}")

    def reiniciar_pantalla(self):
        self.mesa_combobox.setCurrentIndex(0)
        self.mesero_combobox.setCurrentIndex(0)

        # Limpiar contenedores en el scrollArea
        for contenedor in self.contenedores:
            contenedor.hide()

        # Limpiar listas
        self.restaurantes.clear()
        self.productos.clear()
        self.notas.clear()

        # Restablecer el contador y agregar un nuevo contenedor inicial
        self.contador = 0
        self.agregar_contenedor()

        # Mostrar la ventana principal
        self.centralwidget.show()


    
    
        
    def limpiar_contenedores(self):
        for i in reversed(range(self.contenedor_layout.count())):
            self.contenedor_layout.itemAt(i).widget().deleteLater()

    @staticmethod
    def obtener_instancia():
        nueva_instancia = Ui_pedidos()
        nueva_instancia.setupUi(QtWidgets.QMainWindow())
        return nueva_instancia
        
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_pedidos.obtener_instancia()
    ui.show()
    sys.exit(app.exec_())



