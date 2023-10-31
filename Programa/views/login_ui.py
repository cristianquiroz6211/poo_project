# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class PasswordLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(PasswordLineEdit, self).__init__(parent)
        self.setEchoMode(QtWidgets.QLineEdit.Password)

class Ui_IniciarSesion(object):
    def setupUi(self, IniciarSesion):
        IniciarSesion.setObjectName("IniciarSesion")
        IniciarSesion.setEnabled(True)
        IniciarSesion.resize(816, 524)
        IniciarSesion.setStyleSheet("QMainWindow{\n"
"padding:0px;\n"
"margin:0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(IniciarSesion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background:white;\n"
"padding:0px;\n"
"margin:0px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginframe.sizePolicy().hasHeightForWidth())
        self.loginframe.setSizePolicy(sizePolicy)
        self.loginframe.setStyleSheet("#loginframe{\n"
"background-color:white;\n"
"padding:100px 35px;\n"
"margin:0px;\n"
"}\n"
"#titulo{\n"
"color:#FE59A8;\n"
"font-size: 30px;\n"
"}\n"
"QLineEdit{\n"
"border: 0px solid transparent;\n"
"border-bottom: 2px solid #FE59A8;\n"
"border-left: 2px solid #FE59A8;\n"
"background:transparent;\n"
"font-size:15px;\n"
"padding:0px 0px 3px 3px;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"border-bottom: 2px solid #FEA11B;\n"
"border-left: 2px solid #FEA11B;\n"
"}\n"
"#labelinput,#labelinput_2,#mostrar{\n"
"padding:0px 0px 5px 3px;\n"
"color: grey;\n"
"font-size: 15px;\n"
"\n"
"}\n"
"#submit{\n"
"height:60px;\n"
"background:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FE59A8, stop:1 #FEA11B);\n"
"border: transparent;\n"
"color:white;\n"
"border-radius: 20px;\n"
"font-size: 17px;\n"
"}\n"
"#submit:active{\n"
"\n"
"}\n"
"QCheckBox {\n"
"    font-size:13px;\n"
"    color: grey; /* Cambia el color del texto a blanco */\n"
"}")
        self.loginframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginframe.setObjectName("loginframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.loginframe)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(self.loginframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.usuario = QtWidgets.QLineEdit(self.loginframe)
        self.usuario.setMaximumSize(QtCore.QSize(16777215, 30))
        self.usuario.setObjectName("usuario")
        self.verticalLayout.addWidget(self.usuario)
        self.contrasena = PasswordLineEdit(self.loginframe)
        #self.contrasena = QtWidgets.QLineEdit(self.loginframe)
        self.contrasena.setMaximumSize(QtCore.QSize(16777215, 30))
        self.contrasena.setObjectName("contrasena")
        self.verticalLayout.addWidget(self.contrasena)
        self.checkBox = QtWidgets.QCheckBox(self.loginframe)
        self.checkBox.setObjectName("mostrarContrasena")
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.submit = QtWidgets.QPushButton(self.loginframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)
        
        # Cambia esta sección en tu archivo login_ui.py
        self.ir_a_pedidos = QtWidgets.QPushButton(self.loginframe)
        self.ir_a_pedidos.setText("Ir a la plataforma de pedidos")
        self.ir_a_pedidos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ir_a_pedidos.setObjectName("ir_a_pedidos")
        self.ir_a_pedidos.setStyleSheet("color: #FE59A8; border:none; background: none; font-size: 15px")
        self.verticalLayout.addWidget(self.ir_a_pedidos)
        #self.ir_a_pedidos.clicked.connect(self.controller.abrir_pedidos)


        self.horizontalLayout.addWidget(self.loginframe)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("views\\imagen fondo-01_Mesa de trabajo 1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        IniciarSesion.setCentralWidget(self.centralwidget)

        self.retranslateUi(IniciarSesion)
        QtCore.QMetaObject.connectSlotsByName(IniciarSesion)

    def retranslateUi(self, IniciarSesion):
        _translate = QtCore.QCoreApplication.translate
        IniciarSesion.setWindowTitle(_translate("IniciarSesion", "MainWindow"))
        self.titulo.setText(_translate("IniciarSesion", "Le damos la bienvenida"))
        self.usuario.setPlaceholderText(_translate("IniciarSesion", "Usuario"))
        self.contrasena.setPlaceholderText(_translate("IniciarSesion", "Contraseña"))
        self.checkBox.setText(_translate("IniciarSesion", "Mostrar contraseña"))
        self.submit.setText(_translate("IniciarSesion", "Iniciar sesión"))