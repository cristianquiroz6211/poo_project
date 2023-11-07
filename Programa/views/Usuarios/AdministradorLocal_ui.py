from PyQt5 import QtWidgets
from   models.usuariosModel import UsuariosModel

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

        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_local.clicked.connect(self.mostrar_local)
        self.btn_productos.clicked.connect(self.mostrar_productos)
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        self.btn_agregar_cocineros.clicked.connect(self.mostrar_agregar_cocineros)
        self.btn_logout.clicked.connect(self.cerrar_sesion)

        self.layout.addWidget(self.btn_inicio)
        self.layout.addWidget(self.btn_local)
        self.layout.addWidget(self.btn_productos)
        self.layout.addWidget(self.btn_estadisticas)
        self.layout.addWidget(self.btn_agregar_cocineros)
        self.layout.addWidget(self.btn_logout)

        # Widget para mostrar contenido dinámico
        self.contenido = QtWidgets.QWidget()
        self.layout.addWidget(self.contenido)

    def mostrar_inicio(self):
        self.contenido.hide()
        # Puedes crear un nuevo widget o mostrar el contenido que desees en la vista de "Inicio"
        # Por ejemplo, aquí se muestra una etiqueta con el texto "Página de Inicio":
        inicio_content = QtWidgets.QLabel("Página de Inicio")
        self.layout.addWidget(inicio_content)
        self.contenido = inicio_content
    
    def mostrar_local(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Locales"
        # Por ejemplo, una etiqueta con el texto "Gestión de Locales":
        local_content = QtWidgets.QLabel("Gestión de Local")
        self.layout.addWidget(local_content)
        self.contenido = local_content
    
    def mostrar_productos(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Productos"
        # Por ejemplo, una etiqueta con el texto "Gestión de Productos":
        productos_content = QtWidgets.QLabel("Gestión de Productos")
        self.layout.addWidget(productos_content)
        self.contenido = productos_content
    
    def mostrar_estadisticas(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Estadisticas"
        # Por ejemplo, una etiqueta con el texto "Gestión de Estadisticas":
        estadisticas_content = QtWidgets.QLabel("Gestión de Estadisticas")
        self.layout.addWidget(estadisticas_content)
        self.contenido = estadisticas_content

    def mostrar_agregar_cocineros(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Agregar Cocineros"
        # Por ejemplo, una etiqueta con el texto "Gestión de Agregar Cocineros":
        agregar_cocineros_content = QtWidgets.QLabel("Gestión de Agregar Cocineros")
        self.layout.addWidget(agregar_cocineros_content)
        self.contenido = agregar_cocineros_content
        
    
    def cerrar_sesion(self):
        self.close()


