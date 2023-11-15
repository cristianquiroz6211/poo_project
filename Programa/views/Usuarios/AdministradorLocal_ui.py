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
        self.btn_productos = QtWidgets.QPushButton("Productos")
        self.btn_estadisticas = QtWidgets.QPushButton("Estadisticas")
        self.btn_agregar_cocineros = QtWidgets.QPushButton("Agregar Cocineros")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")

        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_productos.clicked.connect(self.mostrar_productos)
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        self.btn_agregar_cocineros.clicked.connect(self.mostrar_agregar_cocineros)
        self.btn_logout.clicked.connect(self.cerrar_sesion)

        self.layout.addWidget(self.btn_inicio)
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
    
    
    def mostrar_estadisticas(self):
       self.contenido.hide()
       # Aquí puedes mostrar el contenido relacionado con "Estadisticas"
       # Por ejemplo, una etiqueta con el texto "Gestión de Estadisticas":
       estadisticas_content = QtWidgets.QLabel("Gestión de Estadisticas")
       self.layout.addWidget(estadisticas_content)
       self.contenido = estadisticas_content

    def mostrar_agregar_cocineros(self):
      self.contenido.hide()

      # Crear etiquetas y campos de entrada de texto para ingresar datos del cocinero
      nombre_label = QtWidgets.QLabel("Nombre del cocinero:")
      nombre_input = QtWidgets.QLineEdit()
      usuario_label = QtWidgets.QLabel("Nombre de usuario:")
      usuario_input = QtWidgets.QLineEdit()
      contrasena_label = QtWidgets.QLabel("Contraseña:")
      contrasena_input = QtWidgets.QLineEdit()
      telefono_label = QtWidgets.QLabel("Número de teléfono:")
      telefono_input = QtWidgets.QLineEdit()
      idEmpresa_label = QtWidgets.QLabel("ID de la empresa:")
      idEmpresa_input = QtWidgets.QLineEdit()

      guardar_button = QtWidgets.QPushButton("Guardar Cocinero")

      # Agregar etiquetas y campos de entrada al diseño
      self.layout.addWidget(nombre_label)
      self.layout.addWidget(nombre_input)
      self.layout.addWidget(usuario_label)
      self.layout.addWidget(usuario_input)
      self.layout.addWidget(contrasena_label)
      self.layout.addWidget(contrasena_input)
      self.layout.addWidget(telefono_label)
      self.layout.addWidget(telefono_input)
      self.layout.addWidget(idEmpresa_label)
      self.layout.addWidget(idEmpresa_input)
      self.layout.addWidget(guardar_button)

      # Definir la función para guardar el cocinero
      def guardar_cocinero():
          nombre = nombre_input.text()
          usuarioN = usuario_input.text()
          contrasena = contrasena_input.text()
          telefono = telefono_input.text()
          idEmpresa = idEmpresa_input.text()

          # Llamar a la clase UsuariosModel para agregar el cocinero a la base de datos
          usuarios_model = UsuariosModel(dbname="FoodAlfa.V4", user="postgres", password="2919", host="localhost", port=5432)
          if usuarios_model.crear_cocinero(nombre, usuarioN, contrasena, telefono, idEmpresa):
              print("Cocinero creado exitosamente")
          else:
              print("Error al crear cocinero")

      guardar_button.clicked.connect(guardar_cocinero)

      self.contenido = QtWidgets.QWidget()
      self.layout.addWidget(self.contenido)
    
    def cerrar_sesion(self):
        self.close()
        import sys
        import os
        ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        sys.path.append(ruta_proyecto)
        from main import LoginApp
    
        window = LoginApp()
        window.show()



