# users_ui.py
from PyQt5 import QtWidgets

class UsersView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        self.label = QtWidgets.QLabel("Bienvenido")
        self.layout.addWidget(self.label)
        
        # Botones para diferentes roles
        self.btn_admin_local = QtWidgets.QPushButton("Administrador Local")
        self.btn_admin_general = QtWidgets.QPushButton("Administrador General")
        self.btn_cocinero = QtWidgets.QPushButton("Cocinero")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        self.layout.addWidget(self.btn_admin_local)
        self.layout.addWidget(self.btn_admin_general)
        self.layout.addWidget(self.btn_cocinero)
        self.layout.addWidget(self.btn_logout)
