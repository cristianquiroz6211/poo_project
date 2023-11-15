from PyQt5 import QtWidgets
from models.usuariosModel import UsuariosModel
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class AdministradorGeneralView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)
        self.model = UsuariosModel(dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432)
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
        self.btn_usuarios = QtWidgets.QPushButton("Agragar Usuarios")
        self.btn_lista_usuarios = QtWidgets.QPushButton("Lista de Usuarios")
        self.btn_estadisticas = QtWidgets.QPushButton("Estadísticas")
        self.btn_logout = QtWidgets.QPushButton("Cerrar Sesión")
        
        menu_layout.addWidget(self.btn_inicio)
        menu_layout.addWidget(self.btn_locales)
        menu_layout.addWidget(self.btn_usuarios)
        menu_layout.addWidget(self.btn_lista_usuarios)
        menu_layout.addWidget(self.btn_estadisticas)
        menu_layout.addWidget(self.btn_logout)
        
        # Conectar las señales de clic de los botones a las funciones correspondientes
        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_locales.clicked.connect(self.mostrar_locales)
        self.btn_usuarios.clicked.connect(self.mostrar_usuarios)
        self.btn_lista_usuarios.clicked.connect(self.mostrar_lista_usuarios)
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        self.btn_logout.clicked.connect(self.cerrar_sesion)
        
        # Agregar el menú lateral al layout principal
        self.layout.addLayout(menu_layout)
        
        # Widget para mostrar contenido dinámico
        self.contenido = QtWidgets.QWidget()
        self.layout.addWidget(self.contenido)
    
    def mostrar_lista_usuarios(self):
        self.contenido.hide()
        lista_usuarios_content = QtWidgets.QWidget()
        layout = QVBoxLayout()

        # Mostrar la información de los usuarios
        usuarios = self.model.obtener_usuarios()
        resultados_label = QLabel("Información de los usuarios:")

        # Mapear los valores de rol a su representación de texto
        rol_mapping = {
            1: 'Administrador General',
            2: 'Administrador de Local',
            3: 'Cocinero',
            4: 'Mesero'
        }

        Estado_mapping = {
            True: 'Activo',
            False: 'Inactivo'
        }
    
        resultados_text = QLabel("\n".join([f"Nombre: {usuario['Nombre']}, Rol: {rol_mapping[usuario['IdRol']]}, Teléfono: {usuario['Telefono']}, Estado: {Estado_mapping[usuario['Estado']]}, Empresa: {usuario['Empresa']}" for usuario in usuarios]))

        layout.addWidget(resultados_label)
        layout.addWidget(resultados_text)
        lista_usuarios_content.setLayout(layout)

        self.contenido = lista_usuarios_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), lista_usuarios_content)

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

        # Llamar a la función obtener_Empresas y almacenar el resultado en una variable
        empresas = self.model.obtener_Empresas()

        # Crear un widget de texto para mostrar los resultados
        resultados_label = QLabel("Empresas y sus identificaciones:")
        resultados_text = QLabel("\n".join([f"{empresa['Empresa']}: {empresa['Identificacion']}" for empresa in empresas]))

        layout = QVBoxLayout()
        layout.addWidget(resultados_label)
        layout.addWidget(resultados_text)
        locales_content.setLayout(layout)

        self.contenido = locales_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), locales_content)

    def mostrar_usuarios(self):
            self.contenido.hide()
            
            # Crear un formulario para agregar usuarios
            formulario = QtWidgets.QWidget()
            layout = QtWidgets.QFormLayout()
            
            nombre_input = QtWidgets.QLineEdit()
            usuario_input = QtWidgets.QLineEdit()
            contraseña_input = QtWidgets.QLineEdit()
            telefono_input = QtWidgets.QLineEdit()
            
            tipo_usuario_combo = QtWidgets.QComboBox()
            tipo_usuario_combo.addItems(['Administrador General', 'Administrador de Local', 'Mesero', 'Cocinero'])
            
            id_empresa_input = QtWidgets.QLineEdit()
            
            layout.addRow("Nombre:", nombre_input)
            layout.addRow("Usuario:", usuario_input)
            layout.addRow("Contraseña:", contraseña_input)
            layout.addRow("Teléfono:", telefono_input)
            layout.addRow("Tipo de Usuario:", tipo_usuario_combo)
            layout.addRow("ID de Empresa:", id_empresa_input)

            agregar_button = QtWidgets.QPushButton("Agregar Usuario")

            def insertar_usuario():
                nombre = nombre_input.text()
                usuario = usuario_input.text()
                contraseña = contraseña_input.text()
                telefono = telefono_input.text()
                tipo_usuario = tipo_usuario_combo.currentText()  # Obtener el texto seleccionado
                id_empresa = id_empresa_input.text()

                # Convertir tipo_usuario a un valor numérico según tus criterios
                if tipo_usuario == "Administrador General":
                    tipo_usuario_num = 1
                elif tipo_usuario == "Administrador de Local":
                    tipo_usuario_num = 2
                elif tipo_usuario == "Cocinero":
                    tipo_usuario_num = 3
                elif tipo_usuario == "Mesero":
                    tipo_usuario_num = 4
                else:
                    tipo_usuario_num = 0  # Un valor por defecto si no coincide con ninguno

                self.model.insertar_usuario(nombre, usuario, contraseña, telefono, True, tipo_usuario_num, id_empresa)

            agregar_button.clicked.connect(insertar_usuario)

            #limpiar los campos de texto al agregar un usuario
            agregar_button.clicked.connect(nombre_input.clear)
            agregar_button.clicked.connect(usuario_input.clear)
            agregar_button.clicked.connect(contraseña_input.clear)
            agregar_button.clicked.connect(telefono_input.clear)
            agregar_button.clicked.connect(id_empresa_input.clear)

            layout.addRow(agregar_button)
            
            formulario.setLayout(layout)
            
            self.contenido = formulario
            self.layout.replaceWidget(self.layout.itemAt(1).widget(), formulario)

    def mostrar_estadisticas(self):
        self.contenido.hide()
        estadisticas_content = QtWidgets.QLabel("Estadísticas de la Administración")
        #Crear una tabla con las  columnas de ID pedido, Precio, Fecha
        pedidos = self.model.obtener_pedidos_finalizados()
        resultados_label = QLabel("Pedidos finalizados:")
        resultados_text = QLabel("\n".join([f"{pedido['IdPedido']}: {pedido['Precio']}: {pedido['FechaYHora']}" for pedido in pedidos]))
        layout = QVBoxLayout()
        layout.addWidget(resultados_label)
        layout.addWidget(resultados_text)
        estadisticas_content.setLayout(layout)

        self.contenido = estadisticas_content
        self.layout.replaceWidget(self.layout.itemAt(1).widget(), estadisticas_content)
    
    def cerrar_sesion(self):
        self.close()
        import sys
        import os
        ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        sys.path.append(ruta_proyecto)
        from main import LoginApp
    
        window = LoginApp()
        window.show()
