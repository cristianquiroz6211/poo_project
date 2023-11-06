# usersController.py

import sys
import os
from PyQt5 import QtWidgets

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)

from views.Usuarios.Usuarios_ui import UsersView
from controllers.loginController import LoginController

class UsersController:
    def __init__(self):

        self.view = UsersView()
        self.view.btn_admin_local.clicked.connect(self.open_admin_local)
        self.view.btn_logout.clicked.connect(self.logout)
        # Controlador de inicio de sesión
        self.loginController = LoginController("FoodAlfa.V4", "postgres", "0000", "localhost", 5432)

        
    def show(self):
        if self.Validate("DanielP", "1234"):
            self.view.show()
        else:
            print("Usuario o contraseña incorrecta")
    
    def Validate(self, username, password):
        return self.loginController.authenticate(username, password)
        
    def open_admin_local(self):
        self.view.hide()
        self.login_controller.abrir_admin_local()
    
    def logout(self):
        self.view.hide()
        self.login_controller.logout()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    users_controller = UsersController()
    users_controller.show()
    sys.exit(app.exec_())
