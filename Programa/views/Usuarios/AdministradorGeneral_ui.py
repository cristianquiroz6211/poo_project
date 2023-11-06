from PyQt5 import QtWidgets

class AdministradorGeneralView(QtWidgets.QWidget):
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
        self.btn_locales = QtWidgets.QPushButton("Locales")
        self.btn_usuarios = QtWidgets.QPushButton("Usuarios")
        self.btn_productos = QtWidgets.QPushButton("Productos")
        self.btn_estadisticas = QtWidgets.QPushButton("Estadísticas")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        self.layout.addWidget(self.btn_inicio)
        self.layout.addWidget(self.btn_locales)
        self.layout.addWidget(self.btn_usuarios)
        self.layout.addWidget(self.btn_productos)
        self.layout.addWidget(self.btn_estadisticas)
        self.layout.addWidget(self.btn_logout)
        
        # Conectar las señales de clic de los botones a las funciones correspondientes
        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_locales.clicked.connect(self.mostrar_locales)
        self.btn_usuarios.clicked.connect(self.mostrar_usuarios)
        self.btn_productos.clicked.connect(self.mostrar_productos)
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        self.btn_logout.clicked.connect(self.cerrar_sesion)
        
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
    
    def mostrar_locales(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Locales"
        # Por ejemplo, una etiqueta con el texto "Gestión de Locales":
        locales_content = QtWidgets.QLabel("Gestión de Locales")
        self.layout.addWidget(locales_content)
        self.contenido = locales_content
    
    def mostrar_usuarios(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Usuarios"
        # Por ejemplo, una etiqueta con el texto "Gestión de Usuarios":
        usuarios_content = QtWidgets.QLabel("Gestión de Usuarios")
        self.layout.addWidget(usuarios_content)
        self.contenido = usuarios_content
    
    def mostrar_productos(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Productos"
        # Por ejemplo, una etiqueta con el texto "Gestión de Productos":
        productos_content = QtWidgets.QLabel("Gestión de Productos")
        self.layout.addWidget(productos_content)
        self.contenido = productos_content
    
    def mostrar_estadisticas(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Estadísticas"
        # Por ejemplo, una etiqueta con el texto "Estadísticas de la Administración":
        estadisticas_content = QtWidgets.QLabel("Estadísticas de la Administración")
        self.layout.addWidget(estadisticas_content)
        self.contenido = estadisticas_content
    
    def cerrar_sesion(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = AdministradorGeneralView()
    ventana.show()
    sys.exit(app.exec_())


