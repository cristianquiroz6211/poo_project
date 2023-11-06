import sys
import os
from PyQt5 import QtWidgets

# Obtener la ruta al directorio del proyecto
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)


from models.loginModel import LoginModel

class LoginController:
    def __init__(self, dbname, user, password, host, port):
        self.model = LoginModel(dbname, user, password, host, port)

    def authenticate(self, username, password):
        estado = True
        return self.model.authenticate(username, password,estado)
    
    def toggleMostrarContrasena(self, ui):
        if ui.checkBox.isChecked():
            ui.contrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            ui.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
    def abrir_pedidos(self):
        from views.pedidos.pedidos_ui import Ui_MainWindow
        self.pedidos_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.pedidos_window)
        self.pedidos_window.show()

    def abrir_admin_local(self):
        from views.Usuarios.Usuarios_ui import UsersView
        self.admin_local_window = QtWidgets.QMainWindow()
        ui = UsersView()
        ui.setupUi(self.admin_local_window)
        self.admin_local_window.show()
    
    def logout(self):
        from views.login_ui import Ui_IniciarSesion
        self.login_window = QtWidgets.QMainWindow()
        ui = Ui_IniciarSesion()
        ui.setupUi(self.login_window)
        self.login_window.show()
