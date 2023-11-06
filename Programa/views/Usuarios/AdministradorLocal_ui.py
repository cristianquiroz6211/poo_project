from PyQt5 import QtWidgets

class AdministradorLocalView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        self.label = QtWidgets.QLabel("Bienvenido")
        self.layout.addWidget(self.label)
        
        # Botones para diferentes roles
        self.btn_inicio = QtWidgets.QPushButton("Inicio")
        self.btn_local = QtWidgets.QPushButton("Local")
        self.btn_productos = QtWidgets.QPushButton("Productos")
        self.btn_estadisticas = QtWidgets.QPushButton("Estadisticas")
        self.btn_agregar_cocineros = QtWidgets.QPushButton("Agregar Cocineros")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        self.layout.addWidget(self.btn_inicio)
        self.layout.addWidget(self.btn_local)
        self.layout.addWidget(self.btn_productos)
        self.layout.addWidget(self.btn_agregar_cocineros)
        self.layout.addWidget(self.btn_logout)

