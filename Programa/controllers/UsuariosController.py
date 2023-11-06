# usersController.py

import sys
import os
from PyQt5 import QtWidgets

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio del proyecto al sys.path
sys.path.append(ruta_proyecto)

from views.Usuarios.AdministradorGeneral_ui import AdministradorGeneralView
from views.Usuarios.AdministradorLocal_ui import AdministradorLocalView
from models.usuariosModel import UsuariosModel

class UsersController:
    def __init__(self):
        self.viewAdminGeneral = AdministradorGeneralView()
        self.viewAdminLocal = AdministradorLocalView()
        self.ModelUser = UsuariosModel(dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432)

    def show(self, username, password):
        rol = self.ModelUser.obtener_rol_por_usuario(username)
        if rol == 1:
            self.viewAdminGeneral.show()
        elif rol == 2:
            self.viewAdminLocal.show()
        else:
            print("No se reconoce el rol del usuario")


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    users_controller = UsersController()
    users_controller.show()
    sys.exit(app.exec_())
