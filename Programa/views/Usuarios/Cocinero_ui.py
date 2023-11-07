#Crear cocinero con un menu lataral con las opciones de: inicio,notificaciones, cerrar sesion

from PyQt5 import QtWidgets

class CocineroView(QtWidgets.QWidget):
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
        self.btn_notificaciones = QtWidgets.QPushButton("Notificaciones")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        self.layout.addWidget(self.btn_inicio)
        self.layout.addWidget(self.btn_notificaciones)
        self.layout.addWidget(self.btn_logout)

        # Conectar las señales de clic de los botones a las funciones correspondientes
        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_notificaciones.clicked.connect(self.mostrar_notificaciones)
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
    
    def mostrar_notificaciones(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Locales"
        # Por ejemplo, una etiqueta con el texto "Gestión de Locales":
        notificaciones_content = QtWidgets.QLabel("Notificaciones")
        self.layout.addWidget(notificaciones_content)
        self.contenido = notificaciones_content
    
    def cerrar_sesion(self):
        self.close()
        import sys
        import os
        ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        sys.path.append(ruta_proyecto)
        from main import LoginApp
    
        window = LoginApp()
        window.show()