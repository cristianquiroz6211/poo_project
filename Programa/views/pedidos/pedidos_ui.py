# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedidos.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagen fondo-01_Mesa de trabajo 1.png"))
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
"#submit{\n"
"height:40px;\n"
"background:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FE59A8, stop:1 #FEA11B);\n"
"border: transparent;\n"
"color:white;\n"
"border-radius: 20px;\n"
"font-size: 17px;\n"
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
"#item{\n"
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
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 442, 192))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pedido = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.pedido.setGeometry(QtCore.QRect(0, 0, 444, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pedido.sizePolicy().hasHeightForWidth())
        self.pedido.setSizePolicy(sizePolicy)
        self.pedido.setMinimumSize(QtCore.QSize(0, 100))
        self.pedido.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pedido.setStyleSheet("QLineEdit,QComboBox{\n"
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
        self.pedido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pedido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pedido.setObjectName("pedido")
        self.gridLayout = QtWidgets.QGridLayout(self.pedido)
        self.gridLayout.setObjectName("gridLayout")
        self.producto = QtWidgets.QComboBox(self.pedido)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.producto.sizePolicy().hasHeightForWidth())
        self.producto.setSizePolicy(sizePolicy)
        self.producto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.producto.setObjectName("producto")
        self.gridLayout.addWidget(self.producto, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.pedido)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 2)
        self.restaurante = QtWidgets.QComboBox(self.pedido)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restaurante.sizePolicy().hasHeightForWidth())
        self.restaurante.setSizePolicy(sizePolicy)
        self.restaurante.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restaurante.setObjectName("restaurante")
        self.gridLayout.addWidget(self.restaurante, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.pedido)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.pedido)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
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
                # Añadir un layout vertical al widget de contenido del scrollArea
        self.scrollAreaWidgetContents.setLayout(QtWidgets.QVBoxLayout())

        # Conectar el widget de contenido al scrollArea
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Conectar el botón "Agregar Nuevo Pedido" a la función correspondiente
        self.pushButton.clicked.connect(self.agregar_nuevo_pedido)

    def retranslateUi(self, pedidos):
        _translate = QtCore.QCoreApplication.translate
        pedidos.setWindowTitle(_translate("pedidos", "MainWindow"))
        self.titulo.setText(_translate("pedidos", "Ingrese Pedido"))
        self.subtitulo.setText(_translate("pedidos", "¡Brilla en cada pedido que realices,"))
        self.subtitulo2.setText(_translate("pedidos", " cuidado y atención transforman cada experiencia!"))
        self.lineEdit.setPlaceholderText(_translate("pedidos", "Notas"))
        self.label_2.setText(_translate("pedidos", "Seleccione restaurante"))
        self.label_3.setText(_translate("pedidos", "Seleccione producto"))
        self.pushButton.setText(_translate("pedidos", "Agregar Nuevo Pedido"))
        self.submit.setText(_translate("pedidos", "Enviar Pedido"))
    def agregar_nuevo_pedido(self):
        # Crea un nuevo QFrame para el pedido
        nuevo_pedido = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        nuevo_pedido.setGeometry(QtCore.QRect(0, 0, 444, 100))
        nuevo_pedido.setMinimumSize(QtCore.QSize(0, 100))
        nuevo_pedido.setMaximumSize(QtCore.QSize(16777215, 100))
        nuevo_pedido.setStyleSheet("QLineEdit,QComboBox{\n"
                                   "border: 0px solid transparent;\n"
                                   "border-bottom: 2px solid #FE59A8;\n"
                                   "border-left: 2px solid #FE59A8;\n"
                                   "background:white;\n"
                                   "font-size:15px;\n"
                                   "padding:0px 0px 3px 3px;\n"
                                   "}\n"
                                   "QLineEdit:hover,QComboBox:hover{\n"
                                   "border-bottom: 2px solid #FEA11B;\n"
                                   "border-left: 2px solid #FEA11B;\n"
                                   "}\n"
                                   "QLabel{\n"
                                   "background:none;\n"
                                   "}")

        # Configura los widgets para el nuevo pedido (copiando del original)
        gridLayout = QtWidgets.QGridLayout(nuevo_pedido)
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                new_widget = widget.__class__(nuevo_pedido)
                if isinstance(widget, QtWidgets.QComboBox):
                    new_widget.addItems(widget.itemText(i) for i in range(widget.count()))
                new_widget.setObjectName(widget.objectName())
                if isinstance(widget, QtWidgets.QLabel):
                    new_widget.setText(widget.text())
                gridLayout.addWidget(new_widget, i // 2, i % 2, 1, 1)

        # Agrega el nuevo pedido al layout vertical del widget de contenido
        self.scrollAreaWidgetContents.layout().addWidget(nuevo_pedido)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pedidos = QtWidgets.QMainWindow()
    ui = Ui_pedidos()
    ui.setupUi(pedidos)
    pedidos.show()
    sys.exit(app.exec_())
