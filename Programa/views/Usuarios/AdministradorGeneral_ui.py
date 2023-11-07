from PyQt5 import QtWidgets
from   models.usuariosModel import UsuariosModel
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class AdministradorGeneralView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)
        
        # Layout principal en forma de QHBoxLayout
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        
        # Menú lateral en forma de QVBoxLayout
        menu_layout = QtWidgets.QVBoxLayout()
        
        self.label = QtWidgets.QLabel("Bienvenido")
        menu_layout.addWidget(self.label)
        
        # Botones para diferentes roles
        self.btn_inicio = QtWidgets.QPushButton("Inicio")
        self.btn_locales = QtWidgets.QPushButton("Locales")
        self.btn_usuarios = QtWidgets.QPushButton("Usuarios")
        self.btn_estadisticas = QtWidgets.QPushButton("Estadísticas")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        menu_layout.addWidget(self.btn_inicio)
        menu_layout.addWidget(self.btn_locales)
        menu_layout.addWidget(self.btn_usuarios)
        menu_layout.addWidget(self.btn_estadisticas)
        menu_layout.addWidget(self.btn_logout)
        
        # Conectar las señales de clic de los botones a las funciones correspondientes
        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_locales.clicked.connect(self.mostrar_locales)
        self.btn_usuarios.clicked.connect(self.mostrar_usuarios)
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        self.btn_logout.clicked.connect(self.cerrar_sesion)
        
        # Agregar el menú lateral al layout principal
        self.layout.addLayout(menu_layout)
        
        # Widget para mostrar contenido dinámico
        self.contenido = QtWidgets.QWidget()
        self.layout.addWidget(self.contenido)
        
    def mostrar_inicio(self):
        self.contenido.hide()
        # Puedes crear un nuevo widget o mostrar el contenido que desees en la vista de "Inicio"
        # Por ejemplo, aquí se muestra una etiqueta con el texto "Página de Inicio":
        inicio_content = QtWidgets.QLabel("Página de Inicio")
        self.contenido = inicio_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), inicio_content)
    
    def mostrar_locales(self):
        self.contenido.hide()
        locales_content = QWidget()
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), locales_content)

        # Crear una instancia de la clase UsuariosModel
        model = UsuariosModel(dbname="FoodAlfa.V4", user="postgres", password="2919", host="localhost", port=5432)

        # Llamar a la función obtener_Empresas y almacenar el resultado en una variable
        empresas = model.obtener_Empresas()

        # Crear un widget de texto para mostrar los resultados
        resultados_label = QLabel("Empresas y sus identificaciones:")
        resultados_text = QLabel("\n".join([f"{empresa['Empresa']}: {empresa['Identificacion']}" for empresa in empresas]))

        layout = QVBoxLayout()
        layout.addWidget(resultados_label)
        layout.addWidget(resultados_text)
        locales_content.setLayout(layout)
            
    
    def mostrar_usuarios(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Usuarios"
        # Por ejemplo, una etiqueta con el texto "Gestión de Usuarios":
        usuarios_content = QtWidgets.QLabel("Gestión de Usuarios")
        self.contenido = usuarios_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), usuarios_content)
    
    
    def mostrar_estadisticas(self):
        self.contenido.hide()
        # Aquí puedes mostrar el contenido relacionado con "Estadísticas"
        # Por ejemplo, una etiqueta con el texto "Estadísticas de la Administración":
        estadisticas_content = QtWidgets.QLabel("Estadísticas de la Administración")
        self.contenido = estadisticas_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), estadisticas_content)
    
    def cerrar_sesion(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = AdministradorGeneralView()
    ventana.show()
    sys.exit(app.exec_())
