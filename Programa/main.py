import sys
from PyQt5 import QtWidgets
from views.login_ui import Ui_IniciarSesion
from views.pedidos.pedidos_ui import Ui_pedidos
from controllers.loginController import LoginController
from controllers.UsuariosController import UsersController

class PedidosWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pedidos()
        self.ui.setupUi(self)

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_IniciarSesion()
        self.ui.setupUi(self)
        self.controller = LoginController(dbname="FoodAlfa.V4", user="postgres", password="0000", host="localhost", port=5432)
        self.ui.submit.clicked.connect(self.login)
        self.ui.checkBox.stateChanged.connect(lambda: self.controller.toggleMostrarContrasena(self.ui))        
        self.ui.ir_a_pedidos.clicked.connect(self.redirect_to_pedidos)  # Cambia esta línea
        #LLamar el controlador de usuarios
        self.UserController = UsersController()

    def login(self):
        username = self.ui.usuario.text()
        password = self.ui.contrasena.text()

        if self.controller.authenticate(username, password):
            self.UserController.show(username, password)
            self.close()
        else:
            print("Credenciales incorrectas")
            
    def redirect_to_pedidos(self):
        self.pedidos_window = PedidosWindow()  # Reemplaza PedidosWindow con el nombre correcto de tu ventana de pedidos
        self.pedidos_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())






