from BaseDatos import *
from Usuario import *

conexion = BaseDatos("localhost",5432,"postgres","0000","Usuarios")
conexion.Conectar()

Usuario1 = Usuario("Mariana","Rios","1234567890")
Usuario1 = Usuario("Daniel","Puerta","1040870522")


# Usuario1.ActualizarUsario(conexion.Conectar(),"2","juan","lopers")
# Usuario1.consulta(conexion.Conectar())

# Usuario1.EliminarUsuarios(conexion.Conectar(),"3")


# Usuario1.crearUsuarios(conexion.Conectar(),"Mariana","Rios")