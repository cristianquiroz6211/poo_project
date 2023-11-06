# usersController.py

import sys
import os
from PyQt5 import QtWidgets

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)

from views.Usuarios.Usuarios_ui import UsersView

class UsersController:
    def __init__(self):
        self.view = UsersView()


    def show(self, username, password,rol):
        self.view.show()
        

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    users_controller = UsersController()
    users_controller.show()
    sys.exit(app.exec_())
